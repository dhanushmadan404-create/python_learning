a=int(input("Enter your start number "))
b=int(input("Enter your end number"))
c=0
while a<=b:
    if a%2==0:
        c+=a
    a+=1
print(c)