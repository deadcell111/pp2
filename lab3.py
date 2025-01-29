class BankAccount:
    print("enter your name and account: ")
    def __init__(self,owner = None,balance = None):
        if owner is None and balance is None:
            owner = input()
            balance = int(input())
        self.owner = owner
        self.balance = balance

    def deposit(self,money = None):
        print("specify how much you want to add: ")
        if money is None:
            money = int(input())
        self.balance += money
        print("The new balance is: ",self.balance)
    def withdraw(self,money = None):
        print("specify how much you want to take: ")
        if money is None:
            money = int(input())
        if self.balance >= money:
            self.balance -= money
            print("The new balance is: ",self.balance)
        else:
            print("insufficient funds on the card")
if __name__ == "__main__":
    bank = BankAccount()
    bank.deposit()
    bank.withdraw()

        

        