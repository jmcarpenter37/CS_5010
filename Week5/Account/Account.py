# Name: John Carpenter
# ID: jmc7dt
# Assignment: HW 5 Python + Unit Testing

class Account: # This is the base class Account
    def __init__(self, accountNum, balance):
        self.accountNumber = accountNum  # account number
        self.balance = balance  # balance

    def __str__(self):
        return "Your account number is: " + self.accountNum + "Your balance is: " + str(self.balance)
# Begin the Checking subclass
class Checking(Account):  # Checking class inheriting the account class
    # Init constructor
    def __init__(self, accountNum, balance, fee):
        Account.__init__(self, accountNum, balance)
        self.fee = fee
    # str constructor
    def __str__(self):
        returnString = Account.__str__(self)
        return "Account Type is {}".format( returnString)
    # Pull the accounts associated fees
    def grabFee(self):
        return self.fee #return the fee for the checking account
    # Put some money into my account
    def deposit_money(self, amount):
        self.balance += amount
    # Take some money out of my account
    def withdraw_money(self, amount):
        if self.balance < amount:
            print("Cannot withdraw this much. There isn't enough money in your account.")
        else:
            self.balance = self.balance - self.fee - amount # Set balance by taking out the fees and amount withdrawn

# Check to see if base class Account works
acc_ret = Account("12345" , 500)
print("Your balance is: ",acc_ret.balance)
print("Your account number is: ",acc_ret.accountNumber) # They work!
checking = Checking(acc_ret.accountNumber , acc_ret.balance , 5)
print(checking.grabFee())