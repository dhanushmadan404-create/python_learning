a="aswin"
b="samanda"  
a=list(a)
b=list(b) 
f=["f","l","a","m","e","s"]
for i in a:
    value=i
    count=0
    for j in b:
        if i==j:
            count=1
            b.remove(j)
    if count==1:
        a.remove(i)

count=len(a)+len(b)




