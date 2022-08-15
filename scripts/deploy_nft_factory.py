from brownie import DonatyNFTFactory, network, config
from scripts.helpful_scripts import get_account


def deploy_nft_factory():
    account = get_account()
    nft_factory = DonatyNFTFactory.deploy({"from": account})
    print(f"New NFT Factory contract created at {nft_factory.address}")


def main():
    deploy_nft_factory()
