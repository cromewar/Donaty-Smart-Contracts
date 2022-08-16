from brownie import NFTMarketPlaceFactory
from scripts.helpful_scripts import get_account


def deploy_marketplace_factory():
    account = get_account()
    marketplace_factory = NFTMarketPlaceFactory.deploy({"from": account})
    print(f"NFT Market place factory deployed at {marketplace_factory.address}")


def main():
    deploy_marketplace_factory()
