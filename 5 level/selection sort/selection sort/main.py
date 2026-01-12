n=[12, 41, 77, 30]
def find_maximum(n):
    for i in range(len(n)):
        min=i
        for y in range(i,len(n)):
            if n[min]>n[y]:
                min=y
        n[i],n[min]=n[min],n[i]
    print(n)
find_maximum(n)
