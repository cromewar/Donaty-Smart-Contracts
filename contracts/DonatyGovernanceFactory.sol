//SPDX-License-Idenfier: MIt

pragma solidity ^0.8.0;

import "./governance/DonatyGovernor.sol";
import "./governance/TimeLock.sol";

contract DonatyGovernanceFactory {
    // Daos Array
    DonatyGovernor[] public donatyDaos;

    event newDaoCreated(
        address indexed _daoAddress,
        address indexed _timeLockAddress
    );

    // Functions
    function createNewDao(IVotes _token, TimelockController _timeLock) public {
        DonatyGovernor dao = new DonatyGovernor(_token, _timeLock);

        bytes32 timeLockExecuterRole = _timeLock.EXECUTOR_ROLE();
        bytes32 timeLockProposerRole = _timeLock.PROPOSER_ROLE();
        bytes32 timeLockCancellerRole = _timeLock.CANCELLER_ROLE();

        _timeLock.grantRole(timeLockExecuterRole, address(dao));
        _timeLock.grantRole(timeLockProposerRole, address(dao));
        _timeLock.grantRole(timeLockCancellerRole, address(dao));

        // add Dao to the list
        donatyDaos.push(dao);

        // event emission

        emit newDaoCreated(address(dao), address(_timeLock));
    }

    function getDaoAddress(uint256 _index) public view returns (address) {
        return address(donatyDaos[_index]);
    }
}
