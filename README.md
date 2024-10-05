# Bank Management System

This **Bank Management System** is a console application written in Python that allows users to manage bank accounts. Users can perform various operations such as adding accounts, depositing money, withdrawing money, transferring money, and viewing account details.

## Features

- **Add Account:** Create a new bank account using the account holder's name and details.
- **Deposit Money:** Add funds to an existing account.
- **Withdraw Money:** Withdraw funds from an account, with a detailed breakdown of how the money will be returned.
- **Transfer Money:** Transfer funds from one account to another and view updated account details after the transaction.
- **View Account Details:** Display account information, including balance and account number.

## Usage

1. **Add Account:**
   - Users can choose to add a new account by providing their name, CNIC, initial balance, and account number.
  
2. **Deposit Money:**
   - Users can deposit money into their accounts by entering their name and the amount they wish to deposit. The system updates the balance accordingly.

3. **Withdraw Money:**
   - Users can withdraw money by entering their name and the desired amount. The system provides the amount in denominations, showing how the user will receive the cash.

4. **Transfer Money:**
   - Users can transfer money to another account by providing their name, the recipient's name, and the amount to be transferred. The system adjusts both accounts' balances accordingly.

5. **Show Details:**
   - After transferring money, users can view the updated details of both the sender and recipient accounts.

## How to Run the Code

1. Ensure you have Python installed on your machine.
2. Copy the code into a Python file (e.g., `bank_management_system.py`).
3. Run the file using a Python interpreter: 
   ```bash
   python bank_management_system.py
