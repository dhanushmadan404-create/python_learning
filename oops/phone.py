class contactBook:
    def __init__(self):
        self.contact=[]
    
    def add_contact(self,name:str,number:int,email:str):
        self.contact.append({"name":name,"number":number,"email":email})
    
    def get_number(self,name:str):
        for con in self.contact:
            if con["name"]==name:
                print( con)
        return " " 
    
    def update(self,name:str,change:int):
        for con in self.contact:
            if con["name"]==name:
                con["number"]=change
                print(con)
            
    def delete_contact(self,name:str):
        for con in self.contact:
            if con["name"]==name:
                self.contact.remove(con)
            
        print(self.contact)
    
my_book = contactBook()

my_book.add_contact("John", "9994254379", "alice@email.com")
my_book.add_contact("Bob", "9876543210", "bob@email.com")

print(my_book.get_number("John") ) # Should output: 123-456-7890
print(my_book.get_number("Charlie")) # Should output: Contact not found.

my_book.update("John","8994254379") # should update the contact
my_book.delete_contact("Bob") # should delete and print output: "Deletion Completed"

my_book.delete_contact("Ram") # Should Print: Contact Not found