s = "Hello World"

# World, Hello World

print("s = " + s) # adding two strings to print using one arg
print("Access the first character: ", s[0]) # printing two separate args using the ,
# s[0]="Z" # this is illegal - you can't change a string

def bondify(name):
    """
    takes in a string in the form "first last" and returns
    it in the form "last, first last"
    """
    space_index = name.find(" ")
    first = name[0:space_index]
    last = name[space_index+1:]
    bond_name = last + ", " + first + " " + last
    return bond_name

def capitalize_name(name):
    """
    name -> a string in the form "first last" all lower case
    returns -> the string with both names capitalized
    ex: capitalize_name("james bond") --> James Bond
    """

print(bondify("Hello World"))
print(bondify("James Bond"))    
