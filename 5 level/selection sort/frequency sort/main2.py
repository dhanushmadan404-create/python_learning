arr=[4, 4, 5, 8, 4, 2, 2, 6, 5]
# [2,2,4,4,4,5,5,6,8]
demo=dict()
new=[]
mul=[]
# This loop for align as dict like key is the num and value is the count of the num
for i in range(len(arr)):
    count=0
    for y in range(len(arr)):
        if arr[i]==arr[y]:
            count+=1
    demo[arr[i]]=count
print(demo)

# this loop for if value is 1 append in new list else:
# append in mul list
for key,value in demo.items():
    if value ==1:
        new.append(key)
    else:
        mul.append([key]*value)

# print(new)
# print(mul)

index=0
# sorting the new list
while index<len(new)-1:
    if new[index]>new[index+1]:
        new[index],new[index+1]=new[index+1],new[index]
        index=0
    else:
        index+=1

index2=0
# sorting the mul list
while index2<(len(mul)-1):
    if mul[index2][0]>mul[index2+1][0]:
        mul[index2],mul[index2+1]=mul[index2+1],mul[index2]
        index2=0
    else:
        index2+=1
print(new)
print(mul)
# This loop for combine the two list as frequency list
for el in mul:
    for el2 in el:
        new.append(el2)
print(new)

# loop=6
# condition=7