# Understinading the basics of vim

## What is Vim?
- vi is the text editor
- Vim is an improved version of vi
- Vim stands for Vi IMproved

## Why Vim?
- Vim is available on all platforms (Linux, macOS, Windows)
- Vim is highly configurable, extensible, and customizable
- Vim is highly efficient, powerful, and productive


## How to install Vim?
```bash
sudo apt update
sudo apt install vim
```

## Modes
- Normal mode
- Insert mode
- Replace mode
- Visual mode
- Command mode

## Normal mode
- The default mode
- Used for navigation and editing
- Press `Esc` to enter normal mode

## Insert mode
- Used for inserting text
- Press `i` to enter insert mode
- Press `a` to enter insert mode after the cursor
- Press `o` to enter insert mode on the next line
- Press `O` to enter insert mode on the previous line
- Press `Esc` to exit insert mode

## Visual mode
- `v` to enter visual mode
- `V` to enter visual line mode
- `Ctrl + v` to enter visual block mode
- `d` to delete the selection
- `y` to copy the selection
- `p` to paste after the cursor
- `P` to paste before the cursor
- `~` to change the case of the selection


## Command mode
- `:` to enter command mode

## Basic commands
- `:w` to save the file
- `:w filename` to save the file as a different filename
- `:q` to quit the file
- `:wq` to save and quit the file
- `:q!` to quit without saving the file

## Showing line numbers
- `:set number` or `:set nu` to show line numbers
- `:set nonumber` or `:set nonu` to hide line numbers
- `:set number!` or `:set nu!` to toggle line numbers
- `:set relativenumber` or `:set rnu` to show relative line numbers
- `:set norelativenumber` or `:set nornu` to hide relative line numbers
- `:set relativenumber!` or `:set rnu!` to toggle relative line numbers


## Navigation
- `h` to move left
- `j` to move down
- `k` to move up
- `l` to move right
- `w` to move to the beginning of the next word
- `b` to move to the beginning of the previous word
- `e` to move to the end of the next word
- `0` to move to the beginning of the line
- `$` to move to the end of the line
- `gg` to move to the beginning of the file
- `G` to move to the end of the file
- `:n` or `nG` or `ngg` to move to the nth line
- `Ctrl + f` to move forward one page
- `Ctrl + b` to move backward one page
- `Ctrl + d` to move forward half a page
- `Ctrl + u` to move backward half a page

## Editing
- `x` to delete the character under the cursor
- `dd` to delete the line
- `yy` to copy the line
- `p` to paste the line
- `u` to undo the last change
- `Ctrl + r` to redo the last change


## Searching
- `/` to search forward
- `?` to search backward
- `n` to move to the next match
- `N` to move to the previous match
- `*` to search for the word under the cursor
- `#` to search for the word under the cursor in the backward direction

## Replace
- `r` to replace the character under the cursor
- `R` to enter replace mode
- `:%s/old/new/g` to replace all occurrences of `old` with `new`
- `:%s/old/new/gc` to replace all occurrences of `old` with `new` with confirmation


## VIM necessary commands
1. `gg` to move to the beginning of the file
2. `G` to move to the end of the file
3. `:n` or `nG` or `ngg` to move to the nth line
4. `0` to move to the beginning of the line
5. `$` to move to the end of the line
6. `i` to enter insert mode
7. `a` to enter insert mode after the cursor
8. `R` to enter replace mode
9. `Esc` to exit insert mode
10. `u` to undo the last change
11. `Ctrl + r` to redo the last change
12. `/` to search forward
backward direction
13. `?` to search backward
14. `n` to move to the next match
15. `N` to move to the previous match
16. `:%s/old/new/g` to replace all occurrences of `old` with `new`
17. `x` to delete the character under the cursor
18. `dd` to delete the line
19. `yy` to copy the line
20. `p` to paste the line
21. `:w` to save the file
22. `:q` to quit the file
23. `:wq` to save and quit the file
24. `:q!` to quit without saving the file
25. `:set nu!` to toggle line numbers



## VIM CHEAT SHEET
- https://devhints.io/vim
- https://vim.rtorr.com/
- https://vimdoc.sourceforge.net/htmldoc/

## VIM TUTORIALS
- https://www.openvim.com/
- https://www.vim.org/docs.php
- https://www.vimgolf.com/


