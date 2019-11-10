# Q7
# Create a base class called account
# Account should have the following attributes: accountNumber and balance, which should be correctly initialized in the constructor (_ _init_ _) method for the class.
# Create a to-string (_ _str_ _) method that prints “Account number 1234” on one line and “Balance: 2000” on the next line (example with account number of 1234 and balance of 2000).

class Account: # Defining the Account class
    def __init__(self , accountNumber , balance): # defining the constructor
        self.accountNumber = accountNumber
        self.balance = balance
        self.transaction = []

    def __str__(self):
        #"Your account number is: {}\nYour balance is: {}".format(self.accountNumber, self.balance)
        return "Your account number is: {}\nYour balance is: {}".format(self.accountNumber, self.balance)


startingAccount = Account('12345' , '2000')

# Create another class called CHECKING. This class should inherit from the Account class. Therefore, the Checking class is the derived class.
# In addition to the accountNumber and balance attributes, the Checking class has a fee attribute (that is used when withdrawing money from the Checking account). Initialize all variables correctly in the constructor (_ _init_ _) method.

class Checking(Account):
    def __init__(self , accountNumber , balance , fee):
        Account.__init__(self , accountNumber , balance)
        self.fee = fee

    def __str__(self):
        baseString = Account.__str__(self)
        inheritFee = self.fee
        return "The account type is Checking.\n{}\nThe fee with this accoutn is: {}".format(  baseString , inheritFee)


test2 = Checking('12345' , 30000 , 3)
print(test2)