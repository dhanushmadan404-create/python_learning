vowel=input("Enter your letter")

match vowel:
    case 'a'|'e'|'i'|'o'|'u':
        print("vowel")
    case _:
        print("Consonant")

