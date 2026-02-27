from abc import ABC, abstractmethod


class BankAccount(ABC):
    """
    Abstract base class representing a generic bank account.

    This class demonstrates:
    - Abstraction: It defines what all bank accounts must be able to do,
        without specifying the exact behavior.
    """

    def __init__(self, owner, balance=0.0):
        """
        Create a new bank account.

        Args:
            owner (str): Name of the account owner.
            balance (float): Initial balance of the account.
        """
        self.owner = owner
        self.balance = balance

    def get_owner(self):
        """
        Return the name of the account owner.

        Returns:
            str: Account owner's name.
        """
        return self.owner

    def get_balance(self):
        """
        Return the current balance of the account.

        Returns:
            float: Current account balance.
        """
        return self.balance

    def deposit(self, amount):
        """
        Deposit money into the account.

        Args:
            amount (float): Amount of money to deposit.

        Raises:
            ValueError: If the deposit amount is not positive.
        """
        if amount <= 0:
            raise ValueError("Deposit must be positive.")
        self.balance += amount
        print(f"{amount} deposited into {self.owner}'s account.")

    @abstractmethod
    def withdraw(self, amount):
        """
        Withdraw money from the account.

        This method is abstract and must be implemented
        by all subclasses, because different account types
        have different withdrawal rules.

        Args:
            amount (float): Amount of money to withdraw.
        """
        pass

    @abstractmethod
    def monthly_update(self):
        """
        Apply monthly account updates.

        Examples include:
        - charging fees
        - adding interest

        Each account type defines its own monthly behavior.
        """
        pass


class CheckingAccount(BankAccount):
    """
    Concrete bank account representing a checking account.

    Demonstrates inheritance:
    - CheckingAccount IS A BankAccount
    - Inherits deposit(), get_balance(), get_owner()
    - Overrides withdraw() and monthly_update()
    """

    def __init__(self, owner, balance=0.0, overdraft_limit=0.0):
        """
        Create a new checking account.

        Args:
            owner (str): Name of the account owner.
            balance (float): Initial balance.
            overdraft_limit (float): Maximum allowed overdraft.
        """
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        """
        Withdraw money from a checking account.

        Allows overdrawing up to the overdraft limit.

        Args:
            amount (float): Amount to withdraw.

        Raises:
            ValueError: If the withdrawal amount is not positive.
        """
        if amount <= 0:
            raise ValueError("Withdrawal must be positive.")

        if self.balance - amount < -self.overdraft_limit:
            print("Withdrawal denied (overdraft limit reached).")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn from {self.owner}'s checking account.")

    def monthly_update(self):
        """
        Apply monthly maintenance fee to the checking account.
        """
        fee = 2.0
        self.balance -= fee
        print(f"Monthly fee of {fee} charged to {self.owner}'s checking account.")


class SavingsAccount(BankAccount):
    """
    Concrete bank account representing a savings account.

    Demonstrates inheritance and specialization:
    - SavingsAccount IS A BankAccount
    - Does not allow negative balances
    - Earns interest every month
    """

    def __init__(self, owner, balance=0.0, interest_rate=0.01):
        """
        Create a new savings account.

        Args:
            owner (str): Name of the account owner.
            balance (float): Initial balance.
            interest_rate (float): Monthly interest rate.
        """
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        """
        Withdraw money from a savings account.

        Savings accounts cannot have a negative balance.

        Args:
            amount (float): Amount to withdraw.

        Raises:
            ValueError: If the withdrawal amount is not positive.
        """
        if amount <= 0:
            raise ValueError("Withdrawal must be positive.")

        if amount > self.balance:
            print("Savings cannot go below 0.")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn from {self.owner}'s savings account.")

    def monthly_update(self):
        """
        Apply monthly interest to the savings account.
        """
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"{self.owner} earned {interest:.2f} interest.")


def run_monthly_updates(accounts):
    """
    Run monthly updates on a list of bank accounts.

    Demonstrates polymorphism:
    - All accounts are treated the same (BankAccount interface)
    - Each account executes its own version of monthly_update()

    Args:
        accounts (list[BankAccount]): List of bank account objects.
    """
    print("\n--- Running monthly updates for all accounts ---")
    for acc in accounts:
        acc.monthly_update()
        print(f"{acc.get_owner()}'s new balance: {acc.get_balance():.2f}")


if __name__ == "__main__":
    # Create some bank accounts
    checking = CheckingAccount("Alice", balance=100.0, overdraft_limit=50.0)
    savings = SavingsAccount("Bob", balance=200.0, interest_rate=0.02)

    # Perform some transactions
    checking.deposit(50)
    checking.withdraw(180)  # Should be allowed (within overdraft)
    
    savings.withdraw(250)   # Should be denied (insufficient funds)

    # Run monthly updates
    accounts = [checking, savings]
    run_monthly_updates(accounts)