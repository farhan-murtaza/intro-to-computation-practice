import time
def fib(n):
    """Assumes n is a non-negative integer
    Returns Fibonacci of n"""
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
    
start = time.perf_counter()
print(fib(40))
end = time.perf_counter()
print('Time taken for recursive Fibonacci:', end - start, 'seconds')


# the above aproch is not efficient for large n
# we can use iterative approach
def fib_iterative(n):
    """Assumes n is a non-negative integer
    Returns Fibonacci of n"""
    if n <= 1:
        return n
     
    a, b = 0, 1

    for _ in range(1, n + 1):
        a, b = b, a + b

    return a


start = time.perf_counter()
print(fib_iterative(40))
end = time.perf_counter()
print('Time taken for iterative Fibonacci:', end - start, 'seconds')
