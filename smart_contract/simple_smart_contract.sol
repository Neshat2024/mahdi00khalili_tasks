// SPDX-License-Identifier: MIT
pragma solidity >=0.4.16 <0.9.0;

contract SimpleStorage {
    uint storedData;

    event GetEvent(uint data);
    event SetEvent(string message);

    function set(uint x) public {
        emit SetEvent("changed the x data");
        storedData = x;
    }

    function get() public {
        emit GetEvent(storedData);

    }
}
