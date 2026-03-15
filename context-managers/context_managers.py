# You've probably already worked with opening and closing files.

f = open("dummy-file.txt", "r")
for line in f:
    print(line)

f.close()           # People will always forget this!

with open("dummy-file.txt", "r") as f:
    for line in f:
        print(line)


# The 'with' statement automatically takes care of closing the file for you,
# The keyword with marks a context. We can define our own context managers as well.
# The idea to create a context that requires some setup before starting and then some cleanup at the end.

import time

def some_heavy_computation():
    time.sleep(1)

start_time = int(round(time.time() * 1000))

some_heavy_computation()

end_time = int(round(time.time() * 1000))

elapsed_time = end_time - start_time

print("Code took %d ms to run." % elapsed_time)



# Fairly simple but it's making our code look ugly and is a hassle Let's do this using a context manager.
# It matches the pattern after all:
# . Do something at startup(Record start time)
# . Perform some (unspecified ) work,
# . Do something at end (Report time elapsed)


from contextlib import contextmanager

@contextmanager
def timeit():
    start_time = int(round(time.time() * 1000))
    yield       # Remember this guy from the generators lecture?
    end_time = int(round(time.time() * 1000))
    elapsed_time = end_time - start_time
    print("Code took %d ms to run." % elapsed_time)


with timeit():
    some_heavy_computation()


def another_function():
    time.sleep(0.5)

with timeit():
    another_function()


# Clean code, saves time!


# Case Study: Temporary Directories
# It's common to create temporary directories for files and delete them after you're done with them.

import tempfile
import shutil
import os

try:
    name = tempfile.mkdtemp()
    print("Created temporary directory ", name)

    filename = os.path.join(name, 'somefile.txt')

    # Do some processing 
    with open(filename, 'w') as f:
        print("Opened file: %s" % filename)
        f.write("Dummy text\n")

finally:
     print("Deleting directory: %s" % name)
     shutil.rmtree(name)




