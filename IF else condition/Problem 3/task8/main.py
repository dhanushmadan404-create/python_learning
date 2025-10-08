t=int(input("Enter your railway time for movie: "))
if t>9 and t<=12:
    print("Morning Show")
elif t>12 and t<=16:
    print("matinee show")
elif t>16 and t<=20:
    print("Evening show")
else:
    print("Invalid time for movie")