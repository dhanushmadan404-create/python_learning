class todo:
    def __init__(self):

        self.detail=[]

    def add_task(self,id:int,task:str,status:bool=False):

        add={"id":id,"task":task,"status":status}

        self.detail.append(add)

    def view_task(self,name):

        for el in self.detail:

            if el["task"]==name:
            
                return el
          

    def Delete_task(self,name):

        for el in self.detail:

            if el["task"]==name:

                self.detail.remove(el)

        print("Successfully deleted")
    def view_all(self):
        print(self.detail)

       
  
#   def add_task(self,id:int,task:str,status:bool=False):
# child
class details(todo):
    def __init__(self):
        super().__init__()

    def mark_completed(self,name,change):
        for el in self.detail:
            if el["task"]==name:
                el["status"]=change
                print(el)
       
    def filter_completed(self):
        for el in self.detail:
            if el["status"]==True:
                print(el)
    def filter_bending(self):
         for el in self.detail:
            if el["status"]!=True:
                print(el)
    def clear_all(self):
       self.detail.clear()
       print(self.detail)
       return "Successfully "


p=details()
p.add_task(1,"dhanush",False)

p.add_task(1,"omr",True)

p.add_task(1,"avadi",True)

p.add_task(1,"kk",False)

print(p.view_task("omr"))

# print(" ")
p.Delete_task("avadi")
# print(" ")
p.view_all()
# print(" ")
p.mark_completed(name="kk",change=True)
print(" ")

(p.filter_completed())
print(" ")
(p.filter_bending())
print(' ')
print(p.clear_all())

# p=details()
# p.add_task(1,"rehana",False)