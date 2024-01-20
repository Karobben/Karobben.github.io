---
toc: true
url: nvimr
covercopy: <a href="https://www.freecodecamp.org/news/turning-vim-into-an-r-ide-cd9602e8c217/">© freecodecamp</a>
priority: 10000
date: 2024-01-03 14:42:34
title: "Using Vim as Python and R IDE"
ytitle: "Using Vim as Python and R IDE"
description: "Using Vim as Python and R IDE, easy configure"
excerpt: "Using Vim as R IDE"
tags: [vim, IDE]
category: [Linux]
cover: "https://cdn-media-1.freecodecamp.org/images/1*cRo1ybQbVMMbAHRjgUhXqg.png"
thumbnail: "https://cdn-media-1.freecodecamp.org/images/1*cRo1ybQbVMMbAHRjgUhXqg.png"
---

## Using Vim as IDE

Vim is a classic text editor known for efficiency, while NeoVim is its modernized fork with improvements like better plugin support. LunarVim, built on NeoVim, offers a pre-configured setup, making it easier for users to get a powerful, feature-rich environment without the hassle of individual configurations. Ideal for those new to Vim/NeoVim or seeking a ready-to-use development setup, LunarVim combines ease of setup with customizability. It's particularly appealing for its integrated toolset, active community support, and a balance between functionality and performance, making it a great choice for a streamlined coding experience.

Plug: [Nvim-R](https://github.com/jamespeapen/Nvim-R/wiki)
Video Tutorial: [Rohit Farmer](https://www.youtube.com/watch?v=nm45WagtV3w)
Instruction following the video: [rohitfarmer](https://gist.github.com/rohitfarmer/68cdadeaeeb196e8a6ecdebdee6e76a5)

Final work:
|![Using vim as R IDE](https://imgur.com/Pdzomq1.png)|
|:-:|
|© Karobben|

## Installation

Please install the latest NeoVim by following the [Neovim document](https://github.com/neovim/neovim/blob/master/INSTALL.md) and [LunarVim Document](https://www.lunarvim.org/docs/installation)

```bash
# install neovim
# sudo apt install neovim
# install vim-plug
curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

# for storing the config file
mkdir ~/.config/nvim
touch ~/.config/nvim/init.vim
# for storing plug
# because all plug would be installed by here, you could just delete the directories here to delete plugs.
mkdir ~/.vim/plugged
# open and edit the config file
vim ~/.config/nvim/init.vim
```

Save the lines below in the `~/.config/nvim/init.vim` file to install the pluges.

<pre>
" Specify a directory for plugins
" - Avoid using standard Vim directory names like 'plugin'
call plug#begin('~/.vim/plugged')

" List of plugins.
" Make sure you use single quotes

" Shorthand notation
Plug 'jalvesaq/Nvim-R', { 'branch' : 'stable' }
Plug 'ncm2/ncm2'
Plug 'roxma/nvim-yarp'
Plug 'gaalcaras/ncm-R'
Plug 'preservim/nerdtree'
Plug 'Raimondi/delimitMate'
Plug 'patstockwell/vim-monokai-tasty'
Plug 'itchyny/lightline.vim'

" Initialize plugin system
call plug#end()
</pre>


!!! note How to instsall the plunges
    After stored the change, you need to open it again by using `nvim ~/.config/nvim/init.vim`. And then, under the command model (which is triggered by `:`), input `PlugInstall` (`PlugUpdate` if you want to update them). After you see the picture below which means you installed it successfully:![](https://imgur.com/SMB1YM3.png)

By following the instruction from [rohitfarmer](https://gist.github.com/rohitfarmer/68cdadeaeeb196e8a6ecdebdee6e76a5)'s post, we could add more things at the end of the `init.vim` file:


!!! note folding behavior
    <pre>
    " Set foldbehavior

    set tabstop=2        " Number of spaces that a <Tab> in the file counts for
    set shiftwidth=2     " Number of spaces to use for each step of (auto)indent
    set softtabstop=2    " Number of spaces that a <Tab> counts for while performing editing operations
    set expandtab        " Use spaces instead of tabs

    set foldmethod=indent
    set foldlevelstart=2    " Start folding at an indent level greater than 2
    </pre>

    For quick unfold all codes:
    <pre>:set nofoldenable</pre>


<pre>
" Set a Local Leader

" With a map leader it's possible to do extra key combinations
" like <leader>w saves the current file
let mapleader = ","
let g:mapleader = ","


" Plugin Related Settings

" NCM2
autocmd BufEnter * call ncm2#enable_for_buffer()    " To enable ncm2 for all buffers.
set completeopt=noinsert,menuone,noselect           " :help Ncm2PopupOpen for more
                                                    " information.

" NERD Tree
map <leader>nn :NERDTreeToggle<CR>                  " Toggle NERD tree.

" Monokai-tasty
let g:vim_monokai_tasty_italic = 1                  " Allow italics.
colorscheme vim-monokai-tasty                       " Enable monokai theme.

" LightLine.vim 
set laststatus=2              " To tell Vim we want to see the statusline.
let g:lightline = {
   \ 'colorscheme':'monokai_tasty',
   \ }


" General NVIM/VIM Settings

" Mouse Integration
set mouse=i                   " Enable mouse support in insert mode.

" Tabs & Navigation
map <leader>nt :tabnew<cr>    " To create a new tab.
map <leader>to :tabonly<cr>     " To close all other tabs (show only the current tab).
map <leader>tc :tabclose<cr>    " To close the current tab.
map <leader>tm :tabmove<cr>     " To move the current tab to next position.
map <leader>tn :tabn<cr>        " To swtich to next tab.
map <leader>tp :tabp<cr>        " To switch to previous tab.


" Line Numbers & Indentation
set backspace=indent,eol,start  " To make backscape work in all conditions.
set ma                          " To set mark a at current cursor location.
set number                      " To switch the line numbers on.
set expandtab                   " To enter spaces when tab is pressed.
set smarttab                    " To use smart tabs.
set autoindent                  " To copy indentation from current line 
                                " when starting a new line.
set si                          " To switch on smart indentation.


" Search
set ignorecase                  " To ignore case when searching.
set smartcase                   " When searching try to be smart about cases.
set hlsearch                    " To highlight search results.
set incsearch                   " To make search act like search in modern browsers.
set magic                       " For regular expressions turn magic on.


" Brackets
set showmatch                   " To show matching brackets when text indicator 
                                " is over them.
set mat=2                       " How many tenths of a second to blink 
                                " when matching brackets.


" Errors
set noerrorbells                " No annoying sound on errors.


" Color & Fonts
syntax enable                   " Enable syntax highlighting.
set encoding=utf8                " Set utf8 as standard encoding and 
                                 " en_US as the standard language.

" Enable 256 colors palette in Gnome Terminal.
if $COLORTERM == 'gnome-terminal'
    set t_Co=256
endif

try
    colorscheme desert
catch
endtry


" Files & Backup
set nobackup                     " Turn off backup.
set nowb                         " Don't backup before overwriting a file.
set noswapfile                   " Don't create a swap file.
set ffs=unix,dos,mac             " Use Unix as the standard file type.


" Return to last edit position when opening files
au BufReadPost * if line("'\"") > 1 && line("'\"") <= line("$") | exe "normal! g'\"" | endif
</pre>


## Basic Usage of Nvim-R

<pre>
Ctrl + W + HJKL   " Remove the cursor from window to window
,nt               " Open a new tab
,tn               " Move to the next tab
,tp               " Back to the previous tab

# code fold behavior
zc - Close (fold) the current fold under the cursor.
zo - Open (unfold) the current fold under the cursor.
za - Toggle between closing and opening the fold under the cursor.
zR - Open all folds in the current buffer.
zM - Close all folds in the current buffer.

# Nvim-R
Ctrl + x + o      " Access the help information (auto fill)
\rf               " Connect to R console.
\rq               " Quit R console.
\ro               " Open object bowser.
\d                " Execute current line of code and move to the next line.
\ss               " Execute a block of selected code.
\aa               " Execute the entire script. This is equivalent to source().
\xx               " Toggle comment in an R script.

# NERDTree
,nn               " Toggle NERDTree.

</pre>

## Basic codes for nvim

You could also included them into the `vim.init` file

```bash
# wrap the words in it is too long
:set wrap 
:set nowrap
# set the wrap behavior
:set showbreak=↪\ 
```

## Bugs

After installed the Nvim-R (them master branch), you'll have the error code below whenever you open nvim. Just ignore it and it would be fine.
<pre>
Error detected while processing function ROnJobStdout[40]..UpdateSynRhlist[11]..FunHiOtherBf:
line   10:
E117: Unknown function: nvim_set_option_value
Press ENTER or type command to continue
</pre>


## Configure for LuanrVim

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
cat "$HOME/.cargo/env" >> ~/.zshrc
source ~/.zshrc

# install LunarVim
LV_BRANCH='release-1.3/neovim-0.9' bash <(curl -s https://raw.githubusercontent.com/LunarVim/LunarVim/release-1.3/neovim-0.9/utils/installer/install.sh)

rm -rf ~/.config/lvim/
git clone https://github.com/Karobben/kickstart.nvim.git ~/.config/lvim
```

### Nerd font

```bash
# curl -fsSL https://raw.githubusercontent.com/ronniedroid/getnf/master/install.sh | bash
mkdir -p ~/.local/share/fonts
cd ~/.local/share/fonts && curl -fLO https://github.com/ryanoasis/nerd-fonts/raw/HEAD/patched-fonts/DroidSansMono/DroidSansMNerdFont-Regular.otf
fc-cache -f -v
```

### Words Editing

For editing the word, we need to switch the model of read, visual, and editing. Press `i` enable the editing mode. Type `Esc` or `Ctrl + c` exist the editing mode and back to the reading mode. `v` enable selection model so you could select words.



```
i                   enter editing mode
dd                  cut the selected line into paste board
p                   paste the coppied contents
v                   selecte mode to selecte multiple words and lines
    wd              delete the selected words/lines
    y               copy the selected words/lines
    p               repalce the selected workds/lines with coppied contents
o                   Start a new line
:>                  Intend the selected line 
:>>                 Intend tiwce
:<                  Undo the intend
: m 10              Move the selected words/line into line 10
Alt+ j/k        Move selected words/lines up/donw
```


### Cursor Related

```
h                   moving left
j                   moving down
k                   moving up
l                   moving right
:10                 moving to line 10
w                   moving to the head of the next word
e                   moving to the end of the word
b                   moving to the head of the previous word
ge                  moving back to the end of the word

gg                  moving to the top of the file
G                   moving to the end of the file
Ctrl + f            page foward (donw)
Ctrl + b            page back (up)
```

```
<leader> e          open directory exploer
<leader> w          save the edit file (:w)

# about tab
<leader> bb         back to the tab left
<leader> bn         go to the next tab (right)
:bd                 close the current tab

<Alt> 1/2/3         open a terminal (only when you installed the pluges)
<Ctrl> w            swtich between windows

:set mouse-=a       Disable the mouse selection
:set mouse=a        Inable the mouse 
```

<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
