# pro-grammers often increase the conceptual complexity of a program in an effort to
# reduce its computational complexity

def f(i):
    """Assumes i is an int and i>=0"""
    answer = 1
    while i >= 1:
        answer *= i
        i -= 1
    return answer

def f(x):
    """Assume x is an int > 0"""
    ans = 0
    #Loop that takes constant time
    for i in range(1000):
        ans += 1
    print('Number of additions so far', ans)
    #Loop that takes time x
    for i in range(x):
        ans += 1
    print('Number of additions so far', ans)
    #Nested loops take time x**2
    for i in range(x):
        for j in range(x):
            ans += 1
        ans += 1
    print('Number of additions so far', ans)
    return ans
# 1000 + x + 2x^2.
f(10)



# O(log(n))

def intToStr(i):
    """Assumes i is a nonnegative int
    Returns a decimal string representation of i"""
    digits = '0123456789'
    if i == 0:
        return '0'
    result = ''
    while i > 0:
        result = digits[i%10] + result
        i = i//10
    return result

# O(n)

def factorial(x):
    """Assumes that x is a positive int
    Returns x!"""
    if x == 1:
        return 1
    else:
        return x*factorial(x-1)
    

# O(n**2)

def isSubset(L1, L2):
    """Assumes L1 and L2 are lists.
    Returns True if each element in L1 is also in L2
    and False otherwise."""
    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True
                break
        if not matched:
            return False
    return True


# Exponential Complexity
def getBinaryRep(n, numDigits):
    """Assumes n and numDigits are non-negative ints
    Returns a str of length numDigits that is a binary
    representation of n"""
    result = ''
    while n > 0:
        result = str(n%2) + result
        n = n//2
    if len(result) > numDigits:
        raise ValueError('not enough digits')
    for i in range(numDigits - len(result)):
        result = '0' + result
    return result

def genPowerset(L):
    """Assumes L is a list
    Returns a list of lists that contains all possible
    combinations of the elements of L. E.g., if
    L is [1, 2] it will return a list with elements
    [], [1], [2], and [1,2]."""
    powerset = []
    for i in range(0, 2**len(L)):
        binStr = getBinaryRep(i, len(L))
        print('i =', i, 'binStr =', binStr)
        subset = []
        for j in range(len(L)):
            print('j =', j, 'binStr[j] =', binStr[j])
            if binStr[j] == '1':
                subset.append(L[j])
        print('subset =', subset)
        powerset.append(subset)
    return powerset

print(genPowerset([1, 2, 3]))