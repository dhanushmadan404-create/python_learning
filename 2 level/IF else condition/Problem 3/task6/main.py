num=int(input("Enter your number THAT IS DIVISIBLE BY 3 AND 5:"))
if num%3==0 and num%5==0:
    print("FIZZBUZZ")
elif num%3==0:
    print("FIZZ")
elif num%5==0:
    print("BUZZ")
else:
    print("YOUR NUMBER NOT DIVISIBLE BY 3 AND 5")