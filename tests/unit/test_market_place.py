from re import U
from brownie import NftMarketPlace, DonatyNFT, exceptions
from scripts.helpful_scripts import get_account
from web3 import Web3
import pytest


TOKEN_ID = 0
PRICE = Web3.toWei(0.1, "ether")
ZERO_ADDRESS = "0x0000000000000000000000000000000000000000"


def test_list_item():
    deployer = get_account()
    market_place = NftMarketPlace.deploy({"from": deployer})
    nft_contract = DonatyNFT.deploy("Donaty", "DON", {"from": deployer})
    tx = nft_contract.createCollectible(
        deployer.address, "http://ipfs.com", {"from": deployer}
    )
    tx.wait(1)
    tx2 = nft_contract.approve(market_place.address, TOKEN_ID, {"from": deployer})
    tx2.wait(1)
    # list NFT
    market_place.listItem(nft_contract.address, TOKEN_ID, PRICE, {"from": deployer})
    listed_item = market_place.getListing(nft_contract.address, TOKEN_ID)
    assert listed_item["price"] == PRICE


def test_cant_list_twice():
    deployer = get_account()
    market_place = NftMarketPlace.deploy({"from": deployer})
    nft_contract = DonatyNFT.deploy("Donaty", "DON", {"from": deployer})
    tx = nft_contract.createCollectible(
        deployer.address, "http://ipfs.com", {"from": deployer}
    )
    tx.wait(1)
    tx2 = nft_contract.approve(market_place.address, TOKEN_ID, {"from": deployer})
    tx2.wait(1)
    market_place.listItem(nft_contract.address, TOKEN_ID, PRICE, {"from": deployer})
    with pytest.raises(exceptions.VirtualMachineError):
        market_place.listItem(nft_contract.address, TOKEN_ID, PRICE, {"from": deployer})


def test_just_owner_can_list():
    deployer = get_account()
    user = get_account(2)
    market_place = NftMarketPlace.deploy({"from": deployer})
    nft_contract = DonatyNFT.deploy("Donaty", "DON", {"from": deployer})
    tx = nft_contract.createCollectible(
        deployer.address, "http://ipfs.com", {"from": deployer}
    )
    tx.wait(1)
    with pytest.raises(exceptions.VirtualMachineError):
        tx2 = nft_contract.approve(market_place.address, TOKEN_ID, {"from": user})
        tx2.wait(1)


def test_needs_approval_to_list():
    deployer = get_account()
    market_place = NftMarketPlace.deploy({"from": deployer})
    nft_contract = DonatyNFT.deploy("Donaty", "DON", {"from": deployer})
    tx = nft_contract.createCollectible(
        deployer.address, "http://ipfs.com", {"from": deployer}
    )
    tx.wait(1)
    tx2 = nft_contract.approve(ZERO_ADDRESS, TOKEN_ID, {"from": deployer})
    tx2.wait(1)
    with pytest.raises(exceptions.VirtualMachineError):
        market_place.listItem(nft_contract.address, TOKEN_ID, PRICE, {"from": deployer})
