from abc import ABC, abstractmethod
from transaction import Transaction


class Account(ABC):
    """Base class for all bank account types."""

    def __init__(self, account_number, account_holder, opening_balance=0):
        if opening_balance < 0:
            raise ValueError("Opening balance cannot be negative.")

        self._account_number = str(account_number)
        self._account_holder = account_holder.strip()
        self.__balance = float(opening_balance)  # Encapsulation
        self._transactions = []

        if opening_balance > 0:
            self._record_transaction("OPENING", opening_balance)

    @property
    def account_number(self):
        return self._account_number

    @property
    def account_holder(self):
        return self._account_holder

    @property
    def balance(self):
        return self.__balance

    @property
    @abstractmethod
    def account_type(self):
        pass

    def _record_transaction(self, transaction_type, amount):
        self._transactions.append(
            Transaction.create(transaction_type, amount, self.__balance)
        )

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")

        self.__balance += amount
        self._record_transaction("DEPOSIT", amount)
        return self.__balance

    @abstractmethod
    def withdraw(self, amount):
        """Each account type defines its own withdrawal rules."""
        pass

    def _complete_withdrawal(self, amount):
        self.__balance -= amount
        self._record_transaction("WITHDRAW", amount)
        return self.__balance

    def transaction_history(self):
        return list(self._transactions)

    def display_details(self):
        print("\n------ ACCOUNT DETAILS ------")
        print(f"Account number : {self.account_number}")
        print(f"Account holder : {self.account_holder}")
        print(f"Account type   : {self.account_type}")
        print(f"Balance        : ₹{self.balance:.2f}")


class SavingsAccount(Account):
    """Savings account does not allow the balance to go below zero."""

    @property
    def account_type(self):
        return "Savings"

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        return self._complete_withdrawal(amount)


class CurrentAccount(Account):
    """Current account can use an approved overdraft limit."""

    def __init__(self, account_number, account_holder, opening_balance=0,
                 overdraft_limit=5000):
        if overdraft_limit < 0:
            raise ValueError("Overdraft limit cannot be negative.")
        self.overdraft_limit = float(overdraft_limit)
        super().__init__(account_number, account_holder, opening_balance)

    @property
    def account_type(self):
        return "Current"

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.balance + self.overdraft_limit:
            raise ValueError("Amount exceeds available balance and overdraft limit.")
        return self._complete_withdrawal(amount)
