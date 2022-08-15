from webbrowser import get
from brownie import DonatyNFT, DonatyGovernanceFactory
from scripts.helpful_scripts import get_account


def deploy_governance_factory():
    account = get_account()
    # Deploy Governor
    donaty_governance_factory = DonatyGovernanceFactory.deploy({"from": account})


def main():
    deploy_governance_factory()
