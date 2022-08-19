//SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "./NftMarketPlace.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NFTMarketPlaceFactory is Ownable {
    NftMarketPlace[] public marketplaces;

    // events
    event NewMarketPlaceCreated(
        address indexed marketplaceAddress,
        address nftContract
    );

    function createNewMarketPlace(address _ownerDao, address nftContract)
        public
    {
        require(_ownerDao != address(0));
        NftMarketPlace newMarketPlace = new NftMarketPlace();
        giveControlToDao(_ownerDao, newMarketPlace);
        marketplaces.push(newMarketPlace);
        emit NewMarketPlaceCreated(address(newMarketPlace), nftContract);
    }

    function giveControlToDao(address _dao, NftMarketPlace _market) internal {
        _market.transferOwnership(_dao);
    }
}
