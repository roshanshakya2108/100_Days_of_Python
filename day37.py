# try:
#     l = [1,2,3,4,56,7,8,49,94,4,946,46,5]
#     i = int(input("Enter index: "))
#     print("Length of l",len(l))
#     print(l[i])
# except:
#     print("Some Error Occured.")


# finally:
#     print("I am always excuted.")




def fun():
    try:
        l = [1,2,3,4,56,7,8,49,94,4,946,46,5]
        i = int(input("Enter index: "))
        print("Length of l",len(l))
        print(l[i])
        return 1
    except:
        print("Some Error Occured.")
        return 0

    finally:
        print("I am always excuted.")
    # print("I am always excuted.")

x = fun()
print(x)
