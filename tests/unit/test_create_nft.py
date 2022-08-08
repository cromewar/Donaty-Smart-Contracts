from brownie import DonatyNFT, network, config
from scripts.helpful_scripts import get_account


def test_deploy_nft():
    account = get_account()
    nft = DonatyNFT.deploy("Donaty", "DON", {"from": account})
    print(f"New NFT contract created at {nft.address}")
    tx = nft.createCollectible(account.address, "http://google.com")
    tx.wait(1)
    user_balance = nft.balanceOf(account.address)
    assert user_balance == 1


def main():
    test_deploy_nft()
