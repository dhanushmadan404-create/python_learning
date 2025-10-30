class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        pass
    def add(self):
        return 'add:',self.a+self.b
    def sub(self):
        return 'subtracts',self.a-self.b
    def multiple(self):
        return'Multiple',self.a*self.b
    def division(self):
        try:
             return'division',self.a//self.b
        except ZeroDivisionError:
            return"It's undefined division"
p1=Calculator(239,140)
print(p1.add())
print(p1.sub())
print(p1.multiple())
print(p1.division())
