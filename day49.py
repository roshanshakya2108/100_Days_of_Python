# f  = open('myfile.txt','r')
# print(f)
# text = f.read()
# print(text)
# f.close


# e  = open('myfile2.txt','w')
# e.write("Hii, How are you?")
# e.close


with open('myfile','a') as f:
    f.write("Adding this string.")
    
