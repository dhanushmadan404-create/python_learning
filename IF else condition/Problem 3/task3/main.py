p_t=input("Enter your property type(residential/commercial)")
u=int(input("Enter your units"))
if p_t == "residential":
        if u <= 100:
            print(u * 3)
        elif u <= 200:
            print(100 * 3 + (u - 100) * 5)
        else:
            print(100 * 3 + 100 * 5 + (u - 200) * 7)
elif p_t == "commercial":
        if u <= 100:
            print(u * 5)
        elif u <= 200:
            print(100 * 5 + (u - 100) * 7)
        else:
            print(100 * 5 + 100 * 7 + (u - 200) * 10)
else:
    print( "Invalid consumer type")