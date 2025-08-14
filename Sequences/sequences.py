# Sequences are very useful in Python, and they can be lists, tuples, or strings.
# They allow you to store multiple items in a single variable.
# Here is an example of a list, which is a type of sequence in Python.



# Lists are mutable, meaning you can change their content after creation.
# You can add, remove, or change items in a list.

digits = [ 1, 8, 2, 9 ]

print(len(digits))  
print(digits[0])  # Accessing the first element

print(1 in digits)  # Checking if 1 is in the list
print(digits[0:2])

def make_tea(ing):
    for i in ing:
        print("Put", i, "in.")


ingredients = ['tea', 'milk', 'sugar']
make_tea(ingredients)  # Calling the function with a list of ingredients



pairs = [[1, 2], [3, 4], [5, 6]]
for x, y in pairs:
    print("x:", x, "y:", y)


a = [1, 2, 3]
a.append(4)
a.remove(2)
a.reverse()
print(a)
a.sort(reverse=True)
print(a)



# strings are also sequences but immutable
# You cannot change a string after it is created, but you can create a new one.
s = "I am a dummy string. Lorem ipsum dolor sit amet. "
print(len(s))
print(s[2:8])
print(s.rstrip())  # Remove trailing whitespace



# Ranges are also a type of sequence, often used in loops.
for i in range(1, 3):
    print(2, "x", i, "=", 2 * i)




# List comprehensions provide a concise way to create lists.
squares = [x**2 for x in range(10)]
print(squares)

print([x for x in range(1, 12+1) if 12 % x == 0])  



# Tuples are immutable sequences, meaning once created, they cannot be changed.
t = (1, 2, 3)
print(t[0])
print(t[1:3])  # Slicing a tuple
print(t.index(3))  # Finding the index of an element in a tuple
print(t.count(1))  # Counting occurrences of an element in a tuple