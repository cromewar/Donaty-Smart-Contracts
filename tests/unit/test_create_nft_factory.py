from brownie import DonatyNFTFactory, network, config
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
