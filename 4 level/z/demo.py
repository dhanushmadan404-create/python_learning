age=int(input("enter your age for movie"))

if age>0 and age<=5:
    print("free ticket")
elif age<5 and age>=12:
    print("price 10 rupee")
elif age>12 and age<=64:
    print("price 20 rupee")
elif age>65 and age<100:
    print("price 15 rupee")
else :
    print("invalid age")
 

month=int(input("ENter your month"))

match month:
    case 1:
        print("January") 
    case 2:
        print("february")
    case 3:
        print("march")
    case 4:
        print("April")
    case 5:
        print("may")
    case 6:
        print("jun")
    case 7:
        print("july")
    case 8:
        print("august")
    case 9:
        print("september")
    case 10:
        print("october")
    case 11:
        print("november")
    case 12:
        print("December")
    case _:
        print("Invalid month")