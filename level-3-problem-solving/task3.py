def words(a):
    count=0
    vowel=['a','e','i','o','u',' ']
    for i in a:
        if i not in vowel:
            count+=1
    print(count)
words('hello world')
            