# this is a new file - this is a comment

# def identifier(params):
def add_one(x):
    """
    this is a docstring that can
    describe the function"""
    #a = x
    #print("You sent in ",a)
    #a = a + 1
    # print("Now x is ",a)
    #a = a + 1
    x = x + 1
    return x

def sub_two(a,b):
    return a-b

def greeter(name):
    """
    greeter("Steve") --> "Hello Steve!")
    greeter("Dana") --> "Hello Dana!")
    """
    result = "Hello " + name + "!"
    return result

def greeter2(name,greeting):
    return greeting+" "+name+"!"

print(greeter("Steve"))
print(greeter2("Bob","Welcome"))
s = greeter2("Sam","Howdy")
print(s)
s = greeter2(s,"huh")
print(s)


    

a = 20
print(a)
a = add_one(a)
print(a)


    
print("This line isn't indented anymore")


