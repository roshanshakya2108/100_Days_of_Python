def average(a,b):
#def average(a=5,b=1):
    print("The average is ",(a+b)/2)


#average(4,6)

average(13,4)



def name(fname,mname = "Jhon", lname="Whatson"):
    print("Hello,",fname,mname,lname)

name("Amy","Agarwal","Jain")




def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is: ",sum /len(numbers))

average(6,65,9,74,34,44,6)