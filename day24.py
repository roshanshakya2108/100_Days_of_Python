tup = (1,2,6,5,6,4,4,8,9,76,44,44,41)
print(type(tup),tup)


tup1 = (1,)
print(type(tup1),tup1)
tup2 = (1)
print(type(tup2),tup2)

print(len(tup))
print(tup[2])


if 76 in tup:
    print("Yes 76 is present in this tuple")



tup3 = tup[1:5]
print(type(tup3),tup3)

print(tup3[0])
print(tup3[-2])