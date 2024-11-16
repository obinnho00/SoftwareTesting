class Account_creation:
    def __init__(self):
        # Initializes an empty dictionary to store accounts
        self.account = {}

    # Creates a new account with an account number and initial deposit
    def Create_Account(self, account_number, deposit):
        if account_number <= 0:
            raise ValueError("Account number is invalid")
        if account_number in self.account:
            raise ValueError("Account already in use, create a new account")
        self.account[account_number] = deposit
        return True

    # Retrieves the account details for a given account number
    def get_account_number(self, account_number):
        return self.account.get(account_number, False)

    # Retrieves the balance of a specific account
    def get_Balance(self, account_number):
        return self.account.get(account_number, False)

    # Deposits a specified amount into an account
    def set_Deposit(self, account_number, amount):
        if amount <= 0:
            raise ValueError("Deposit must be greater than 0")
        if account_number in self.account:
            self.account[account_number] += amount
        else:
            raise ValueError("Account does not exist")

    # Withdraws a specified amount from an account
    def set_Withdrawal(self, account_number, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than 0")
        if account_number not in self.account:
            raise ValueError("Account does not exist")
        if self.account[account_number] >= amount:
            self.account[account_number] -= amount
        else:
            raise ValueError("Insufficient funds")


import unittest

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        # Initializes the Account_creation class before each test case
        self.bank = Account_creation()

    # Tests creating a new account
    def test_Create_Account(self):
        self.assertTrue(self.bank.Create_Account(1234, 100))
        self.assertEqual(self.bank.account[1234], 100)

    # Tests creating an account with a duplicate account number
    def test_Create_Duplicate_Account(self):
        self.bank.Create_Account(1234, 100)
        with self.assertRaises(ValueError):
            self.bank.Create_Account(1234, 100)

    # Tests creating an account with an invalid account number
    def test_Create_Invalid_Account(self):
        with self.assertRaises(ValueError):
            self.bank.Create_Account(0, 100)
        with self.assertRaises(ValueError):
            self.bank.Create_Account(-1234, 100)

    # Tests retrieving an existing account number
    def test_get_account_number(self):
        self.bank.Create_Account(1234, 100)
        self.assertEqual(self.bank.get_account_number(1234), 100)
        self.assertFalse(self.bank.get_account_number(3456))

    # Tests retrieving the balance of an account
    def test_get_Balance(self):
        self.bank.Create_Account(1234, 100)
        self.assertEqual(self.bank.get_Balance(1234), 100)
        self.assertFalse(self.bank.get_Balance(3456))

    # Tests depositing money into an account
    def test_set_Deposit(self):
        self.bank.Create_Account(1234, 100)
        self.bank.set_Deposit(1234, 50)
        self.assertEqual(self.bank.get_Balance(1234), 150)

    # Tests making invalid deposits (negative or zero amount)
    def test_invalid_Deposit(self):
        self.bank.Create_Account(1234, 100)
        with self.assertRaises(ValueError):
            self.bank.set_Deposit(1234, -50)
        with self.assertRaises(ValueError):
            self.bank.set_Deposit(1234, 0)

    # Tests depositing money into a non-existent account
    def test_Deposit_nonexistent_account(self):
        with self.assertRaises(ValueError):
            self.bank.set_Deposit(3456, 50)

    # Tests withdrawing money from an account
    def test_set_Withdrawal(self):
        self.bank.Create_Account(1234, 100)
        self.bank.set_Withdrawal(1234, 50)
        self.assertEqual(self.bank.get_Balance(1234), 50)

    # Tests withdrawing an amount greater than the account balance
    def test_insufficient_funds(self):
        self.bank.Create_Account(1234, 100)
        with self.assertRaises(ValueError):
            self.bank.set_Withdrawal(1234, 150)

    # Tests withdrawing money from a non-existent account
    def test_Withdrawal_nonexistent_account(self):
        with self.assertRaises(ValueError):
            self.bank.set_Withdrawal(3456, 50)

    # Tests withdrawing invalid amounts (negative or zero amount)
    def test_invalid_Withdrawal(self):
        self.bank.Create_Account(1234, 100)
        with self.assertRaises(ValueError):
            self.bank.set_Withdrawal(1234, 0)
        with self.assertRaises(ValueError):
            self.bank.set_Withdrawal(1234, -50)


if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
