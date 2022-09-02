alias ll='ls -l'
alias la='ls -la'
alias lt='ls --human-readable --size -1 -S --classify'
alias lm="ls -t -1"
alias ping='ping -c 5'
alias pig='ping -c 5 google.com'
alias gh="history|grep"
alias c='clear'
alias ..='cd ..'

# editing dotfiles
alias baa='vim ~/.bash_aliases; source ~/.bashrc'
alias zaa='vim ~/.zsh_aliases; source ~/.zshrc'
alias bs='vim ~/.config/bspwm/bspwmrc'
alias sx='vim ~/.config/sxhkd/sxhkdrc'
alias pol='vim ~/.config/polybar/'
alias qtl='vim ~/.config/qtile/'




# laptop specific
alias btr='cat /sys/class/power_supply/BAT0/capacity'
alias btrst='cat /sys/class/power_supply/BAT0/status'
alias bt='xrandr --output eDP1 --brightness '
alias bl='brightnessctl -d asus::kbd_backlight s '

# arch linux specific
alias update='sudo pacman -Syu'
alias download='sudo pacman -S --noconfirm'

#
alias mnt="mount | awk -F' ' '{printf\"%s\t%s\n\",\$1,\$3;}' | column -t | egrep ^/dev/ | sort"
alias count="find . -type f | wc -l"
alias ve="python3 -m venv ./venv"
alias va="source ./venv/bin/activate"
alias cpv="rsync -ah --info=progress2"
alias tcn="mv --force -t ~/.local/share/Trash"
alias startgit="cd 'git rev-parse --show-toplevel' && git checkout master && git pull"
alias cg="cd 'git rev-parse --show-toplevel'"
alias ipe='curl ipinfo.io/ip'
alias www='python3 -m SimpleHTTPServer 8000'
alias mount='mount |column -t'
# shortcut  for iptables and pass it via sudo#
alias ipt='sudo /sbin/iptables'
# display all rules #
alias iptlist='sudo /sbin/iptables -L -n -v --line-numbers'
alias iptlistin='sudo /sbin/iptables -L INPUT -n -v --line-numbers'
alias iptlistout='sudo /sbin/iptables -L OUTPUT -n -v --line-numbers'
alias iptlistfw='sudo /sbin/iptables -L FORWARD -n -v --line-numbers'
alias firewall=iptlist

alias shutdown='sudo /sbin/shutdown'
## pass options to free ##
alias meminfo='free -m -l -t'
 
## get top process eating memory
alias psmem='ps auxf | sort -nr -k 4'
alias psmem10='ps auxf | sort -nr -k 4 | head -10'
 
## get top process eating cpu ##
alias pscpu='ps auxf | sort -nr -k 3'
alias pscpu10='ps auxf | sort -nr -k 3 | head -10'
 
## Get server cpu info ##
alias cpuinfo='lscpu'
 
## older system use /proc/cpuinfo ##
##alias cpuinfo='less /proc/cpuinfo' ##
 
## get GPU ram on desktop / laptop##
alias gpumeminfo='grep -i --color memory /var/log/Xorg.0.log'

## set some other defaults ##
alias df='df -H'
alias du='du -ch'
 
# top is atop, just like vi is vim
alias top='atop'

# Git
alias gs='git status'
alias gst='git status -sb'
alias gl='git log'
alias ga='git add'
alias gaa='git add -A'
alias gca='git commit -a'
alias gc='git commit -m'
alias gcl='git clone'
# Wget
# alias wget='wget -c'


