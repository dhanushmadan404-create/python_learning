arr=[1,3,5,5,1,0,2]
arr=[4, 4, 5, 6, 4, 2, 2, 8, 5]
arr=[1, 3, 5, 5, 1, 0, 2]


#shuffled number of  arr list 

new=[]
# this list for store the single number

same=[]
# this list for store the multiple number
temp=[]
temp2=[]
#This loop for get every element
for i in range(len(arr)):
    count=0
     #every time count to become zero
    for y in range(len(arr)): 
        #This loop start in parent element because comparison
        if arr[i]==arr[y]:
            #if matched count will increases
            count+=1
   
        #the value couldn't in same list because every value double time comes
    if count==1:
            #count is one append in new
        new.append(arr[i])
    elif arr[i] not in temp2:
        temp=[]
           #count will in loop because this loop takes how many time it's came
        for z in range(count):
            temp.append(arr[i])
            temp2.append(arr[i])
             #append the values
        same.append(temp)
print(new)
print(same)
#sort the new and same list

index=0
while index<(len(new)-1):
    if new[index]>new[index+1]:
        new[index],new[index+1]=new[index+1],new[index]
        index=0
    else:
        index+=1
print(new)


y=0
while y<(len(same)-1):
    if same[y][0]>same[y+1][0]:
        same[y],same[y+1]=same[y+1],same[y]
        y=0
    else:
        y+=1

# align as in new list
for i in same:
    for y in i:
        new.append(y)

print(new)

# loop=7
# condition=7


    