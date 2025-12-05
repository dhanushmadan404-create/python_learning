arr=[ 7, 12, 9, 11, 3,4]
small=arr[0]
for i in range(len(arr)):
    if small > arr[i]:
        small=arr[i]
print(small)