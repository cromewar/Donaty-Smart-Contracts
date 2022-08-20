from re import U
from brownie import (
    NftMarketPlace,
    DonatyNFT,
    exceptions,
    DonatyNFTFactory,
    TimeLockFactory,
    DonatyGovernanceFactory,
    NFTMarketPlaceFactory,
    Contract,
    TimeLock,
    DonatyGovernor,
)
from scripts.helpful_scripts import get_account
from web3 import Web3
import pytest


TOKEN_ID = 0
PRICE = Web3.toWei(1, "ether")
ZERO_ADDRESS = "0x0000000000000000000000000000000000000000"


def test_list_item():
    deployer = get_account()
    account2 = get_account(2)
    market_place = NftMarketPlace.deploy({"from": deployer})
    nft_contract = DonatyNFT.deploy("Donaty", "DON", {"from": deployer})
    tx = nft_contract.createCollectible(
        account2.address, "http://ipfs.com", {"from": account2}
    )
    tx.wait(1)
    tx2 = nft_contract.approve(market_place.address, TOKEN_ID, {"from": account2})
    tx2.wait(1)
    # list NFT
    market_place.listItem(nft_contract.address, TOKEN_ID, PRICE, {"from": account2})
    listed_item = market_place.getListing(nft_contract.address, TOKEN_ID)
    assert listed_item["price"] == PRICE


def test_all_market_flux():
    deployer = get_account()
    print(f"balance of deployer is {Web3.fromWei(deployer.balance(), 'ether')}")
    account2 = get_account(2)
    nft_factory = DonatyNFTFactory.deploy({"from": deployer})
    time_lock_factory = TimeLockFactory.deploy({"from": deployer})
    governance_factory = DonatyGovernanceFactory.deploy({"from": deployer})
    market_place_factory = NFTMarketPlaceFactory.deploy({"from": deployer})

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
        {"from": deployer},
    )
    tx.wait(1)
    donaty_nft = Contract.from_abi(
        "DonatyNFT", nft_factory.getNFTContract(0), DonatyNFT.abi
    )

    tx2 = time_lock_factory.createNewTimeLock(
        2, [], [], donaty_nft.address, {"from": deployer}
    )
    tx2.wait(1)
    time_lock = Contract.from_abi(
        "TimeLock", time_lock_factory.getTimeLock(0), TimeLock.abi
    )

    tx3 = governance_factory.createNewDao(
        donaty_nft.address,
        time_lock.address,
        donaty_nft.address,
        1,
        17280,
        0,
        {"from": deployer},
    )
    tx3.wait(1)

    governance_contract = Contract.from_abi(
        "DonatyGovernor", governance_factory.getGovernor(0), DonatyGovernor.abi
    )

    time_lock_executer_role = time_lock.EXECUTOR_ROLE()
    time_lock_proposer_role = time_lock.PROPOSER_ROLE()
    timelock_canceller_role = time_lock.CANCELLER_ROLE()
    roles = [time_lock_executer_role, time_lock_proposer_role, timelock_canceller_role]

    tx4 = time_lock_factory.addRole(
        roles,
        governance_contract.address,
        time_lock.address,
        donaty_nft.address,
        {"from": deployer},
    )
    tx4.wait(1)

    tx5 = market_place_factory.createNewMarketPlace(
        governance_contract.address, donaty_nft.address, {"from": deployer}
    )
    tx5.wait(1)

    marketplace_contract = Contract.from_abi(
        "NftMarketPlace", market_place_factory.marketplaces(0), NftMarketPlace.abi
    )

    # Mint NFT
    tx6 = nft_factory.createCollectibleAndApproveMarket(
        donaty_nft.address,
        deployer.address,
        "http://ipfs.com",
        marketplace_contract.address,
        {"from": deployer},
    )
    tx6.wait(1)

    # List NFT
    tx7 = marketplace_contract.listItem(
        donaty_nft.address, 0, PRICE, {"from": deployer}
    )
    tx7.wait(1)

    # listed_items = marketplace_contract.getListing(donaty_nft.address, 0)
    # print(listed_items)

    tx8 = marketplace_contract.buyItem(
        donaty_nft.address, 0, {"from": account2, "value": PRICE}
    )
    tx8.wait(1)

    balance_of_contract = marketplace_contract.getBalance()
    print(
        f"The balance of the contract is {Web3.fromWei(balance_of_contract, 'ether')}"
    )

    print(f"balance of deployer is {Web3.fromWei(deployer.balance(), 'ether')}")
    # tx9 = donaty_nft.approve(marketplace_contract.address, TOKEN_ID, {"from": account2})
    # tx9.wait(1)

    # tx10 = marketplace_contract.listItem(
    #     donaty_nft.address, 0, PRICE, {"from": account2}
    # )
    # tx10.wait(1)


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
