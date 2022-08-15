//SPDX-License-Idenfier: MIT

pragma solidity ^0.8.0;

import "./governance/TimeLock.sol";

contract TimeLockFactory {
    TimeLock[] public timeLocks;

    event newTimeLockCreated(address indexed _timeLockAddress);

    function createNewTimeLock(
        uint256 _minDelay,
        address[] memory _proposers,
        address[] memory _executors
    ) public {
        TimeLock timeLock = new TimeLock(_minDelay, _proposers, _executors);

        timeLocks.push(timeLock);

        emit newTimeLockCreated(address(timeLock));
    }

    function getTimeLock(uint256 _index) public view returns (address) {
        return address(timeLocks[_index]);
    }
}
