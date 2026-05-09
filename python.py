class BankAccount:
    # class variable
    bank_name="gauraand bank";

    def __init__(self, owner,balance=0):  # constructor
        self.owner=owner;
        self.__balance=balance;     # private variable  (encapsulation/data hiding)

    def deposit(self,amount):    # instance method
        if(self.isValidAmount(amount)):
            self.__balance+=amount;

    def withdraw(self,amount):  # instance method
        if (self.isValidAmount(amount) and amount <=self.__balance):
            self.__balance-=amount;

    @classmethod
    def bank_info(cls):
       print(cls.bank_name);


    @staticmethod
    def isValidAmount(amount):
       return amount>0

    def getBalance(self):
        return self.__balance;
    def showBalance(self):
        print(self.__balance);


class SavingsAccount(BankAccount):
    def __init__(self,owner,balance=0,interest_rate=5):
        super().__init__(owner,balance)
        self.interest_rate=interest_rate

# method overriding
    def withdraw(self,amount):
        print("savings account withdrawl")
        super().withdraw(amount);

    def add_interest(self):
        interest=(self.getBalance()*self.interest_rate)/100;
        self.deposit(interest);


## class bankaccount and class savings account
acc1=BankAccount("gauraand",55);  # object of BankBalance
acc2=SavingsAccount("gunnugaand",5555,10);  # OBJECT OF SAVINGS ACCOUNT EHICH IS INHERITED
acc1.showBalance();
acc2.showBalance();
BankAccount.bank_info()
SavingsAccount.bank_info()
print(BankAccount.isValidAmount(55))
print(SavingsAccount.isValidAmount(555));
print(SavingsAccount.isValidAmount(-66));

acc1.withdraw(44);
acc2.withdraw(55);

acc1.showBalance();
acc2.showBalance();

acc1.deposit(444);
acc2.deposit(5225);

acc1.showBalance();
acc2.showBalance();

acc2.add_interest();
acc2.showBalance();








