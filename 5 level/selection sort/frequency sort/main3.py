arr=[4, 4, 5, 8, 4, 2, 2, 6, 5]


# [2,2,4,4,4,5,5,6,8]
demo=dict()
new=[]
mul=[]
# This loop for align as dict like key is the num and value is the count of the num
count=0
for i in arr:
    demo.update({i:count+1})
print(demo)