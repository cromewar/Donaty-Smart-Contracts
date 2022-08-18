//SPDX-License-Identifier: MIT

import "./governance/DonatyGovernor.sol";
import "@openzeppelin/contracts/governance/extensions/GovernorTimelockControl.sol";

pragma solidity ^0.8.0;

contract DonatyGovernanceFactory {
    DonatyGovernor[] public governors;

    function createNewDao(IVotes _token, TimelockController _timelock) public {
        DonatyGovernor newGovernor = new DonatyGovernor(_token, _timelock);
        governors.push(newGovernor);
    }

    function getGovernor(uint256 _index) public view returns (address) {
        return address(governors[_index]);
    }
}

//  function grantRole(bytes32 role, address account) public virtual override onlyRole(getRoleAdmin(role)) {
//         _grantRole(role, account);
//     }

// bytes32 public constant TIMELOCK_ADMIN_ROLE = keccak256("TIMELOCK_ADMIN_ROLE");
//     bytes32 public constant PROPOSER_ROLE = keccak256("PROPOSER_ROLE");
//     bytes32 public constant EXECUTOR_ROLE = keccak256("EXECUTOR_ROLE");
//     bytes32 public constant CANCELLER_ROLE = keccak256("CANCELLER_ROLE");
