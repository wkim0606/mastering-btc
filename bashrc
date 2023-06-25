#!/user/bin/env bash
alias rm='rm -i'
alias l='ls -al'

# Terminal Setting, if color is strange, delete #
# export LS_COLORS="di=01;37;fi=01;37"

# Bitcoin command aliases

alias getbalance='bitcoin-cli -regtest -rpcuser=test -rpcpassword=test -rpcport=12345 -rpcconnect="127.0.0.1" -datadir="/bitcoin/node1" getbalance'

# TX listunspent
alias listunspent='bitcoin-cli -regtest -rpcuser=test -rpcpassword=test -rpcport=12345 -rpcconnect="127.0.0.1" -datadir="/bitcoin/node1" listunspent'


alias getnewaddress='bitcoin-cli -regtest -rpcuser=test -rpcpassword=test -rpcport=12345 -rpcconnect="127.0.0.1" -datadir="/bitcoin/node1" getnewaddress'

alias getblockcount='bitcoin-cli -regtest -rpcuser=test -rpcpassword=test -rpcport=12345 -rpcconnect="127.0.0.1" -datadir="/bitcoin/node1" getblockcount'

# getblock "block hash id"
alias getblock='bitcoin-cli -regtest -rpcuser=test -rpcpassword=test -rpcport=12345 -rpcconnect="127.0.0.1" -datadir="/bitcoin/node1" getblock'

# send bitcoin to address
alias sendtoaddress='bitcoin-cli -regtest -rpcuser=test -rpcpassword=test -rpcport=12345 -rpcconnect="127.0.0.1" -datadir="/bitcoin/node1" sendtoaddress'

# bitcoin block generate
alias generate='bitcoin-cli -regtest -rpcuser=test -rpcpassword=test -rpcport=12345 -datadir="$PWD/node1" generate'

# bitcoin listaccounts
alias listaccounts='bitcoin-cli -regtest -rpcuser=test -rpcpassword=test -rpcport=12345 -datadir="$PWD/node1" listaccounts'

# bitcoin start_node1_deprecated.sh
alias start_node1_deprecated='bitcoind -regtest -rpcuser=test -rpcpassword=test -rpcport=12345 -port=123456 -datadir="$PWD/node1" -deprecatedrpc=accounts'
