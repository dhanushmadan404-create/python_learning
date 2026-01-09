# Products
class SouthDosa:
    def prepare(self):
        return "South Indian Dosa"

class NorthDosa:
    def prepare(self):
        return "North Indian Dosa"

class SouthTea:
    def serve(self):
        return "South Indian Tea"

class NorthTea:
    def serve(self):
        return "North Indian Tea"


# Abstract Factory
class HotelFactory:
    def create_dosa(self):
        pass
    def create_tea(self):
        pass


# Concrete Factories
class SouthHotel(HotelFactory):
    def create_dosa(self):
        return SouthDosa()
    def create_tea(self):
        return SouthTea()

class NorthHotel(HotelFactory):
    def create_dosa(self):
        return NorthDosa()
    def create_tea(self):
        return NorthTea()


# Client
def order(hotel):
    print(hotel.create_dosa().prepare())
    print(hotel.create_tea().serve())

order(SouthHotel())
order(NorthHotel())
