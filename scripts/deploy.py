from brownie import NineTailsToken, accounts

def main():
    with open('wallet.txt', 'r') as file:
        deployer_wallet_address = file.read()
    initial_supply = 1000000 * 10**18
    ninetails = NineTailsToken.deploy(initial_supply, {'from': deployer_wallet_address})
    return ninetails