from brownie import NftMarketPlace
from scripts.helpful_scripts import get_account


def deploy_market_place():
    account = get_account()
    market_place = NftMarketPlace.deploy({"from": account})
    print(f"NFT Market place deployed at {market_place.address}")


def main():
    deploy_market_place()
