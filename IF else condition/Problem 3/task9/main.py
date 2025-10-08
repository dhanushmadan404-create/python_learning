
t=int(input("Enter your conversion number: "))
c=int(input("Enter your converted by (1 is meter/2 is centimeter/3 is millimeter/4 is miles): "))
match c:
    case 1:
        print(c*1000)
    case 2:
        print(c*1000*100)
    case 3:
        print(c*1000*1000)
    case 4:
        print(c*0.621371)
    case _:
        print("invalid conversion number")