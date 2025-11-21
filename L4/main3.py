# :three: Find Pair With Minimum Difference
# Input: [4,9,1,32,13]
#  Output: (4,1)
import math
def num(a):
    small=math.inf
    for i in a:
        for y in range(1,len(a)):
            sum=i - a[y]
            if sum<small:
                small=sum
                dif=[i,a[y]]
    print(dif)

num([4,9,1,32,13])

            