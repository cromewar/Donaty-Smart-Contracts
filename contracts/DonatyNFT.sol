// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract DonatyNFT is ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;

    event newNFTMinted(address owner, uint256 id, string tokenUri);

    constructor(string memory _nftName, string memory _tokenName)
        ERC721(_nftName, _tokenName)
    {}

    function createCollectible(string memory tokenURI)
        public
        onlyOwner
        returns (uint256)
    {
        address owner = address(this);
        uint256 newItemId = _tokenIds.current();
        _mint(owner, newItemId);
        _setTokenURI(newItemId, tokenURI);
        _tokenIds.increment();

        emit newNFTMinted(owner, newItemId, tokenURI);

        return newItemId;
    }
}
