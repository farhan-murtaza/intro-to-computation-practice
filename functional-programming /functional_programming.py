# Functional Programming is a different paradigm.
# The idea is to treat all computations as mathematical functions -- no side effects.

    # - Easier to predict outputs from inputs
    # - Easier to debug
    # - Easier to parallelize

# Map 
from math import sqrt
s = [sqrt(i) for i in [1, 4, 9, 16]]
print("simeple version", s)

# Map applies a unary function to each element in the sequence and returns a new sequence 
# containing the results, in the same order.
s_map = list(map(sqrt, [1, 4, 9, 16]))
print("map version", s_map)


def mymap(f, seq):
    result = []
    for x in seq:
        result.append(f(x))
    return result
s_mymap = mymap(sqrt, [1, 4, 9, 16])
print("mymap version", s_mymap)

def powOfTwo(x):
    return x ** 2

squared = list(map(powOfTwo, [1, 2, 3, 4, 5]))
print("squared using map and powOfTwo function", squared)
print(list(map(lambda k: 2**k, [1, 2, 3, 4, 5])))  # using lambda function



# Filter

x = filter(str.isalpha, ['x', '1', 'y', '2', 'z', '3'])
print("filter only alphabetic characters", list(x))


# Reduce
from functools import reduce
def add(x, y):
    return x + y
sum = reduce(add, [1, 2, 3], 0)
print("sum using reduce and add function", sum)



# But Why?
lines = [
    "A cow is a domestic animal. A cow is a very useful animal.",
    "A cow is kept in barns. Cow milk is very healthy.",
]

# Let's count words in all these lines.
from collections import defaultdict

def count_words(s):             # Takes in a single string
    counts = defaultdict(int)   # Initialize keys not already present

    for word in s.split():  # Split string into words
        counts[word] += 1       # Increment count for word

    return dict(counts)     # don't want to send back the defaultdict

print("count words in a single line", count_words(lines[0]))


count_map = list(map(count_words, lines))  # Map count_words to each line

def reduce_counts(x, y):
    print("x: ", x)
    print("y: ", y)
    print("---")
    return {'word': 0}


total_counts = reduce(reduce_counts, count_map, {})


from collections import Counter

def reduce_counts(x, y):
    counter = Counter()         

    counter.update(x)           # Update numbers with  x
    counter.update(y)           # Update counts with  y

    return dict(counter)  # return a normal dict

total_counts = reduce(reduce_counts, count_map, {})
print("total word counts across all lines", total_counts)



# This makes parallelization easier. That's what MapReduce (and Hadoop/Spark) is built on top of!
# Imagine a scenario where you have 1 billion files and a Hadoop cluster of 5,000 machines.
# - Take a million files and pass to one machine (Since they are independent, no  network overhead)
# - Each machine computes their own sum
# - Add them all together once!
# - Almost 5000x speedup (more if you use threads on one machine)


