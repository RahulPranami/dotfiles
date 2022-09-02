set nocompatible
filetype on
syntax on
set number
set cursorline
" set cursorcolumn
filetype plugin on
filetype indent on
set ignorecase
set smartcase
set showcmd
set showmode
set showmatch

set hlsearch
set wildmenu

" " Plugins

call plug#begin()

Plug 'scrooloose/nerdtree'
Plug 'airblade/vim-gitgutter'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
" Plug 'valloric/youcompleteme'
" Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
" Plug 'junegunn/fzf.vim'
" Plug 'w0rp/ale'
" Plug 'mattn/emmet-vim'
" Plug 'junegunn/vim-easy-align'
" Plug 'https://github.com/junegunn/vim-github-dashboard.git'

" Plug 'tpope/vim-sensible'
Plug 'arcticicestudio/nord-vim'
Plug 'catppuccin/nvim', {'as':'catppuccin'}

call plug#end()