//SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "./DonatyNFT.sol";

contract DonatyNFTFactory {
    //events
    event newNFTContractCreated(
        address indexed nftArtist,
        address indexed contractAddress,
        string title,
        uint256 goal,
        string initialDate,
        string dueDate,
        uint256 duration,
        uint256 steps,
        string ipfsImage
    );

    event newStepAdded(
        string description,
        string initialDate,
        string dueDate,
        address contractAddress
    );

    event newNFTMintedAndApproved(
        address owner,
        uint256 id,
        string tokenUri,
        address nftContract
    );

    // Array for contracts.

    DonatyNFT[] public nftContracts;

    // counter
    uint256 private contracts = 0;

    mapping(address => uint256) private nftContractsIndex;

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

        nftContractsIndex[address(newNFTContract)] = nftContracts.length - 1;
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

    function createCollectibleAndApproveMarket(
        address nftContract,
        address owner,
        string memory _tokenURI,
        address nftMarketPlace
    ) public {
        uint256 nftContractIndex = nftContractsIndex[nftContract];
        uint256 nftId = nftContracts[nftContractIndex]
            .createAndApproveCollectible(owner, _tokenURI, nftMarketPlace);
        emit newNFTMintedAndApproved(owner, nftId, _tokenURI, nftContract);
    }

    // 1 address
    // 2 busco por el mapping
    // 3 nftContracts
}
