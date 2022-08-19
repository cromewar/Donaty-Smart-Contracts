// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/draft-ERC721Votes.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract DonatyNFT is ERC721Votes, ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;

    event newNFTMinted(address owner, uint256 id, string tokenUri);

    constructor(string memory _nftName, string memory _tokenName)
        ERC721(_nftName, _tokenName)
        EIP712(_nftName, "1")
    {}

    function createCollectible(address owner, string memory _tokenURI)
        public
        returns (uint256)
    {
        uint256 newItemId = _tokenIds.current();
        _mint(owner, newItemId);
        _setTokenURI(newItemId, _tokenURI);
        _tokenIds.increment();

        emit newNFTMinted(owner, newItemId, _tokenURI);

        return newItemId;
    }

    // Create and approve a new collectible.
    function createAndApproveCollectible(
        address owner,
        string memory _tokenURI,
        address nftMarketPlace
    ) public returns (uint256) {
        uint256 newItemId = _tokenIds.current();
        _mint(owner, newItemId);
        _setTokenURI(newItemId, _tokenURI);
        _tokenIds.increment();
        _approve(nftMarketPlace, newItemId);
        return newItemId;
    }

    // Sending the Voting power to the new Owner

    function _afterTokenTransfer(
        address from,
        address to,
        uint256 tokenId
    ) internal override(ERC721, ERC721Votes) {
        super._beforeTokenTransfer(from, to, tokenId);
    }

    // Just some Overrides to make the compiler happy :3

    function _burn(uint256 tokenId)
        internal
        override(ERC721, ERC721URIStorage)
    {
        super._burn(tokenId);
    }

    function tokenURI(uint256 tokenId)
        public
        view
        override(ERC721, ERC721URIStorage)
        returns (string memory)
    {
        return super.tokenURI(tokenId);
    }

    function _getVotingUnits(address account)
        internal
        view
        virtual
        override
        returns (uint256)
    {
        return balanceOf(account);
    }
}
