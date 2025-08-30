##----------------------------------------------------
#-------------------- Monte Carlo Simulation ---------
##----------------------------------------------------

# We can do simulation to, well, simulate the real world in low-risk environment. Monte Carlo simulation
# is by far the most widely used simulation and the concept is very simple: try to do something
# n number of times and calculate probabilities of landing in a particular state.

# Examples:
#  - Estimate Pi
#  - Random Walks
#  - Finance: Predicting stocks prices
#  - Aeronautical Engineering: Airflow around the wings
#  - Car Safety: Crash simulations
#  - Medicine: spread of disease and contagions
#  ...

## ----------------------- Estimating Pi ---------------------------
# Area of circle is given as: πr²
# So, π is essentially a ratio between the area and the radius square. We can use that to estimate
# the value π using Monte Carlo simulation

# We can simulate through darts and see which ones land within  the circle and which ones land 
# outside it.

# Also, if we throws darts only in the top-right quadrant, it will have the same ratio.

# area(circle) = πr²
# area(circle) = (2r)² = $r²

# So, if we divide the area of circle by the area of square, we get π/4. Multiply by 4 and you get an 
# estimate of value of π.


import random as r
from math import sqrt
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt



def distance(a, b):
    return sqrt(a**2 + b**2)

def estimate_pi(darts):
    inside = 0

    for _ in range(darts):
        x = r.random()
        y = r.random()

        if distance(x, y) < 1.0:
            inside += 1
    
    pi = (inside/ darts) * 4
    return pi

num_sim = int( 1e+6)
pi = estimate_pi(num_sim)
print(pi)

## --------------------------------- Random Walks ---------------------
steps=20000
def get_action():
    return r.choice( [(0, 1), (0, -1), (1, 0), (-1, 0)])

def random_walk(n):
    """ Return path after 'n' block random walk"""
    path = []

    x, y = 0, 0

    for i in range(n):

        (dx, dy)  =  get_action()  # get step deltas

        x = x + dx
        y = y + dy


        path.append( (x, y) )

    
    return path


walk = random_walk(steps)
plt.figure(num=None, figsize=(15, 10))
point_color = list(range(steps))

x_number = [x[0] for x in walk]
y_number = [x[1] for x in walk]


plt.scatter(x_number, y_number, marker='.', s=20, c=point_color)
plt.show()


