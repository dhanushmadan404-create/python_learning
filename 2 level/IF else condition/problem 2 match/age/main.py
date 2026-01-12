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
