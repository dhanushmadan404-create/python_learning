n=int(input("Enter you number"))
re=0
while n>=0:
    add =n%10
    re=re*10+n
    n//=10
print(re)
