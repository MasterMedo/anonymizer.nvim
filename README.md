# neovim buffer anonymizer

1. set up python path in your init.vim
```vim
let g:python3_host_prog = '/usr/bin/python3'
let g:python_host_prog = '/usr/bin/python2'
```
2. add plugin
```vim
Plug 'mastermedo/anonymizer.vim'
```
3. install and update remote plugins
```vim
:PlugInstall
:UpdateRemotePlugins
```
4. restart neovim
5. use anonymizer
```
map <leader><leader> :call AnonymizeBuffer()<cr>
map <leader><leader> :call AnonymizeBuffer('(', ')', '#', 'O')<cr>
```

### TODO
- characters of variable length/bytes (unicode)
- one click undo
- optimise code
- update as buffer view moves
- switch to vimscript or lua
