
- smart contract :

* creating a simple smart contract with .sol extension
* sudo apt-get install solc   ---- solc is the compiler
* solc simple_smart_contract.sol --bin --abi --optimize -o ./compiled


- install the Geth on ubuntu using this command:

* sudo add-apt-repository -y ppa:ethereum/ethereum
* sudo apt update
* sudo apt-get install ethereum
* sudo apt install geth

- geth dev mode: (deploy)

* geth --datadir path account new
* save the password in path/secret.txt file
* sudo geth --datadir path --dev --unlock 'ACCOUNT_PUBLIC_ADDRESS' --password path/secret.txt
* in another terminal: geth attach url(geth attach path/geth.ipc)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


var simpleStorageContract = eth.contract(abi);
var simpleStorage = simpleStorageContract.new({from: eth.accounts[0], data: '0x{bin_value}', gas: 4700000})

var set_trx = simpleStorage.set(100, {from: eth.accounts[0]});
var get_trx = simpleStorage.get({from: eth.accounts[0]});



eth.getTransactionReceipt(set_trx)

the encoded data getted from previews line result.

using the chatGPT to decoding data (abi and encoded data sended to chatGPT)