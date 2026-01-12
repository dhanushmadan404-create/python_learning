# T pattern
n=9
foo=""
for i in range (1,n+1):
    foo+="*"+" "
print(foo)
new=((n+(n-1))//2)
koo=""
for i in range(1,new+1):
    koo=(" "*new)+"*"
    print(koo)

