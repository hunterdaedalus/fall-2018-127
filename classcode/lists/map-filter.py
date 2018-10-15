def map_sq(l):
    result = []
    for item in l:
        result = result + [item*item]
    return result

def map_inc(l):
    result = []
    for item in l:
        result = result + [item+1]
    return result

def mapsq_while(l):
    result = []
    i = 0
    while i < len(l):
        result.append(l[i]*l[i])
        i = i + 1
    return result
def mapsq_while_side_effect(l):
    i = 0
    while i < len(l):
        l[i] = l[i] * l[i]
        i = i + 1
    return l



def filter_odd(l):
    result = []
    for item in l:
        if item % 2 != 0:
            result.append(item)
    return result


def filter_even(l):
    result = []
    for item in l:
        if item % 2 == 0:
            result.append(item)
    return result

def is_odd(n):
    return n%2==1

def is_even(n):
    return n%2==0

def is_big(n):
    return n>5

def myfilter(predicate,l):
    result=[]
    for item in l:
        if predicate(item):
            result.append(item)
    return result

def mymap(f,l):
    result=[]
    for item in l:
        result.append(f(item))
    return result

def cube(n):
    return n*n*n

def make_upper(w):
    return w[0].upper()+w[1:]

def is_name(word):
    return word[0]==word[0].upper()


l = [1,2,3,4,5,6,5,4,3,2,1]
word_list = ["one","James","superman","Sally","constitution"]

def piglatinify(name):
    name = name.lower()
    first = name[0]
    rest = name[1:]
    if first in "aeiou":
        result = name + "ay"
    else:
        result = rest + first + "ay"
    return result


sentence="when shall we three meet again"
wl = sentence.split()

pl_sencence = " ".join(mymap(piglatinify,sentence.split()))

spacestring = " hello "

