def greet(fx):
    def mfx(*args,**kwargs):
        print("Good Morning")
        fx()
        print("Thanks for usinng this function")
    return mfx
    
@greet
def hello():
    print("hello world")

def sum(a,b):
    return a+b

#greet(hello)()
hello()
print(sum(78,45)) 
# greet(sum(15,45))