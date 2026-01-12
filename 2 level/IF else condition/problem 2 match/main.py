x=int(input("enter your mark"))
# y=x>=100 and x<=80
# z=x<80 and x>=60
# a=x<60 and x>=50
# b=x<50 and x>=40
match x:
    case _ if x>=100 and x<=80:
        print("A")
    case _ if  x<80 and x>=60:
        print("B")
    case _ if x<60 and x>=50:
        print("C")
    case _ if x<50 and x>=40:
        print("D")
    case _ if x<40 and x>=0:
        print("E")
    case _:
        print("invalid")
