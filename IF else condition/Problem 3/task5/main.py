a=int(input("Enter your a side triangle:"))
b=int(input("Enter your b side triangle:"))
c=int(input("Enter your c side triangle:"))
if a+b<=c or b+c<=a or c+a<=b:
    print("Not a valid triangle")
else:

    if a==b==c :
        print("Equilateral")
    elif a==b!=c or b==c!=a or c==a!=b:
        print("Isosceles")
    elif a!=b!=c:
        print("scalene")

