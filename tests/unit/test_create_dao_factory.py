from brownie import (
    DonatyGovernanceFactory,
    TimeLock,
    Contract,
    DonatyNFT,
)
from scripts.deploy_governance import ZERO_ADDRESS
from scripts.helpful_scripts import get_account

ZERO_ADDRESS = ["0x0000000000000000000000000000000000000000"]


def test_can_deploy_and_create_dao():
    account = get_account()
    # Deploy Time lock factory
    token_factory = DonatyNFT.deploy("Donaty", "DON", {"from": account})
    # Deploy Time Lock
    time_lock_factory = TimeLock.deploy(
        2, ZERO_ADDRESS, ZERO_ADDRESS, {"from": account}
    )
    token_factory = DonatyNFT.deploy("Donaty", "DON", {"from": account})

    # Deploy Governance factory
    governance_factory = DonatyGovernanceFactory.deploy({"from": account})
    print(f"governance token {governance_factory.address}")
    # Deploy Time lock
    tx = governance_factory.createNewDao(
        token_factory.address,
        time_lock_factory.address,
        token_factory.address,
        120960,
        483840,
        {"from": account},
    )
    tx.wait(1)

    # IVotes _token,
    # TimelockController _timelock,
    # address nftContract,
    # uint256 initVotingPeriod,
    # uint256 proposalThreshhold

    # Get Time Lock Roles
    time_lock_executer_role = time_lock_factory.EXECUTOR_ROLE()
    time_lock_proposer_role = time_lock_factory.PROPOSER_ROLE()
    timelock_canceller_role = time_lock_factory.CANCELLER_ROLE()

    # Grant timeLock Roles to governor

    # donaty_governor = Contract.from_address(governance_factory.getDaoAddress(0))

    # tx1 = time_lock_factory.grantRole(
    #     time_lock_executer_role, donaty_governor.address, {"from": account}
    # )
    # tx1.wait(1)
    # tx2 = time_lock_factory.grantRole(
    #     time_lock_proposer_role, donaty_governor.address, {"from": account}
    # )
    # tx2.wait(1)
    # tx3 = time_lock_factory.grantRole(
    #     timelock_canceller_role, donaty_governor.address, {"from": account}
    # )
    # tx3.wait(1)
