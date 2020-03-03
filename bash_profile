# .bash_profile
# Get the aliases and functions

if [ -f ~/.bashrc ]; then
	. ~/.bashrc
fi
PATH=$PATH:$HOME:$HOME/node1
export PATH
export PS1='\u@\h \w$ '
