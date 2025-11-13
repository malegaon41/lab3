// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract BankAccount {
    // State variable to store the account balance
    uint public balance;

    // Constructor to initialize the account with an initial balance (optional)
    constructor() {
        balance = 0; // Initial balance is set to 0
    }

    // Function to deposit money into the account
    function deposit(uint amount) public {
        require(amount > 0, "Deposit amount must be greater than zero.");
        balance += amount; // Increase the balance by the deposit amount
    }

    // Function to withdraw money from the account
    function withdraw(uint amount) public {
        require(amount > 0, "Withdraw amount must be greater than zero.");
        require(balance >= amount, "Insufficient balance.");
        balance -= amount; // Decrease the balance by the withdrawal amount
    }
}
