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