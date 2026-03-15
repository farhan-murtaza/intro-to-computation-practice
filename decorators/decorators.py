def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-2) + fib(n-1)
    

print(fib(10))

# time taken by fib
import time
start_time = time.time()
fib(35)
end_time = time.time()
print("Time taken by fib 35):", end_time - start_time)

# start_time = time.time()
# fib(50)
# end_time = time.time()
# print("Time taken by fib(50):", end_time - start_time)


# This is a naive implementation of Fibonacci sequence calculation. It has exponential time complexity due to repeated calculations of the same Fibonacci numbers.
# We can use the concept of higher-order functions and decorators to tackle this issue.

def logger(f):

    # f will be "remembered" by the wrapper even after we exit logger.
    # This is the concept of closure in Python.

    def wrapper(n):
        print("I'm going to call a function")
        v = f(n)
        print("The function returned: ", v)
        return v
    return wrapper


logged_fib = logger(fib)    # remember, fib is just a name
  
print(logged_fib(1))


# Now that we can do stuff before the fib call, let's see if we can save some values that are repeatedly needed.

def memoize(f):
    mem = {}

    def memoized_func(n):
        if n not in mem:
            mem[n] = f(n)
        return mem[n]
    
    return memoized_func


@memoize                        # this is called "decorator", EQUALS: fib = memoize(fib)
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-2) + fib(n-1)
    



start_time = time.time()
# fib = memoize(fib)
fib(100)
end_time = time.time()
print("Time taken by fib(100):", end_time - start_time)

