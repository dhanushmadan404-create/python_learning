a=[55,55,55,-55,55]
b=max(a)
i=0
while i<len(a):
    if a[i]==b:
        a.remove(a[i])
        i=0
    else:
        i+=1
    
# print(max(a))