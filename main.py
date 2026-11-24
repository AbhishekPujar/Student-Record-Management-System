from bank import Bank


def read_amount(prompt):
    try:
        amount = float(input(prompt))
        if amount <= 0:
            print("Please enter an amount greater than zero.")
            return None
        return amount
    except ValueError:
        print("Please enter a valid number.")
        return None


def show_menu():
    print("\n========== PYTHON BANKING SYSTEM ==========")
    print("1. Create account")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Check account details")
    print("5. View transaction history")
    print("6. View all accounts")
    print("7. Exit")
    print("============================================")


def main():
    bank = Bank()

    print(f"Welcome to {bank.name}!")

    while True:
        show_menu()
        choice = input("Enter your choice (1-7): ").strip()

        try:
            if choice == "1":
                holder = input("Enter account holder name: ").strip()
                account_type = input(
                    "Enter account type (Savings/Current): "
                ).strip()
                opening_balance = float(input("Enter opening balance: ₹"))

                overdraft_limit = 5000
                if account_type.lower() == "current":
                    overdraft_limit = float(
                        input("Enter overdraft limit (₹, default 5000): ") or 5000
                    )

                account = bank.create_account(
                    holder, account_type, opening_balance, overdraft_limit
                )
                print("\nAccount created successfully!")
                print(f"Your account number is: {account.account_number}")
                account.display_details()

            elif choice == "2":
                number = input("Enter account number: ").strip()
                amount = read_amount("Enter deposit amount: ₹")
                if amount is not None:
                    balance = bank.deposit(number, amount)
                    print(f"Deposit successful. New balance: ₹{balance:.2f}")

            elif choice == "3":
                number = input("Enter account number: ").strip()
                amount = read_amount("Enter withdrawal amount: ₹")
                if amount is not None:
                    balance = bank.withdraw(number, amount)
                    print(f"Withdrawal successful. New balance: ₹{balance:.2f}")

            elif choice == "4":
                number = input("Enter account number: ").strip()
                bank.get_account(number).display_details()

            elif choice == "5":
                number = input("Enter account number: ").strip()
                transactions = bank.show_transactions(number)
                print("\n------ TRANSACTION HISTORY ------")
                if not transactions:
                    print("No transactions found.")
                else:
                    for transaction in transactions:
                        print(transaction)

            elif choice == "6":
                accounts = bank.list_accounts()
                print("\n------ ALL BANK ACCOUNTS ------")
                if not accounts:
                    print("No accounts have been created yet.")
                else:
                    for account in accounts:
                        print(
                            f"{account.account_number} | "
                            f"{account.account_holder} | "
                            f"{account.account_type} | "
                            f"₹{account.balance:.2f}"
                        )

            elif choice == "7":
                print("Thank you for using the Python Banking System. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number from 1 to 7.")

        except ValueError as error:
            print(f"Error: {error}")
        except Exception as error:
            print(f"Something went wrong: {error}")


if __name__ == "__main__":
    main()
