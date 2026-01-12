c=input("choose your (science/commerce/arts):")
match c:
    case 'science':
        s=input("choose your medical or engineer:")
        match s:
            case 'medical':
                print("science->medical")
            case 'engineer':
                print("science->engineer")
    case 'commerce':
        C=input("Choose your CA or B COM:")
        match C:
            case 'CA':
                print("COMMERCE->CA")
            case 'B COM':
                print("COMMERCE->B COM")
    case 'arts':
        a=input("Choose your history or literature:")
        match a:
            case 'history':
                print("COMMERCE->CA")
            case 'literature':
                print("COMMERCE->B COM")
    case _:
        print("invalid career")           
        
                            

