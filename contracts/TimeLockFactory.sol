//SPDX-License-Idenfier: MIT

pragma solidity ^0.8.0;

import "./governance/TimeLock.sol";

contract TimeLockFactory {
    TimeLock[] public timeLocks;
    bytes32 public constant TIMELOCK_ADMIN_ROLE =
        keccak256("TIMELOCK_ADMIN_ROLE");

    event newTimeLockCreated(
        address indexed timelockAddress,
        address nftContract
    );

    function createNewTimeLock(
        uint256 _minDelay,
        address[] memory _proposers,
        address[] memory _executors,
        address _nftContract
    ) public {
        TimeLock timeLock = new TimeLock(_minDelay, _proposers, _executors);

        timeLocks.push(timeLock);

        emit newTimeLockCreated(address(timeLock), _nftContract);
    }

    function giveAdminControl(uint256 _timeLock) public {
        TimeLock timeLock = timeLocks[_timeLock];
        timeLock.grantRole(TIMELOCK_ADMIN_ROLE, msg.sender);
    }

    function getTimeLock(uint256 _index) public view returns (address) {
        return address(timeLocks[_index]);
    }
}
