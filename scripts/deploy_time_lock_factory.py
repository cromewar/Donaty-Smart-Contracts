from brownie import TimeLockFactory, TimeLock, Contract, DonatyGovernor, DonatyNFT
from scripts.helpful_scripts import get_account

ZERO_ADDRESS = ["0x0000000000000000000000000000000000000000"]
time_delay = 2


def deploy_time_lock_factory():
    account = get_account()
    # Deploy Time Lock
    time_lock_factory = TimeLockFactory.deploy({"from": account})
    print(f"TimeLock Factory Deploy to {time_lock_factory.address}")
    # Deploy Governor
    # token_factory = DonatyNFT.deploy("Donaty", "DON", {"from": account})

    # tx = time_lock_factory.createNewTimeLock(
    #     time_delay, ZERO_ADDRESS, ZERO_ADDRESS, token_factory.address, {"from": account}
    # )
    # tx.wait(1)
    # print(f"TimeLock Factory Deploy to {time_lock_factory.getTimeLock(0)}")
    # time_lock = Contract.from_abi(
    #     "TimeLock", time_lock_factory.getTimeLock(0), TimeLock.abi
    # )

    # donaty_governor = DonatyGovernor.deploy(
    #     token_factory.address, time_lock_factory.address, {"from": account}
    # )

    # time_lock_executer_role = time_lock.EXECUTOR_ROLE()
    # time_lock_proposer_role = time_lock.PROPOSER_ROLE()
    # timelock_canceller_role = time_lock.CANCELLER_ROLE()
    # roles = [time_lock_executer_role, time_lock_proposer_role, timelock_canceller_role]

    # tx = time_lock_factory.addRole(
    #     roles,
    #     donaty_governor.address,
    #     time_lock.address,
    #     token_factory.address,
    #     {"from": account},
    # )
    # bytes32[] memory role,
    #     address account,
    #     address timelock,
    #     address nftContract
    # tx.wait(1)


def main():
    deploy_time_lock_factory()
