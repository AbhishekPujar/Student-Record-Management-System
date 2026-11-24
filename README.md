# Python Banking Management System

## 1. Project Description

A beginner-friendly command-line banking application built using Python and Object-Oriented Programming (OOP).

This application allows users to create bank accounts, deposit money, withdraw money, check account balances and view transaction history.

## 2. Project Objectives

- Understand Object-Oriented Programming.
- Implement classes and objects.
- Apply the four major OOP concepts.
- Develop a simple banking application.
- Practise Python programming and error handling.

## 3. Features

- Create Savings and Current accounts.
- Deposit money.
- Withdraw money.
- Check account details and balance.
- View transaction history.
- View all bank accounts.
- Input validation and error messages.

## 4. OOP Concepts Used

- **Classes and Objects:** Account, SavingsAccount, CurrentAccount, Bank and Transaction.
- **Constructor:** `__init__()` initializes objects.
- **Methods:** `deposit()`, `withdraw()`, `display_details()`.
- **Encapsulation:** Account balance is stored in a private attribute.
- **Inheritance:** SavingsAccount and CurrentAccount inherit from Account.
- **Polymorphism:** Each account type implements its own withdrawal method.
- **Abstraction:** Account is an abstract base class.

## 5. Technologies Used

- Python 3
- Visual Studio Code
- Object-Oriented Programming

## 6. Project Folder Structure

```text
Python_Internship_Module_03/
│
├── account.py
├── bank.py
├── transaction.py
├── main.py
├── class_diagram.md
└── README.md
```

## 7. Requirements

- Python 3.10 or later.
- No external packages required.

## 8. How to Run the Project

1. Open the project folder in Visual Studio Code.
2. Open Terminal → New Terminal.
3. Run the following command:

```bash
python3 main.py
```

4. Follow the menu displayed in the terminal.

## 9. UML Class Diagram

The UML class diagram is available in `class_diagram.md`.

It describes the Bank, Account, SavingsAccount, CurrentAccount and Transaction classes and their relationships.

## 10. Important Note

This is an educational demonstration. Account data is stored in memory and is cleared when the program exits. It is not connected to a real bank and must not be used for real financial transactions.

## 11. Author

Python Internship – Module 03 Project.
