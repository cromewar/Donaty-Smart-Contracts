from brownie import DonatyGovernanceFactory, NFTMarketPlaceFactory, TimeLockFactory
from scripts.helpful_scripts import get_account


def deploy_all_factories():
    account = get_account()
    time_lock_factory = TimeLockFactory.deploy({"from": account})
    print(f"TimeLock Factory Deploy to {time_lock_factory.address}")
    donaty_governance_factory = DonatyGovernanceFactory.deploy({"from": account})
    print(f"Governance Factory Deploy to {donaty_governance_factory.address}")
    marketplace_factory = NFTMarketPlaceFactory.deploy({"from": account})
    print(f"NFT Market place factory deployed at {marketplace_factory.address}")


def main():
    deploy_all_factories()
