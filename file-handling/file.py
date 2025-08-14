import os


directory = 'res'
name = 'dummy.txt' 

# different operating systems may use different path separators
# such as window use '\' and linux use '/'
# so we use os.path.join to create a path that works on all systems

filename = os.path.join(directory, name)

print(filename)



# open the file in read mode
fileHandler = open(filename, 'r')

for line in fileHandler:
    print(line.strip())  # rstrip() removes the trailing newline character

fileHandler.close()  # never forget to close the file!

# Python know people are lazy, so python give us context manager to handle files and automatically close them and house keeping 
with open(filename, 'r') as fileHandler:
    for line in fileHandler:
        print(line.strip())   


with open(filename, 'r') as f:
    print(f.read())            # the whole file 

l = []

with open(filename, 'r') as f:
    l = f.read().split('\n')

print(l)

out_name = 'dummy-out.txt'
out_filename = os.path.join(directory, out_name)
with open(out_filename, 'a') as f:
    f.write("Two ...\n")