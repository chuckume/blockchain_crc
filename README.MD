
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
geth --ropsten --config d:\geth\ropsten.toml --http


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


Import Pkey to geth
geth account import --datadir D:\geth\data_dir ./key.prv

Connect metamask to geth
0xb504D3CAA96e90Bb5FDC06591f45Ef108C16e4f0
geth --datadir D:\geth\data_dir  --networkid 2018 --http --http.corsdomain “*” --http.api “admin,db,eth,miner,web3,net,personal,txpool” --allow-insecure-unlock --ropsten --syncmode "full"  dumpconfig > roptsten.toml

installé web3


# Ethereum Tutorial 
https://github.com/ethereumbook/ethereumbook/blob/develop/02intro.asciidoc#remix_compile

Shows how to create a faucet on ropsten

# Testnet options
- geth or parity
- Local blockchain : Ganache
- Cloud based client : Infuria
- Remote client (doesn't store blockchain dataa) : MetaMask, Emerald Wallet, MyEtherWallet, or MyCrypto

Light client : validate blocks, remote client dont



Json-Rpc example:
curl -X POST -H "Content-Type: application/json" --data \
'{"jsonrpc":"2.0","method":"web3_clientVersion","params":[],"id":1}' \
  http://localhost:8545

https://www.jsonrpc.org/specification

curl -X POST -H "Content-Type: application/json" --data \
  '{"jsonrpc":"2.0","method":"eth_gasPrice","params":[],"id":4213}' \
  http://localhost:8545
echo $((0x430e23400))

Chapter 4 cryptography

n simple terms, a hash function is “any function that can be used to map data of arbitrary size to data of fixed size.”

While you may see "SHA-3" mentioned throughout Ethereum documents and code, many if not all of those instances actually refer to Keccak-256, not the finalized FIPS-202 SHA-3 standard. The implementation differences are slight, having to do with padding parameters, but they are significant in that Keccak-256 produces different hash outputs from FIPS-202 SHA-3 for the same input.

Test vector: passing an empty vector and see th return
Keccak256("") = c5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470
SHA3("") = a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a


# Hello World source
https://mirabdulhaseeb.medium.com/truffle-vs-hardhat-vs-brownie-lets-compare-ea08b927d084



# DEFI

Uniswap
DAI (MakerDao)
Compound
Dharma

Defi protocols mostly provide liquidity for margin trading
They are also used for flash loans that are valid within one transaction.
There are zero risk because the borrower must be able to pay back the tokens otherwise the contract won't execute the trade. The borrower doesnt need collaterals.

Flash loans fail if: 1) Insufficient transaction fees, 2) conflicting transctions 3) anothe condition within the transaction cannot be met

Loans are backed by collaterals so they are guaranteed.

Flash attacks: capital intensive attacks on DEXes. Attacks vulnerabilites on untested contracts, low liquidity markets.
Can be used to manipulate data feeds about asset prices on illiquid markets.

Prices come from different exchanges with high spread, so one can profit by borrowing tokens at low price and selling at higher price before repaying the loan. This can be made within the same transactio since most defi run on Ethereum. Attackers can borrow almost unlimited amount of money to manipulate the market price .


Some DEX use liquidity pools.

Weaknesses:
- Oracles : data feeds can be manipulated.
- Vulnerable to flash attacks
- Not fully decentralized
- Not tested.
- Low user experience
- Low liquidity
- many Defi producct overcollateralieed
