// SPDX-License-Identifier: MIT
// compiler version must be greater than or equal to 0.8.10 and less than 0.9.0
pragma solidity ^0.8.10;

contract BooleanTest {
    bool public val;

    function getVal() public view returns (bool) {
        return val;
    }

    function setVal(bool _val) public {
        val = _val;
    }

}
