# rating=int(input("enter your rating for the movie"))
# match rating:
#     case 5:
#         print("very good movie")
#     case 4:
#         print("good")
#     case 3:
#         print("average")
#     case 2:
#         print("bad")
#     case 1:
#         print("very bad")
#     case _:
#         print("invalid")

# this is traffic light
# traffic=str(input("enter you traffic light color"))

# match traffic:
#     case "RED":
#         print("stop")
#     case "yellow":
#         print("ready")
#     case "green":
#         print("go")
#     case _:
#         print("invalid")



# num=int(input("Enter your number"))
# if num>0:
#     print("the number is positive")
# elif num<0:
#     print("The number is negative")
# else:
#     print("the number is zero")


letter=(input("Enter your one letter in lower case"))

if letter in ("a","e","i","o","u"):
    print("the character is  a vowel")
else:
    print("The character is a consonant")