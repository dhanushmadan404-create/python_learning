# Find the LCM amongst a list of Positive Integers.
import math
# def lcm(list):
#     smaller=math.inf
#     gcd=0
#     lcm_num=1
#     for small in list:
#         lcm_num+=small
#         if small<smaller:
#             smaller=small
#     for i in range(1,small+1):
#         count=0
#         for el in list:
#              if el%i!=0:
#                  count+=1
#         if count==0:
#             gcd=i
#     print(gcd)
# lcm([2,6,8,4,10])


# Find the factorials of each of the integers given in an List.

# def fact(list):
#     factorial=[]
#     for el in list:
#         mul=1
#         for num in range(el,1,-1):
#             mul*=num
#         factorial.append(mul)
#     print(factorial)

# fact([2,1,3,3,5])


# Perform search and replace without using library functions. Given a String "This is programming" find_str = "is" and replace "are" result should be "Thare are programming"

# def string(sen):  
#     new=""  
#     for el in range(0,len(sen)):
#         if sen[el]=="i" and sen[el+1]=="s":
#             new+="are"
#         elif sen[el]=="s" and sen[el-1]=="i":
#             new+=""
#         else:
#             new+=sen[el]
#     print(sen)
#     print(new)
# string("This is programming")
            

# for i in range(0,3):
#     gap=" "*(3)
#     gap+=str(i)
#     gap=str(i)+gap
# print(gap)