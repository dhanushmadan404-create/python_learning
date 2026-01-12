n=[1, 12, 7, 11, 3]

for i in range(len(n)):
    index=i
    value=n[i]
    for y in range(i,-1,-1):
        if value<n[y]:
            index=y
            n[y+1]=n[y]
    n[index]=value
print(n)
print(3>3)

