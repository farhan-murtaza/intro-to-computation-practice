mammals = ['cat', 'kangaroo', 'horse']
fish = ['tuna','shark', 'catfish']

animals = [mammals, fish]
print(animals)

mammals[0] =  'mule'

print('mammals = ', mammals)
print('animals = ', animals)


mammals_2 = mammals
mammals_2[0] = 'dog'


print('mammals_2 = ', mammals_2)
print('mammals = ', mammals)
print('animals = ', animals)

mammals_3 = mammals[:]              # this create a copy!
 

mammals_3[0] = 'mouse'

print('mammals_3 = ', mammals_3)
print('mammals_2 = ', mammals_2)
print('mammals = ', mammals)
print('animals = ', animals)



s1 = ['student 1', 'Ali', 'Khan']
s2 = ['student 2', 'Zia', 'Farooq']
s3 = ['student 3', 'Hadi', 'Zaman']

students = [s1, s2, s3]
print(students)
students_copy = students[:]
print(students_copy)

students_copy[0][0] = 'Student 1 changed'
print(students_copy)
print(students)


# Deep Copying

import copy

students_3 = copy.deepcopy(students)


students_3[0][0] = 'Student 1 changed again'
print(students_3)
print('-------------')
print(students)



# Passing lists as arguments 

def change_var(x):
    x = x + 1

def change_list(lst):
    lst.append(24)

x = 25
change_var(x)
print(x)  # our global x remains the same

print(s2)
change_list(s2)
print(s2)   # but the list is affected!


# Now this should be understanable.

# And that's why we have tuples as immutable .. so that called functions are guaranted to not change them. 