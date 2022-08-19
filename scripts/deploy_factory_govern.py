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
    token_factory = DonatyNFT.deploy("Donaty", "DON", {"from": account})
    # Deploy Time Lock
    time_lock_factory = TimeLockFactory.deploy({"from": account})
    tx = time_lock_factory.createNewTimeLock(
        2, ZERO_ADDRESS, ZERO_ADDRESS, account.address, {"from": account}
    )
    tx.wait(1)
    # time_lock_factory.giveAdminControl(0, {"from": account})
    tx2 = donaty_governance_factory.createNewDao(
        token_factory.address,
        time_lock_factory.address,
        account.address,
        {"from": account},
    )
    tx2.wait(1)
    print(f"Dao Deploy to {donaty_governance_factory.getGovernor(0)}")

    governor = Contract.from_abi(
        "DonatyGovernor", donaty_governance_factory.getGovernor(0), DonatyGovernor.abi
    )
    time_lock = Contract.from_abi(
        "TimeLock", time_lock_factory.getTimeLock(0), TimeLock.abi
    )

    # Get Time Lock Roles
    time_lock_executer_role = time_lock.EXECUTOR_ROLE()
    time_lock_proposer_role = time_lock.PROPOSER_ROLE()
    timelock_canceller_role = time_lock.CANCELLER_ROLE()

    # Grant timeLock Roles to governor contract
    tx3 = time_lock.grantRole(
        time_lock_executer_role, governor.address, {"from": account}
    )
    tx3.wait(1)
    tx4 = time_lock.grantRole(
        time_lock_proposer_role, governor.address, {"from": account}
    )
    tx4.wait(1)
    tx5 = time_lock.grantRole(
        timelock_canceller_role, governor.address, {"from": account}
    )
    tx5.wait(1)


def main():
    deploy_governance_factory()
