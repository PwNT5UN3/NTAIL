// contracts/NineTailsToken.sol
// SPDX-License-Identifier: GNU General Public License v3.0 
pragma solidity ^0.8.0;

import "openzeppelin/contracts/token/ERC20/ERC20.sol";

contract NineTailsToken is ERC20 {
    constructor(uint256 initialSupply) ERC20("NineTailsToken", "NTAIL") {
        _mint(msg.sender, initialSupply);
    }
}