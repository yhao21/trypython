
from web3 import Web3

# you can find this endpoint in your own project dashboard
endpoint = 'https://mainnet.infura.io/v3/94f7b92334c54d169af1a144242a1ccd'

web3 = Web3(Web3.HTTPProvider(endpoint))
# current block number
print(web3.eth.blockNumber)




bitdao_balance = web3.eth.get_balance('0x3F7b35C3492584FF5E1498866037deB0DAa7f5Fa')
print(bitdao_balance)

#check_stat = web3.toChecksumAddress('0x3f7b35c3492584ff5e1498866037deb0daa7f5fa'.lower())
#print(check_stat)


