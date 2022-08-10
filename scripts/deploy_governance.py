from brownie import DonatyNFT, DonatyGovernor, TimeLock
from scripts.helpful_scripts import get_account


ZERO_ADDRESS = ["0x0000000000000000000000000000000000000000"]
time_delay = 2


def deploy_governance():
    account = get_account()
    # Deploy NFT Contract
    token_factory = DonatyNFT.deploy("Donaty", "DON", {"from": account})
    # Deploy Time Lock
    time_lock_factory = TimeLock.deploy(
        2, ZERO_ADDRESS, ZERO_ADDRESS, {"from": account}
    )
    # Deploy Governor
    donaty_governor = DonatyGovernor.deploy(
        token_factory.address, time_lock_factory.address, {"from": account}
    )

    # Get Time Lock Roles
    time_lock_executer_role = time_lock_factory.EXECUTOR_ROLE()
    time_lock_proposer_role = time_lock_factory.PROPOSER_ROLE()
    timelock_canceller_role = time_lock_factory.CANCELLER_ROLE()

    # Grant timeLock Roles to governor contract
    tx1 = time_lock_factory.grantRole(
        time_lock_executer_role, donaty_governor.address, {"from": account}
    )
    tx1.wait(1)
    tx2 = time_lock_factory.grantRole(
        time_lock_proposer_role, donaty_governor.address, {"from": account}
    )
    tx2.wait(1)
    tx3 = time_lock_factory.grantRole(
        timelock_canceller_role, donaty_governor.address, {"from": account}
    )
    tx3.wait(1)

    print(f"Dao Deploy to {donaty_governor.address}")
    print(f"TimeLock Deploy to {time_lock_factory.address}")
    print(f"NFt Contract Deploy to {token_factory.address}")


def main():
    deploy_governance()
