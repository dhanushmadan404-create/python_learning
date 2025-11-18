def count(t):
    count=0
    for i in t:
        if i ==2:
            count+=1
        elif i%2!=0:
            count+=1
    print(count)
count({8, 14, 11, 23, 6})


def count(n):
    for i in range(1,n+1):
        a=" "*i
        for y in range(i,n+1):
            a+=" "+"*"
        print(a)

count(8)


print("Try programiz.pro")


def gcd(one,two):
  if one<two:
      smaller=one
  else:
      smaller=two
       
  for i in range(1,smaller+1):
      if one%i==0 and two%i==0:
          gcd=i
  print("gcd:",gcd)
  print("lcm:",one*two//gcd)
  
    
gcd(64,89)


