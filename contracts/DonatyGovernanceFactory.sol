//SPDX-License-Identifier: MIT

import "./governance/DonatyGovernor.sol";
import "@openzeppelin/contracts/governance/extensions/GovernorTimelockControl.sol";

pragma solidity ^0.8.0;

contract DonatyGovernanceFactory {
    DonatyGovernor[] public governors;

    //events
    event NewGovernorCreated(address indexed daoAddress, address nftContract);

    function createNewDao(
        IVotes _token,
        TimelockController _timelock,
        address nftContract
    ) public {
        DonatyGovernor newGovernor = new DonatyGovernor(_token, _timelock);
        governors.push(newGovernor);
        emit NewGovernorCreated(address(newGovernor), nftContract);
    }

    function getGovernor(uint256 _index) public view returns (address) {
        return address(governors[_index]);
    }
}
