# exception


def div(num, den):
    return num / float(den)

try:
    print('Div 4 by 2 is:', div(4, 2))
    print('Div 4 by 0 is:', div(4, 0))

except ZeroDivisionError:
    print('Do not ask me to divide by 0 please.')

print("done")


# Exception hierarchy

try:
    print('Div 4 by 2 is:', div(4, 2))
    v
except ZeroDivisionError:
    print('Do not ask me to divide by 0 please.')
except NameError:
    print('That\'s a bad name')

try:
    print('Div 4 by 2 is:', div(4, 0))
    v
except Exception:
    print('No idea what went wrong!')       # hence, don't do this



def sqrt(x, guess =  1.0):
    """Calculate square root of a positive number.
        Return a ValueError if a negative number is passed to it. """
    if x < 0:
        raise ValueError("Cannot find square root of negative numbers")

    # calculate square root and return value
    return 6


try:
    print(sqrt(-2))
except:
    print('Tried to find square root of negative number')