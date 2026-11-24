
```mermaid
classDiagram

    class Bank {
        +name
        -accounts
        -next_account_number
        +create_account()
        +get_account()
        +deposit()
        +withdraw()
        +list_accounts()
    }

    class Account {
        <<abstract>>
        -account_number
        -account_holder
        -balance
        +deposit()
        +withdraw()
        +transaction_history()
        +display_details()
    }

    class SavingsAccount {
        +account_type
        +withdraw()
    }

    class CurrentAccount {
        +overdraft_limit
        +account_type
        +withdraw()
    }

    class Transaction {
        +transaction_type
        +amount
        +balance_after
        +date
        +create()
    }

    Account <|-- SavingsAccount
    Account <|-- CurrentAccount
    Bank o-- Account
    Account *-- Transaction
    ```
