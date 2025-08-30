import numpy as np
import matplotlib.pyplot as plt
import pylab


X = np.linspace(0, 10, 40)
print(X)

C = np.cos(X)
S = np.sin(X)
print(C)


plt.figure()
plt.plot(X, C, label='cos')
plt.plot(X, S, label='sin')
plt.xlabel('x')
plt.ylabel('sin(x)/cos(x)')
plt.legend() 
plt.show()






def fibslow(n):
    if n == 0 or n == 1:
        return n
    
    else:
        return fibslow(n-1) + fibslow(n - 2)
    

def fibfast(n):
    if n <= 1: return n

    a, b = 0, 1

    for i in range(1, n):
        a, b = b, a + b

    return a

from_n, to_n = 1, 30

X = range(from_n, to_n)

print(X)


def time_function(fn, start, end):
    from datetime import datetime


    times = []

    for i in range(start, end):
        start_time = datetime.now()

        __ = fn(i)

        end_time = datetime.now()

        time_taken = end_time - start_time
        time_taken = time_taken.microseconds

        times.append(time_taken)

    return times



fibslow_times = time_function(fibslow, from_n, to_n)
fibfast_times = time_function(fibfast, from_n, to_n)

print('slow',fibslow_times)
print('fast',fibfast_times)


# Plot performance comparison
plt.figure()
plt.plot(range(from_n, to_n), fibslow_times, label="fibslow")
plt.plot(range(from_n, to_n), fibfast_times, label="fibfast")
plt.xlabel("n")
plt.ylabel("Time (μs)")
plt.legend()
plt.show()

# it save pic in the same directory
plt.savefig("plot.png")

pylab.figure(1) #create figure 1
pylab.plot([1,2,3,4], [1,7,3,5]) #draw on figure 1
pylab.show() #show figure on screen
pylab.savefig('pylab.png')