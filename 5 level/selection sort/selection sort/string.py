sen=["banana","dragon","carrot","apple","abrow"]
for el in range(len(sen)):
    small=el

    for swap in range(el,len(sen)):
        if sen[small]>sen[swap]:
            small=swap
    sen[el],sen[small]=sen[small],sen[el]
print(sen)
