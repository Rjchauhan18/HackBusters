
from dotenv.main import load_dotenv
import os

from web3 import Web3
load_dotenv('/home/rahul/Desktop/dApp/.env')

infura_url= os.getenv('infura_url')
ganachi_url= os.getenv('ganachi_url')


w3 = Web3(Web3.HTTPProvider(ganachi_url))
print(w3.is_connected())

print( w3.eth.block_number)


acc1=""
acc2=""

balance = w3.eth.get_balance("")
print(w3.from_wei(balance, 'ether'))