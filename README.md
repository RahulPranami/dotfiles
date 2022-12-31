# dotfiles

## how to backup dotfiles

> git init $HOME/.dotfiles

> alias dotfiles='git --git-dir=$HOME/.dotfiles/.git --work-tree=$HOME'

> echo "alias dotfiles='git --git-dir=$HOME/.dotfiles/.git --work-tree=$HOME'" >> $HOME/.zshrc

> source $HOME/.zshrc

> dotfiles config --local status.showUntrackedFiles no

> dotfiles add .vimrc .zshrc

> ln -f 


 -- ubuntu @ 18.208.34.138
