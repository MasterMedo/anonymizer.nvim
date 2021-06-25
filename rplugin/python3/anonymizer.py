import pynvim


@pynvim.plugin
class BufferAnonymizer(object):
    def __init__(self, nvim):
        self.nvim = nvim

    @pynvim.function("AnonymizeBuffer")
    def anonymize_buffer(self, args):
        self.anonymize(*args)

    def anonymize(self, left='<', right='>', mid='=', solo='o'):
        src = self.nvim.new_highlight_source()
        top_line = self.nvim.funcs.line("w0")
        bottom_line = self.nvim.funcs.line("w$")
        lines = self.nvim.funcs.getline(top_line, bottom_line)
        for lnum, line in enumerate(lines, top_line):
            new_line = ' '
            blobs = self.get_syn_groups(lnum, line)
            for synid, start, end in blobs:
                new_line += ' ' * (start - len(new_line) + 1)
                if start == end:
                    raise Exception(f'start and end are the same: {start}')
                if start + 1 == end:
                    new_line += solo
                else:
                    new_line += left
                    for col in range(start + 1, end - 1):
                        new_line += mid
                    new_line += right

            self.nvim.current.buffer[lnum - 1] = new_line[2:]
            for synid, start, end in blobs:
                self.nvim.current.buffer.add_highlight(
                    self.nvim.funcs.synIDattr(synid, 'name'),
                    lnum - 1,
                    start - 1,
                    end - 1,
                    src_id=src
                )

    def get_syn_groups(self, lnum, line):
        blobs = []
        started = False
        for col, char in enumerate(line, 1):
            if not started:
                if char.isspace():
                    continue
                else:
                    started = True
                    start = col
                    synid = self.nvim.funcs.synID(lnum, col, False)

            new_synid = self.nvim.funcs.synID(lnum, col, 1)
            if char.isspace():
                if line[col - 2].isspace():
                    blobs.append([
                        synid,
                        start,
                        col - 1
                    ])
                    started = False
                continue

            colour = self.nvim.funcs.synIDattr(
                self.nvim.funcs.synIDtrans(synid), "fg")
            new_colour = self.nvim.funcs.synIDattr(
                self.nvim.funcs.synIDtrans(new_synid), "fg")
            if colour != new_colour:
                blobs.append([
                    synid,
                    start,
                    col - 1 if line[col - 2].isspace() else col
                ])
                synid = new_synid
                start = col

        if started:
            blobs.append([synid, start, col + 1])
        return blobs
