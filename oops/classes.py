class BankManagement:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        pass
    def deposit(self,amount):
        self.balance=self.balance+amount
        return 'name:',self.name,'balance:',self.balance
    def withdrawn(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
            return 'name:',self.name,'balance:',self.balance
        else:
            "warning_Check_Your_balance"
        
sec1=BankManagement("Dhanush",10000)
print(sec1.deposit(5000))
print(sec1.withdrawn(14000))
