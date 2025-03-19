class Person:
    name = "Roshan"
    occupation = "DS"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person()
a.name = "Shubham"
a.occupation = "Accountant"

b= Person()
b.name = "Parvati"
b.occupation = "Developer"

c= Person()
a.info()
b.info()
c.info()

# print(a.name, a.occupation)    