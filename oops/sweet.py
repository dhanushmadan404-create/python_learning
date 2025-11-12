class magesh:
    
    def __init__(self):
        
        self.sweets=[]
    def add_item(self,id:int,product:str,quantity:int,price:float):
        item={"id":id,"product":product,"quantity":quantity,"Price":price}
        self.sweets.append(item)
    def remove(self,name):
        for el in self.sweets:
            if el["product"]==name:
                self.sweets.remove(el)
                
                return "successfully removed"
            else:
                return "not found"
        
    def display(self):
        add=0
        for el in self.sweets:
            add+=el["Price"]*el["quantity"]
        return add
    
    def change(self,id,product,quantity,price):
        for el in self.sweets:
            if el["id"]==id:
                el.update({"id":id,"product":product,"quantity":quantity,"Price":price})
                return "successfully updated"
            else:
                return "not found"
c1=magesh()
c1.add_item(1,"samosa",3,90.0)
c1.add_item(2,"water",4,50.0)
c1.change(3,"saamosa",3,90.0)
print(c1.remove("samosa"))
print(c1.display())