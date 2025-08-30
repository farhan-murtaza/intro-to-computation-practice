# Sorting in the Real World

# Descending Sorts

## ----------------------------- Selection sort --------------------------------
def selection_sort(l):
    n = len(l)
    for i in range(n):
        min_idx = i

        for j in range(i+1, n):

            if l[j] > l[min_idx]:
                min_idx = j

        l[i], l[min_idx] = l[min_idx], l[i]


l = [3,5,4,1,2]
selection_sort(l)
print(l)

# What is the problem, this is the function that you have already written, we use it as a box, when try to sort 
# Ascending order I do two things:
# 1. I need to break the abstraction and change greater than sign to less than 
# 2. or I need to write the same version of this code for Ascending version 


# We avoid both of them 
# we use better way
# we put comparison in the interface and take as input from user 


def less_than(a, b):
    return a < b;



def selection_sort(l, compare_with):
    n = len(l)
    for i in range(n):
        min_idx = i

        for j in range(i+1, n):

            if compare_with(l[j], l[min_idx]):      # now the comparison is out-source
                min_idx = j

        l[i], l[min_idx] = l[min_idx], l[i]

l = [1, 2, 4, 1, 2, 5, 5, 6, 1, 110, 15]
selection_sort(l, less_than)
print(l)

def greater_than(a, b):
    return a > b

l = [1, 2, 4, 1, 2, 5, 5, 6, 1, 110, 15]
selection_sort(l, greater_than)
print(l)


## ------------------------------ Taking it further ----------------------------------
# Now we can do all sorts of stuff with this without making a single change to our selection sort code.

all_tuples = [
    (24, 25),
    (1, 2),
    (2, 4),
    (3, 5)
]

def tuples_less_than(a, b):
   return sum(a) < sum(b)

def tuples_greater_than(a, b):
   return sum(a) > sum(b)

print("Ascending:\t", end="")
selection_sort(all_tuples, tuples_less_than)
print(all_tuples)

print("Descending:\t", end="")
selection_sort(all_tuples, tuples_greater_than)
print(all_tuples)



# Sorting in Python 

# If you have a list of dictionaries--each represent a student, for intance.

d = [
    { 'name': 'khalid', 'age': 5},
    { 'name': 'usman', 'age': 7},
    { 'name': 'ali', 'age': 12},
    { 'name': 'farooq', 'age': 3},

]

def student_age(a):
    return a['age'] 

print(d)
d.sort(key=student_age)
print(d)
d.sort(key=student_age, reverse=True)
print(d)

## Sorting Objects of Custom Classes

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return self.name + ":" + str(self.age)

s1 = Student('Wajid',5)
s2 = Student('Usman',7)
s3 = Student('Ali',3)

s = [s1, s2, s3]

# You don't even have give the function a name -- just use an anonymous function like so:

for i in s:
    print(i)

s.sort(key=lambda x: x.age, reverse=True)        # reverse

for i in s:
    print(i)


# functional programming 
# map 
# filter
# reduce 
# apply

# Elixir



