arr= [ 2, 3, 0, 2, 3, 2]
big=max(arr)
new=[]
count=[0]*(big+1)

for i in arr:
    count[i]+=1
print(count)
arr.clear()
for i in range(len(count)):
    for y in range(count[i]):
        new.append(i)

print(new)
