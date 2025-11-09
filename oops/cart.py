class product:
    def __init__(self):
        self.cart={}
    def add_item(self,name,price,quantity):
        self.cart.update({'name':name},{'price':price},{'quantity':quantity})
    def remove(self,other):
        if other in self.cart:
            del self.cart[other]
        else:
            print("not in the cart")
    def search(self,name):
        for i ,y ,z in self.cart.keys():
            if i ==name:
                print(i,y,z)
            else:
                print("not in list")
        