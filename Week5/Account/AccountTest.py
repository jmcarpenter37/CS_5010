# Name: John Carpenter
# ID: jmc7dt
# Assignment: HW 5 Python + Unit Testing
# This script tests the Account.py file
import unittest
from Account import *

# Begin unit testing the Account file
class AccountTest(unittest.TestCase):
    def test_AcctNumber(self):
        account1 = Account("12345", 500)
        self.assertEqual(account1.accountNumber , "12345")

    # test the balance
    def test_balance(self):
        account1 = Account("12345", 500)
        self.assertEqual(account1.balance , 500)

    # Testing for sub class inheritance
    def test_balance_inherit(self):
        # create account
        account1 = Account("12345", 500)
        checking_init = Checking("12345" , 500 , 5)
        print("Checking inherit test: " , checking_init.balance)
        self.assertEqual(account1.balance , checking_init.balance) # check to see if both inheritance and balance works
    # Testing for acct number inheritance
    def test_acctNum_inherit(self):
        # create account
        account1 = Account("12345", 500)
        checking_init = Checking("12345" , 500 , 5)
        print("Checking account number test: " , checking_init.accountNumber)
        self.assertEqual(account1.accountNumber , checking_init.accountNumber) # check to see if both inheritance and balance works


    # Testing for the fee method
    def test_fee(self):
        account1 = Account("12345", 500)
        checking_init = Checking("12345", 500, 5)
        print("Checking inherit fee: ", checking_init.fee)
        self.assertEqual(checking_init.fee, 5)  # check to see if both inheritance and balance works

    # Testing the grabFee method
    def test_grabFee(self):
        account1 = Account("12345" , 500)
        # inheritence check
        checking_init = Checking(account1.accountNumber , account1.balance , 5)
        self.assertEqual(checking_init.fee , checking_init.grabFee() )

    # Testubg the deposit money method
    def deposit_money(self):
        account1 = Account("12345", 500)
        # inheritence check
        checking_init = Checking(account1.accountNumber, account1.balance, 5)
        # We are going to deposit 10 bucks. So we know there should be 510
        print("Checking balance: ", checking_init.deposit_money(10))
        self.assertEqual(checking_init.balance + 10 , checking_init.deposit_money(10))


    # Testing the withdraw_money method
    def withdraw_money(self):
        account1 = Account("12345", 500)
        # inheritence check
        checking_init = Checking(account1.accountNumber, account1.balance, 5)
        # Withdraw 10
        withdraw = checking_init.withdraw_money(10)
        self.assertEqual(checking_init.balance - 10 , withdraw)

if __name__ == '__main__':
    unittest.main()



