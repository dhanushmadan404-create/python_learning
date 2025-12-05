arr= [ 2, 3, 0, 2, 3, 2]
big=max(arr)
new=[]
count=[0]*(big+1)

for i in arr:
    count[i]+=1
print(count)
for i in range(len(count)):
    for y in range(1,count[i]):
        new.append(i)

print(new)
