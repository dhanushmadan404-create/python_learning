p=input("Enter your payment mode:")
match p:
    case "upi":
        print("You selected UPI payment")
    case "card":
        print("You selected Debit/Credit card payment")
    case "netbanking":
        print(" you selected NetBanking")
    case "cod":
        print("you selected cash on Delivery")
    case _:
        print("Invalid Payment Mode")