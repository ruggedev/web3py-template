import helper

endpoint = 'https://api.avax.network/ext/bc/C/rpc' # Avalanche Mainnet
web3 = helper.web3_connector(endpoint)

token_address = '0x6e84a6216eA6dACC71eE8E6b0a5B7322EEbC0fDd' # Joe Token
token_abi = helper.abi_loader("./abis/SimpleToken.json")
token_contract = helper.contract_loader(web3, token_address, token_abi)


totalSupply = token_contract.functions.totalSupply().call()
print(totalSupply)
