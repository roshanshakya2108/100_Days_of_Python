def cube(x):
    return x*x*x

print(cube(3))

l = [1,2,3,4,5,6]
newl = []
for item in l:
    newl.append(cube(item))
print(newl)


#Map 

newl = list(map(cube,l))
print(newl)


sq = list(map(lambda x: x**2,l))
print(sq)

#filter
def filter_fun(a):
    return a>4
newnewl = list(filter(filter_fun,l))
print(newnewl)


#Reduce


from functools import reduce

num = [1,2,3,4,5,6]

def mysum(x,y):
    return x+y

sum = reduce(mysum,num)
print(sum)