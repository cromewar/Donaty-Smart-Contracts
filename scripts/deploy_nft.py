from brownie import DonatyNFT, network, config
from scripts.helpful_scripts import get_account


def deploy_nft():
    account = get_account()
    nft = DonatyNFT.deploy("Donaty", "DON", {"from": account})
    print(f"New NFT contract created at {nft.address}")


def main():
    deploy_nft()
