l = [5,8,59,4,1,4,1,]
p=[2626,595,626,262,5444,7,8,4,101,5]
print(l,p)

l.append(7)
print(l)
p.sort()
print(p)

l.reverse()
print(l)

print(l.index(4))
print(l.count(485))

m = l.copy()
m[0] = 15
print(m)

l.insert(2,454989)
print(l)


n = [900,8000,10000,11000,400]
l.extend(n)
print(l)

q = l + n + m