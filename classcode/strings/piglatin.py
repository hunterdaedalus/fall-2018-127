def piglatin_simple(name):
    first = name[0]
    rest = name[1:]
    result = rest + first + "ay"
    return result

def piglatinify_verbose(name):
    name = name.lower()
    first = name[0]
    rest = name[1:]
    if first == "a"  or first == "e" or\
       first == "i" or first == "o" or first == "u":
        result = name + "ay"
    else:
        result = rest + first + "ay"
    return result

def piglatinify(name):
    name = name.lower()
    first = name[0]
    rest = name[1:]
    if first in "aeiou":
        result = name + "ay"
    else:
        result = rest + first + "ay"
    return result


print(piglatinify("hello"))
print(piglatinify("able"))
    