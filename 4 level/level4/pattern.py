n=10
pattern="*"*n
for i in range(n):
    pattern="* "*(n-i)
    print(" "*i+pattern)