
# Project setup

Install remix in project terminal (get node at nodejs.org):
`npm i -g @remix-project/remixd`

Run remix in project terminal
`remixd -s .`

In a browser, go to remix.ethereum.org and in "Workspace" select localhost.

You should be able to see your repo


# Contract schema

https://docs.google.com/presentation/d/1Vlu4eKyztd7EDq0PdN5ekq4mLXy3iRHMEaiKlnIRDBY/edit?usp=sharing

# Service used to pin IPFS files

app.pinata.cloud

https://ipfs.io/ipfs/QmbKAgUgopYKA4dHbwd5uKBSoBUPZE9AS3pxUy8V2xtS4j

# To check all smart contracts deployed from your address

https://ropsten.etherscan.io/address/YOUR_ADDRESS


# GO ETHEREUM INSTALL (GETH)

Download instruction on https://geth.ethereum.org/

### Generate desired config file. You must specify testnet here.

** In the folder that will receive data **
geth --ropsten --syncmode "full"  dumpconfig > roptsten.toml

### Start geth with given config file. Here too the testnet must be specified.
geth --ropsten --config ropsten.toml --http


To test curl : curl --data "{/"jsonrpc/":/"2.0/",/"method/":/"eth_coinbase/", /"id/":1}" localhost:8545

curl --location --request POST /"localhost:8545/" --header /"Content-Type: application/json/" --data-raw "{ /"jsonrpc/":/"2.0/",  /"method/":/"web3_clientVersion/",/"params/":[], "id/":1 }"

Use postman to test
https://documenter.getpostman.com/view/4117254/ethereum-json-rpc/RVu7CT5J

URL
localhost:8545/

HEADER
Content-Type        application/json

BODY : Raw
{
	"jsonrpc":"2.0",
	"method":"web3_clientVersion",
	"params":[],
	"id":1
}