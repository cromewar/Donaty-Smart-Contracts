//SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "./DonatyNFT.sol";

contract DonatyNFTFactory {
    //events
    event newNFTContractCreated(
        address indexed _nftArtist,
        address indexed contractAddress,
        string _title,
        uint256 _goal,
        string indexed _initialDate,
        string _dueDate,
        uint256 _duration,
        uint256 _steps,
        string _ipfsImage
    );

    event newStepAdded(
        string _description,
        string _initialDate,
        string _dueDate,
        address _contractAddress
    );

    // Array for contracts.

    DonatyNFT[] public nftContracts;

    // counter
    uint256 private contracts = 0;

    function createNFTContract(
        string memory _nftName,
        string memory _tokenName,
        uint256 _goal,
        string[] memory _stepsInitialDate,
        string[] memory _stepsDueDate,
        string memory _title,
        string memory _initialDate,
        string memory _dueDate,
        uint256 _duration,
        uint256 _stepDivision,
        string memory _ipfsImage,
        string[] memory _descriptionSteps
    ) public {
        DonatyNFT newNFTContract = new DonatyNFT(_nftName, _tokenName);
        nftContracts.push(newNFTContract);
        contracts = contracts + 1;
        emit newNFTContractCreated(
            msg.sender,
            address(newNFTContract),
            _title,
            _goal,
            _initialDate,
            _dueDate,
            _duration,
            _stepDivision,
            _ipfsImage
        );
        emitEventForStep(
            _descriptionSteps,
            _stepsInitialDate,
            _stepsDueDate,
            address(newNFTContract)
        );
    }

    function getNFTContract(uint256 _index) public view returns (address) {
        return address(nftContracts[_index]);
    }

    function emitEventForStep(
        string[] memory _steps,
        string[] memory _initialDate,
        string[] memory _dueDate,
        address _contractAddress
    ) internal {
        for (uint256 i = 0; i < _steps.length; i++) {
            emit newStepAdded(
                _steps[i],
                _initialDate[i],
                _dueDate[i],
                _contractAddress
            );
        }
    }
}
