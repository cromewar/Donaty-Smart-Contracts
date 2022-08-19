from brownie import (
    DonatyNFTFactory,
    network,
    config,
    NftMarketPlace,
    DonatyNFT,
    Contract,
)
from scripts.helpful_scripts import get_account


def test_can_deploy_and_create():
    account = get_account()
    nft_factory = DonatyNFTFactory.deploy({"from": account})
    print(f"New NFT Factory contract created at {nft_factory.address}")
    tx = nft_factory.createNFTContract("Donaty", "DON")
    tx.wait(1)
    contract_address = nft_factory.getNFTContract(0)
    print(f"contract adddres: {contract_address}")
    assert contract_address != "0x0000000000000000000000000000000000000000"


def test_can_deploy_create_and_approve():
    account = get_account()
    market_place = NftMarketPlace.deploy({"from": account})
    nft_factory = DonatyNFTFactory.deploy({"from": account})
    tx = nft_factory.createNFTContract(
        "Donaty",
        "DON",
        50,
        [],
        [],
        "Cause",
        "Date1",
        "Date2",
        3,
        1,
        "https//ipfs.com",
        [],
        {"from": account},
    )
    tx.wait(1)
    nft_contract = Contract.from_abi(
        "DonatyNFT", nft_factory.getNFTContract(0), DonatyNFT.abi
    )
    tx2 = nft_factory.createCollectibleAndApproveMarket(
        nft_contract.address,
        account.address,
        "https//ipfs.com",
        market_place.address,
        {"from": account},
    )
    tx2.wait(1)
