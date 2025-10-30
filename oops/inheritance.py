# parent
class Factory:
    def __init__(self):
        pass
    def make_vehicle(self):
        print("I am making a general vehicle")
# class Child_class_name(Parent_class_name)
class CarFactory(Factory):
    def __init__(self):
        pass
    def make_cars(self):
        print("I am making only cars")
    def make_vehicle(self):
        print("I am changing the print statement")
class BikeFactory(Factory):
    def __init__(self):
        pass
    def make_bike(self):
        print("I am making only bikes")
    def make_vehicle(self):
        print("I am changing it to other print statement")
new_car_fac=CarFactory()
# self property
new_car_fac.make_cars()
# parent property
new_car_fac.make_vehicle()
new_bike_fac=BikeFactory()
new_bike_fac.make_bike()
new_bike_fac.make_vehicle()
