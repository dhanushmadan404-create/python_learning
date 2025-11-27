print("Try programiz.pro")
arr=[ 7, 12, 9, 11, 3]
for el in range(len(arr)):
    small=el
    for el2 in range(el,0-1,-1):
        if arr[el]<arr[el2]:
            small=el2
    remove_num=arr.pop(el)
    arr.insert(small,remove_num)
print(arr)