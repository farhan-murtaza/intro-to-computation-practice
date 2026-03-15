x = 24
def square(n):
    return n * n

print(square(6))

print(square)

f = square

print(f)

print(f(6))


def summation(low, high):
    total = 0
    for i in range(low, high + 1):
        val = i ** 2
        total += val 
    return total

print(summation(1, 3))


# Now, if I ask you to write a function that does this
def summation(low, high):
    total = 0
    for i in range(low, high + 1):
        val = i ** 3
        total += val 
    return total
print(summation(1, 3))


# But what's the difference? Only the val has changed. Can't we just write one function and have you decide how val needs to be calculated?
def summation(low, high, func):
    total = 0
    for i in range(low, high + 1):
        val = func(i)
        total += val 

    return total

print(summation(1, 3, square))  # sum of squares
# This is an anonymous function (a function without a name)
print(summation(1, 3, lambda n: n ** 3))  # sum of cubes