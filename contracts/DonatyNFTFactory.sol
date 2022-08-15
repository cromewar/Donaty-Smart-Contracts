//SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "./DonatyNFT.sol";

contract DonatyNFTFactory {
    //events
    event newNFTContractCreated(
        address indexed _nftArtist,
        address indexed contractAddress
    );

    // Array for contracts.

    DonatyNFT[] public nftContracts;

    // counter
    uint256 private contracts = 0;

    function createNFTContract(string memory _nftName, string memory _tokenName)
        public
    {
        DonatyNFT newNFTContract = new DonatyNFT(_nftName, _tokenName);
        nftContracts.push(newNFTContract);
        contracts = contracts + 1;
        emit newNFTContractCreated(msg.sender, address(newNFTContract));
    }

    function getNFTContract(uint256 _index) public view returns (address) {
        return address(nftContracts[_index]);
    }
}
