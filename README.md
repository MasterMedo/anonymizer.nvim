<h1 align="center">
  anonymizer.nvim
</h1>
<p align="center">Anonymize your neovim buffer.</p>
<a href="https://github.com/inkarkat/vim-mark/issues/37">
  <p align="right">(how it all started)</p>
</a>

<p align="center">
  <a href="https://github.com/mastermedo/anonymizer.nvim/LICENSE">
    <img src="https://img.shields.io/github/license/mastermedo/anonymizer.nvim" alt="license" title="license"/>
  </a>
  <a href="https://github.com/mastermedo/anonymizer.nvim">
    <img src="https://img.shields.io/github/languages/code-size/mastermedo/anonymizer.nvim" alt="build" title="build"/>
  </a>
  <a href="https://github.com/mastermedo/anonymizer.nvim/stargazers">
    <img src="https://img.shields.io/badge/maintainer-mastermedo-yellow" alt="maintainer" title="maintainer"/>
  </a>
</p>

<p align="center">
  <a href="https://github.com/mastermedo/anonymizer.nvim">
    <img src="https://user-images.githubusercontent.com/16375100/123435258-ab119400-d5cd-11eb-9e4a-7643b96fba38.gif" alt="demo" title="demo"/>
  </a>
</p>

## :clipboard: description
Anonymizes your neovim buffer by transforming every visible character into a character of your choice, while keeping the color the character had before the transformation.

## :zap: features
- choose leftmost character, default `(`
- choose rightmost character, default `)`
- choose middle character, default `#`
- choose alone character, default `O`

## :shipit: installation
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

## :question: usage
```vim
map <leader><leader> :call AnonymizeBuffer()<cr>
```

## :bulb: TODO
- characters of variable length/bytes (unicode)
- one click undo
- optimise code
- update as buffer view moves
- switch to vimscript or lua

<p align="center">
  <a href="#">
    <img src="https://img.shields.io/badge/⬆️back_to_top_⬆️-white" alt="Back to top" title="Back to top"/>
  </a>
</p>
