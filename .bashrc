[robcat@arch-netbook ~]$ cat /etc/skel/.bashrc 
#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '

# neofetch

if [ -e $HOME/.bash_aliases ]; then
	source $HOME/.bash_aliases
fi