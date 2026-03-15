for i in [0, 1, 2, 3, 4]:  # keeps the list in memory
    print(i)              # process each item

for i in range(5):      # does not generate all five elements in memory!
    print(i)            # process each item


# range(5)   # NOT a list but a generator-like object

def myrange(n):
    x = 0
    while x < n:
        yield x    # 'yield' turns a function into a generator
        x += 1

print(type(myrange(5)))  # generator object


for i in myrange(5):
    print(i)              # process each item


def countdown(n):
    while n > 0:
        print("Computing next number ...")
        yield n
        n -= 1
    print("Done!")

for i in countdown(5):
    print(i)

v = countdown(5)
print(next(v))  # Counting down from 5 \n 5


import random 

def random_gen(low, high, num):
    i = 0
    while i < num:
        yield random.randrange(low, high)
        i += 1

r = random_gen(0, 100, 5)

print(r)
for i in r:
    print(i)

def random_gen_inf(low, high):
    while True:
        yield random.randrange(low, high)

r = random_gen_inf(0, 100)
print("----------------")
print(next(r))



# Generator Syntax
import time
start = time.time()
v = [i**2 for i in range(10000000)]
print("Computed", len(v), "items in", time.time() - start, "seconds")

print(type(v))


import time
start = time.time()
g = (i**2 for i in range(10000000))
print("Computed", len(v), "items in", time.time() - start, "seconds")
print(type(g))



# Real World Example 
wwwlog = open("access-log")
for line in wwwlog:
    print(line)
    break

start = time.time()
wwwlog = open("access-log")
total = 0

for line in wwwlog:
    bytestr = line.rsplit(None, 1)[1]
    if bytestr != '-':
        total += int(bytestr)

print("Total bytes:", total)
print("Computed", len(v), "items in", time.time() - start, "seconds")



# The generator version
start = time.time()

wwwlog = open("access-log")

bytecolumn      = (line.rsplit(None, 1)[1] for line in wwwlog)
bytes           = (int(x) for x in bytecolumn if x != '-')

total = sum(bytes)
print("Total bytes:", total)
print("Computed", len(v), "items in", time.time() - start, "seconds")


# Tailing a File 
import time
def follow(thefile):
    thefile.seek(0,2)  # Go to the end of the file
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)  # Sleep briefly
            continue
        yield line

logfile = open("test-log")

loglines = follow(logfile)

print(type(loglines))

for line in loglines:
    print(line, )

    if line[:1] == ".":
        break