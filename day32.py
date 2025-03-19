s = {5,7,9,1,7,9,5,5,6,5,4,6,4,5,7,5,4,8,4,5,4}
print(s)
r = {1,5,2,3,4,6,7,9,4,1,2,6,45,6,91,51,94,4}
print(r)

print(s.union(r))

s.update(r)
print(s,r)

q = s.intersection(r)
print(q)

e = {15,4,64,64,1,8,34,5,2,4}
w = {26,6,4,1,48,484,51,1,21,61}
t = e.intersection_update(w)
print(t)