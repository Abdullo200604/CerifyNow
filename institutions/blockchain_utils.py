from web3 import Web3
from dotenv import load_dotenv
import os

load_dotenv()

INFURA_URL = os.getenv('INFURA_URL')
PRIVATE_KEY = os.getenv('PRIVATE_KEY')
CONTRACT_ADDRESS = os.getenv('CONTRACT_ADDRESS')
WALLET_ADDRESS = os.getenv('WALLET_ADDRESS')

# Remix'dan olingan ABI to'liq list ko'rinishida
contract_abi = [
    {
        "inputs": [{"internalType": "bytes32", "name": "docHash", "type": "bytes32"}],
        "name": "addDocumentHash",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [{"internalType": "bytes32", "name": "", "type": "bytes32"}],
        "name": "documentOwner",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [{"internalType": "bytes32", "name": "docHash", "type": "bytes32"}],
        "name": "getOwner",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function"
    }
]

w3 = Web3(Web3.HTTPProvider(INFURA_URL))
contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=contract_abi)

def save_hash_to_blockchain(hash_value):
    # Bu yerda hash_value = '0x...' ko'rinishida bo'lishi kerak
    tx = contract.functions.addDocumentHash(hash_value).build_transaction({
        'from': WALLET_ADDRESS,
        'nonce': w3.eth.get_transaction_count(WALLET_ADDRESS),
        'gas': 300000,
        'gasPrice': w3.to_wei('20', 'gwei')
    })
    signed_tx = w3.eth.account.sign_transaction(tx, PRIVATE_KEY)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    return tx_hash.hex()
