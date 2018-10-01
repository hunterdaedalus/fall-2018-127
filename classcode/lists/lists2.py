
import random

def build_random_list(items, max_value):
    """
    create and return a list filled with items number of element
    each element should be a random integer value
    between 0 and 99
    """
    l=[]
    # your code here
    i = 0
    while i < items:
        #l.append(random.randrange(0,max_value))
        l = l + [ random.randrange(0,max_value) ]
        i = i + 1
        
    return l

l = build_random_list(15,100)
print(l)
l2 = build_random_list(8,1000)
print(l2)