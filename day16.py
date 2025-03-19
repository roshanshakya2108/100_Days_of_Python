x = int(input("Enter your desire value: "))

match x:
    case 0:
        print("X is zero.")
    case 4:
        print("X is the case of 4.")
    case _:
        print(x)