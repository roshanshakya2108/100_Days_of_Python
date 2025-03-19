class Person():
    def __init__(self, n, o):
        print("Hey, I am a Person")
        self.name = n
        self.occupation = o

    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person("Roshan", "Developer")        
b = Person("Rohit","Manager")
a.info()
b.info()