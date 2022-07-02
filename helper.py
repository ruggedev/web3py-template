from web3 import Web3
import json

def web3_connector(endpoint):
  provider = Web3(Web3.HTTPProvider(endpoint))
  if provider.isConnected():
    print(f'Web3 connected to {endpoint}')
    return provider
  else:
    print('Web3 Connection failed.')

def abi_loader(file_path):
  with open(file_path) as f:
    return json.load(f)

def contract_loader(provider, address, contract_abi):
  _address = Web3.toChecksumAddress(address)
  return provider.eth.contract(address=_address, abi=contract_abi)
