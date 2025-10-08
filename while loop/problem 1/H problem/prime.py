n=int(input("enter your number "))
i=2
if n==0 or n==1:
    print("is not prime number")
elif  n%2==0:
     
     print("n is not prime number")
else:

     while i<=n:
          
          if i%n==0:
            print("n is prime number")
          i+=1
