class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print('name',self.name,'age',self.age)
class student(person):
    def __init__(self,name,age):
        super().__init__(name,age)

student1=student("Dhanush",27)