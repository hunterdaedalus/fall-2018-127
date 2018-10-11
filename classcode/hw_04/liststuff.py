
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

def locate(l,value):
    i = 0
    found_index = -1
    while i < len(l):
        if l[i] == value:
            found_index = i
            break # breaks out of the current loop
        i=i+1
    return found_index
def locate_for (l,value):
    
    found_index = -1
    for i in range(len(l)):
        if l[i] == value:
            found_index = i
            break # breaks out of the current loop
        
    return found_index

def locate2(l,value):
    if value in l:
        return l.index(value)
    else:
        return -1

def count(l,value):
    i = 0
    found_count = 0
    while i < len(l):
        if l[i] == value:
            found_count = found_count + 1
        i=i+1
    
    return found_count

def reverse(l):
    reversed = []
    i = len(l)-1
    while i >= 0:
        reversed.append(l[i])
        i -= 1
    return reversed

def reverse_for(l):
    reversed = []
    for i in range(len(l)-1,-1,-1):
        reversed.append(l[i])
        
    return reversed

def isPalindrome(l):
    l2 = reverse(l)
    return l == l2

def isIncreasing(l):
    increasing = True
    i = 0
    while i < len(l)-1:
        if l[i] >= l[i+1]:
            increasing = False
            break
        i = i + 1
    return increasing


l = build_random_list(15,100)
l2 = build_random_list(200,50)
#print(l)
#print(locate(l,10))
#print(locate(l,l[4]))
#print(locate2(l,10))
#print(locate2(l,l[4]))
#print(count(l2,l2[4]))
print(l)
print(reverse(l))
