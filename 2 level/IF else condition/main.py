A=int(input("Enter your amount"))
amount_1000=(A*10/100)
amount_500=(A*5/100)
if A >= 1000:
    print(A-amount_1000)
elif A >=500 and A<1000:
    print(A-amount_500)
else :
    print(A)