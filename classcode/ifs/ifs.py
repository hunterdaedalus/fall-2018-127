import random


print("This is before the if / conditional")

if True:
    print("This always executes")
    print("Multiple lines can execute if the boolean condition")
    print("is True as long as they're all indented the same")
    
print("This is outside of all the if statements")


if False:
    print("This never executes")
   
if 5 > 3:
    print("the above boolean is true")

if 5 == 5 :
    print("Hello")

name="Joe"
if name.upper()=="joe".upper():
    print("Hi Joe")
    
  
TF = False  
if TF==False:
    print("this can be tricky")
 
name="Joe"
age=20
if name=="Joe" and age > 18:
    print("It's Joe and he's over 18")
  
  
number = random.randrange(10)
print("Number = ",number)
if number >= 5:
    print("Number is greater than 5:",number)
if number < 5:
    print("Number is less than 5:",number)
    
if number >= 5:
    print("Number is >= than 5 with an else:",number)
else:
    print("Number is less than 5 with an else:",number)
    
if number > 7:
    print("Number > 7",number)
elif number > 4:
    print("Number > 4:",number)
else:
    print("Number <= 4",number)
    
            
print("This is after the if / conditional")
