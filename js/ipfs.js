var ethers = require('ethers');
var url = 'https://mainnet.infura.io/v3/d90b320bfd7c4ada8a5fdc13b559fc7d'; //'ADD_YOUR_ETHEREUM_NODE_URL';
var provider = new ethers.providers.JsonRpcProvider(url);
var address  = '0xfCd8c2F1821Ab7F6f9297F2DbD47fb130e71F072';// 'CONTRACT_ADDRESS_FROM_REMIX';
var abi = [
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "x",
				"type": "string"
			}
		],
		"name": "sendHash",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getHash",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
];
var contract = new ethers.Contract(address,abi,provider);

contract.getHash().then((result) =>{
  document.getElementById("btn").onclick = function () {
//		location.href = "https://ipfs.io/ipfs/"+result;
		location.href = "https://gateway.pinata.cloud/ipfs/"+result;

  	};
});