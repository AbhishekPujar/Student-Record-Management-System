from account import SavingsAccount, CurrentAccount


class Bank:
    def __init__(self, name="JanMitra Bank"):
        self.name = name
        self._accounts = {}
        self._next_account_number = 1001

    def create_account(self, holder, account_type, opening_balance=0,
                       overdraft_limit=5000):
        if not holder.strip():
            raise ValueError("Account holder name cannot be empty.")

        account_number = str(self._next_account_number)
        self._next_account_number += 1

        account_type = account_type.lower()
        if account_type == "savings":
            account = SavingsAccount(account_number, holder, opening_balance)
        elif account_type == "current":
            account = CurrentAccount(
                account_number, holder, opening_balance, overdraft_limit
            )
        else:
            raise ValueError("Choose either Savings or Current account.")

        self._accounts[account_number] = account
        return account

    def get_account(self, account_number):
        account = self._accounts.get(str(account_number))
        if account is None:
            raise ValueError("Account not found.")
        return account

    def list_accounts(self):
        return list(self._accounts.values())

    def deposit(self, account_number, amount):
        return self.get_account(account_number).deposit(amount)

    def withdraw(self, account_number, amount):
        return self.get_account(account_number).withdraw(amount)

    def show_transactions(self, account_number):
        return self.get_account(account_number).transaction_history()
