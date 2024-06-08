from brownie import NineTailsToken, accounts

def main():
    deployer_wallet_address = "0x79d519E1549bd610d6EFB89FA41405dBB7E738E3"

    initial_supply = 1000000 * 10**18
    ninetails = NineTailsToken.deploy(initial_supply, {'from': deployer_wallet_address})
    return ninetails