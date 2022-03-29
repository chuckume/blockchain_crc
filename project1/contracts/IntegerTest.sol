// SPDX-License-Identifier: MIT
// compiler version must be greater than or equal to 0.8.10 and less than 0.9.0
pragma solidity ^0.8.10;

contract IntegerTest {
    uint public val;

    function getVal() public view returns (uint) {
        return val;
    }

    function setVal(uint _val) public {
        val = _val;
    }

}

contract SignedIntegerTest {
    int public val;

    function getVal() public view returns (int) {
        return val;
    }

    function setVal(int _val) public {
        val = _val;
    }

}