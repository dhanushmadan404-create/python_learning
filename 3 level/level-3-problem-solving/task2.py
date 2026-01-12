def reverse_letter(a):
    b=[]
    for i in range(0,len(a)):
        b.insert(0,a[i])
    print(b)
reverse_letter("python")