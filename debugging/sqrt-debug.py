def sqrt(x, guess = 1.0):
    if x < 0:
        raise ValueError
    

    if good_enough(guess, x):
        return guess
    else:
        new_guess = improve_guess(guess, x)
        return  sqrt(x, new_guess)
    

def good_enough(guess, x):
    if  abs(guess * guess - x) < 0.1:
        return True
    else: 
        return False
    

def avg(a, b):
    return (a+b)/2.0


def improve_guess(guess, x):
    new_guess = avg(guess, x/guess)
    return new_guess 


print(sqrt(36))
