from brownie import NFTMarketPlaceFactory
from scripts.helpful_scripts import get_account


def test_market_factory():
    account = get_account()
    account2 = get_account(3)
    market_factory = NFTMarketPlaceFactory.deploy({"from": account})
    print(f"NFT Market place factory deployed at {market_factory.address}")

    tx = market_factory.createNewMarketPlace(account2, {"from": account})
    tx.wait(1)
