from brownie import (
    DonatyGovernanceFactory,
    DonatyNFTFactory,
    TimeLockFactory,
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
    time_lock_factory = TimeLockFactory.deploy({"from": account})
    print(f"timelock contract {time_lock_factory.address}")
    # Deploy NFT factory
    nft_factory = DonatyNFTFactory.deploy({"from": account})
    print(f"nft factory {nft_factory.address}")

    # Deploy Governance factory
    governance_factory = DonatyGovernanceFactory.deploy({"from": account})
    print(f"governance token {governance_factory.address}")
    # Deploy Time lock
    tx = time_lock_factory.createNewTimeLock(
        2, ZERO_ADDRESS, ZERO_ADDRESS, {"from": account}
    )
    tx.wait(1)
    time_lock_address = time_lock_factory.getTimeLock(0)
    print(f"time lock contract {time_lock_address}")

    time_lock_contract = Contract.from_abi("TimeLock", time_lock_address, TimeLock.abi)
    # get Nft Contract
    tx1 = nft_factory.createNFTContract("Donaty", "DON", {"from": account})
    tx1.wait(1)
    nft_address = nft_factory.getNFTContract(0)
    print(f"nft address {nft_address}")
    nft_contract = Contract.from_abi("DonatyNFT", nft_address, DonatyNFT.abi)

    time_lock_executer_role = time_lock_contract.EXECUTOR_ROLE()
    time_lock_proposer_role = time_lock_contract.PROPOSER_ROLE()
    timelock_canceller_role = time_lock_contract.CANCELLER_ROLE()

    # Grant timeLock Roles to governor contract
    tx1 = time_lock_contract.grantRole(
        time_lock_executer_role, governance_factory.address, {"from": account}
    )
    tx1.wait(1)
    tx2 = time_lock_contract.grantRole(
        time_lock_proposer_role, governance_factory.address, {"from": account}
    )
    tx2.wait(1)
    tx3 = time_lock_contract.grantRole(
        timelock_canceller_role, governance_factory.address, {"from": account}
    )
    tx3.wait(1)

    tx4 = governance_factory.createNewDao(
        nft_contract.address, time_lock_contract.address, {"from": account}
    )
    tx4.wait(1)
