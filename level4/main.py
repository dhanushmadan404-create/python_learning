# Given an array of Positive integers, count the number of prime numbers in it. Sample Input: {8, 14, 11, 23, 6}, Output: 2
def is_prime(n):
    count=0
  
    for i in n:
        checkCount=0
        check=i//2
        if i==0 or i==1:
            continue
        if i==2:
            count+=1
        else:
            for y in range(2,check+1):
                if i%y==0:
                    checkCount+=1
            if checkCount==0:
                count+=1
    print(count)
is_prime([8, 14, 11, 23, 6])

        
            

