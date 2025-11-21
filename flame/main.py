a=list(input("Enter your name "))
b=list(input('Enter your lover name '))   
f=["f","l","a","m","e","s"]
for i in a:
    for j in b:
        if i==j:
            a.remove(i)
            b.remove(j)
ab1=len(a)+len(b)

for i in range(1,ab1):
    

# print(ab1) 
# b1=""
# ab1=[]

# for i in a:
#     count=0
#     for y in b:
#         if i == y:
#             count+=1
#     if count==0:
#         a1+=i
    
# for i in b:
#     count=0
#     for y in a:
#         if i == y:
#             count+=1
#     if count==0:
#         b1+=i

# count=len(a1)+len(b1)


# print(a1,b1,count) 
   
# print(ab1)

