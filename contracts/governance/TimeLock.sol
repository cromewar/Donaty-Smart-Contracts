// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/governance/TimelockController.sol";

contract TimeLock is TimelockController {
    constructor(
        uint256 _minDelay,
        address[] memory _proposers,
        address[] memory _executors
    ) TimelockController(_minDelay, _proposers, _executors) {}

    function grantRoleByArray(bytes32[] memory role, address account)
        public
        virtual
        onlyRole(getRoleAdmin(role[0]))
        onlyRole(getRoleAdmin(role[1]))
        onlyRole(getRoleAdmin(role[2]))
    {
        for (uint256 i = 0; i < role.length; i++) {
            _grantRole(role[i], account);
        }
    }
}
