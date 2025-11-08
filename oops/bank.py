class bankAc:
    def __init__(self,name:str,balance:int):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"deposit successful::{self.balance}")
        else:
            print("invalid")
    def withdraw(self,amount:int):
        if amount>0:
            if amount<=self.balance:
                self.balance-=amount
                print(f"withdraw successful::{self.balance}")
            else:
                print("insufficient Balance")
        else:
            print("error")
    def transfer(self,other,amount:int):
        if amount<=self.balance:
            self.balance-=amount
            other.balance+=amount
        else:
            print("insufficient")
    def detail(self):
        print(f"{self.name}Balance:{self.balance}")
    
a1=bankAc("dhanush",10000)
a2=bankAc("madan",5000)
a1.detail()
a2.detail()
a1.deposit(5000)
a2.withdraw(3000)
a1.transfer(a2,10000)
a1.detail()
a2.detail()
