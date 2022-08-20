//SPDX-License-Identifier: MIT

import "./governance/DonatyGovernor.sol";
import "@openzeppelin/contracts/governance/extensions/GovernorTimelockControl.sol";

pragma solidity ^0.8.0;

contract DonatyGovernanceFactory {
    DonatyGovernor[] public governors;

    mapping(address => uint256) public governorIndex;

    //events
    event NewGovernorCreated(address indexed daoAddress, address nftContract);
    event newProposalCreated(address nftAddress, uint256 proposalId);

    function createNewDao(
        IVotes _token,
        TimelockController _timelock,
        address nftContract,
        uint256 initVotingDelay,
        uint256 initVotingPeriod,
        uint256 proposalThreshhold
    ) public {
        DonatyGovernor newGovernor = new DonatyGovernor(
            _token,
            _timelock,
            initVotingDelay,
            initVotingPeriod,
            proposalThreshhold
        );
        governors.push(newGovernor);
        governorIndex[address(newGovernor)] = governors.length - 1;

        emit NewGovernorCreated(address(newGovernor), nftContract);
    }

    function getGovernor(uint256 _index) public view returns (address) {
        return address(governors[_index]);
    }

    function proposeVotation(
        address[] memory targets,
        uint256[] memory values,
        bytes[] memory calldatas,
        string memory description,
        address nftAddress,
        address daoAddress
    ) public {
        uint256 governor = governorIndex[daoAddress];
        uint256 proposeId = governors[governor].propose(
            targets,
            values,
            calldatas,
            description
        );
        emit newProposalCreated(nftAddress, proposeId);
    }
}
