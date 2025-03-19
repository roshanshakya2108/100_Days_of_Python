# for i in range(11):
#     print("5 X",i+1, "=", 5*(i+1))


#break

for i in range(11):
    if(i ==10):
        break
    print("5 X",i+1, "=", 5*(i+1))


#continue
for i in range(15):
    if(i ==10):
        print("Skip this iteration")
        continue
    print("5 X",i+1, "=", 5*(i+1))



##################

i = 0
while True:
    print(i)
    i = i + 1
    if(i%100 ==0):
        break