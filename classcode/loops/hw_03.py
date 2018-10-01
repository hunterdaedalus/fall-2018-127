# HW 3 solutions

def collatz(n):
    """
    if n = 1 stop
    otherwise
    if n is odd --> 3n+1
    if n is even --> n/2
    until n becomes 
    """
    i = 0
    while n != 1:
        print(n)
        if n % 2 == 0: # even 
            n = n / 2
        else: # odd
            n = 3 * n + 1
        i = i + 1
    print(n)
    return i
    
    
# print("Count for 5: ",collatz(5))

def calc_new_guess(n,oldguess):
    newguess = (oldguess + ( n / oldguess)) / 2
    return newguess

def mysqrt(n):
    guess = 1
    while abs((guess * guess) - n) > 0.000001:
        guess = calc_new_guess(n,guess)
    return guess

i = 1
while i <= 25:
    print(i," : ",mysqrt(i))
    i = i + 1