t = (4,49,94,6,7,46,14,4,45,4,5)
print(t)

temp = list(t)
temp.append(150)
print(temp)
temp.pop(2)
print(temp)

t1 = tuple(temp)
print(t1)

print(t.count(3))
print(t.index(46))
print(t.index(46,4,7))