from brownie import TimeLockFactory
from scripts.helpful_scripts import get_account

ZERO_ADDRESS = ["0x0000000000000000000000000000000000000000"]
time_delay = 2


def deploy_time_lock_factory():
    account = get_account()
    # Deploy Time Lock
    time_lock_factory = TimeLockFactory.deploy({"from": account})
    # tx = time_lock_factory.createNewTimeLock(
    #     time_delay, ZERO_ADDRESS, ZERO_ADDRESS, {"from": account}
    # )
    # tx.wait(1)
    # print(f"TimeLock Factory Deploy to {time_lock_factory.getTimeLock(0)}")


def main():
    deploy_time_lock_factory()
