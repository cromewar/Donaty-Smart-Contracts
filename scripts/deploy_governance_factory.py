from brownie import (
    DonatyNFT,
    DonatyGovernanceFactory,
    TimeLockFactory,
    Contract,
    TimeLock,
    DonatyGovernor,
)
from scripts.helpful_scripts import get_account

ZERO_ADDRESS = ["0x0000000000000000000000000000000000000000"]
time_delay = 2


def deploy_governance_factory():
    account = get_account()
    # Deploy Governor
    donaty_governance_factory = DonatyGovernanceFactory.deploy({"from": account})
    print(f"Governance Factory Deploy to {donaty_governance_factory.address}")


def main():
    deploy_governance_factory()
