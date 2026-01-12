import math
# def count(t):
#     count=0
#     for i in t:
#         if i ==2:
#             count+=1
#         elif i%2!=0:
#             count+=1
#     print(count)
# count({8, 14, 11, 23, 6})


# def count(n):
#     for i in range(1,n+1):
#         a=" "*i
#         for y in range(i,n+1):
#             a+=" "+"*"
#         print(a)

# count(8)


# print("Try programiz.pro")


def gcd(one):
  smaller=math.inf
  for i in one:
      if smaller >i:
          smaller=i
    
  for i in range(1,smaller+1):
      count=0
      for y in one:
          if y%i==0:
              gcd=y
          else:
              count+=1
      if count==0:
          break
            
     
  print(gcd)
  
    
gcd([6,3,2])


# def pattern(d):
#     for i in range(1,d+1):
#         number=""
#         for y in range(1,d+1):
#             number+=str(i)
#         print(number)
# pattern(3)



