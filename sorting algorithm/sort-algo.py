# Selection sort

def selSort(L):
    """Assumes that L is a list of elements that can be 
            compared using >.
        Sorts L in ascending order"""
    suffixStart = 0
    while suffixStart != len(L):
        #look at each element in suffix
        for i in range(suffixStart, len(L)):
            if L[i] < L[suffixStart]:
                #swap position of elements
                L[suffixStart], L[i] = L[i], L[suffixStart]

        suffixStart +=1


l = [3,5,4,1,2]
selSort(l)
print(l)


# Merge Sort

def merge(left, right, compare):
    """Assume left and right are sorted lists and
            compare defines an ordering on the elements.
        Returns a new sorted (by compare) list containing the 
            same elements as (left + right) would contain."""
    
    result = []

    i, j = 0, 0

    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while ( i < len(left)):
        result.append(left[i])
        i += 1
    
    while ( j < len(right)):
        result.append(right[j])
        j += 1
    return result

    
def mergeSort(L, compare = lambda x, y: x < y):
    """Assumes L is a list, compare defines an ordering 
        on elements of L
        Returns a new sorted list with the same elements as L"""
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left  =mergeSort(L[:middle], compare)
        right = mergeSort(L[middle:], compare) 
        return merge(left, right, compare)
    

l = [3,5,4,1,2]
print(mergeSort(l))


def lastNameFirstName(name1, name2):
    arg1 = name1.split(' ')
    arg2 = name2.split(' ')
    if arg1[1] != arg2[1]:
       return arg1[1] < arg2[1]
    else: #last names the same, sort by first name
        return arg1[0] < arg2[0]
def firstNameLastName(name1, name2):
    arg1 = name1.split(' ')
    arg2 = name2.split(' ')
    if arg1[0] != arg2[0]:
        return arg1[0] < arg2[0]
    else: #first names the same, sort by last name
        return arg1[1] < arg2[1]
L = ['Tom Brady', 'Eric Grimson', 'Gisele Bundchen']
newL = mergeSort(L, lastNameFirstName)
print('Sorted by last name =', newL)
newL = mergeSort(L, firstNameLastName)
print('Sorted by first name =', newL)


# As mentioned earlier, the Python method list.sort takes a list as its first ar-
# gument and modifies that list. In contrast, the Python function sorted takes an
# iterable object (e.g., a list or a view) as its first argument and returns a new sorted
# list. For example, the code

L = [3,5,2]
D = {'a':12, 'c':5, 'b':'dog'}
print(sorted(L))
print(L)
L.sort()
print(L)
print(sorted(D))
# D.sort()            #AttributeError: 'dict' object has no attribute 'sort'

L = [[1,2,3], (3,2,1,0), 'abc']
print(sorted(L, key = len, reverse = True))