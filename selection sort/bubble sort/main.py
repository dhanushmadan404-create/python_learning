arr=[ 7, 12, 9, 11, 3]

for i in range(len(arr)):
    for el in range(len(arr)-i-1):
        if arr[el]>arr[el+1]:
            arr[el],arr[el+1]=arr[el+1],arr[el]
print (arr)
