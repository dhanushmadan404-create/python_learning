# 28-10-25
# SeparateTheVowel
def vowel(v):
    m=('a','e','i','o','u')
    n=[]
    for y in v:
        if y in m:
            n.append(y)
    print(n)
vowel("education")


# HighestVowelWord
def word(w):
    vow=('a','e','i','o','u')
    new={}
    for i in w:
        count=0
        for y in i:
            if y in vow:
                count+=1
        new.update({count:i})
    print(max(new.items()))
word(["cat", "eagle", "umbrella", "sky"])

# CountEvenNumberOddNumber
def num(n):
    even=0
    odd=0
    if len(n)==0:
        print('NumberError')
    else:
        for i in n:
            if i%2==0:
               even+=1
            else:
               odd+=1
        print(f'even:{even}  odd:{odd}')
num([1, 2, 3, 4, 5, 6, 7])


# FirstAndLast
def index(n):
    v=[]
    if len(n)==0:
        print('ValueError')
    else:
        for i in range(0,len(n)):
            if n[i]==5:
               v.append(i)
        print(f'firstIndex: {min(v)}, lastIndex: {max(v)}')
index([5, 2, 3, 5, 7, 5, 8])

# list-combine
def lists(i,j):
    new=[]
    for k in range(0,len(i)):
        new.append(i[k])
        new.append(j[k])
    print(new)
lists( [10, 20, 30] ,[1, 2, 3]) 