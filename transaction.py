from dataclasses import dataclass
from datetime import datetime


@dataclass
class Transaction:
    transaction_type: str
    amount: float
    balance_after: float
    date: str

    @classmethod
    def create(cls, transaction_type, amount, balance_after):
        return cls(
            transaction_type=transaction_type,
            amount=amount,
            balance_after=balance_after,
            date=datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
        )

    def __str__(self):
        return (
            f"{self.date} | {self.transaction_type:<10} | "
            f"Amount: ₹{self.amount:.2f} | Balance: ₹{self.balance_after:.2f}"
        )
