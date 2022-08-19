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

    event roleGranted(bool success, address nftContract);

    mapping(address => uint256) public timelockIndex;

    function createNewTimeLock(
        uint256 _minDelay,
        address[] memory _proposers,
        address[] memory _executors,
        address _nftContract
    ) public {
        TimeLock timeLock = new TimeLock(_minDelay, _proposers, _executors);

        timeLocks.push(timeLock);
        timelockIndex[address(timeLock)] = timeLocks.length - 1;
        giveAdminControl(timeLock);

        emit newTimeLockCreated(address(timeLock), _nftContract);
    }

    function giveAdminControl(TimeLock _timeLock) internal {
        TimeLock timeLock = _timeLock;
        timeLock.grantRole(TIMELOCK_ADMIN_ROLE, msg.sender);
    }

    function getTimeLock(uint256 _index) public view returns (address) {
        return address(timeLocks[_index]);
    }

    function addRole(
        bytes32[] memory role,
        address account,
        address timelock,
        address nftContract
    ) public {
        uint256 timeLockIndex = timelockIndex[timelock];
        timeLocks[timeLockIndex].grantRoleByArray(role, account);
        emit roleGranted(true, nftContract);
    }

    // 1 address
    // 2 busco por el mapping
    // 3 timeLocks
}
