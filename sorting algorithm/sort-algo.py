## ------------------------------- Bubble sort --------------------------------
# Introduction to Sorting:
# Tower of Hanoi is important but important is it teaches u power of recursion.
# So before sorting doing exercise using paper card numbered 0 - 8.
# And Tell the student to sort them.
# And Asked students how they sort.
# Discuss roughly approaches.

# Why Sort krna zarori --> List is an ordered collection, so sometimes ordered according to some rule are usefull. Random ordered usually not such useful.

# students sorting by rollno. or player by ranking, department by performance.

# Always when we process on data we need some order.
# so we using sorting algorithm to sort data. (Asc, dec).



# 1. Bubble Sort:  
# Such a slow and stupid method, nobody does it neither academically nor in practice. Because all world teach it first, I also teach it so you never disappoint.
# You have items. You to take consecutive items, compare, and swap. (Asc, or desc)
# When one element loop over whole array is called pass. and the largest or smallest element is end of the array at the end of first pass.
# This process is repeated throughout the array in passes.
# When in each pass no swap occurs that mean everything is sorted. we use flag for this.
# and It is an iterative algorithm.


def bubble_sort(l):
    n = len(l)
    # print(n)

    # Outer loop, Goes over the  whole thing 'n' times
    # (because each time, one 'highest will have moved to the end)
    for i in range(n):

        #try to bubble the highest one up 
        for j in range(0, (n-i)-1):

            # compare pairs, move higher one up (the highest will always reach the end )
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]

l = [1, 2, 4, 1, 2, 5, 5, 6, 1, 110, 15]
bubble_sort(l)
print(l)


## ----------------------------- Insertion Sort --------------------------------
# Take element and place it into its correct position.
def insertion_sort(l):
    # Go through  all elements (except first).
    # call it 'key'
    # Each time, the key would be 'inserted' in its place
    # At each iteration, stuff less than i would be sorted already

    for i in range(1, len(l)):
        key = l[i]      # hold this key

        # start comparing keys to things on its left!
        # stop when less or equal value found (or we reach and)

        j = i-1
        while j >= 0 and key < l[j]:
            l[j+1] = l[j]           # move this to right. Slot left on j
            j-=1

 
        l[j+1] = key # Place key in free slot .. ( j+1 we decrement j above)


l = [1, 2, 4, 1, 2, 5, 5, 6, 1, 110, 15]
insertion_sort(l)
print(l)







## ----------------------------- Selection sort --------------------------------
def selection_sort(l):
    """Assumes that L is a list of elements that can be 
            compared using >.
        Sorts L in ascending order"""
    n = len(l)
    for i in range(n):
        min_idx = i

        for j in range(i+1, n):

            if l[j] < l[min_idx]:
                min_idx = j

        l[i], l[min_idx] = l[min_idx], l[i]


l = [3,5,4,1,2]
selection_sort(l)
print(l)


## ---------------------------------------- Quick Sort ----------------------------------
import random

def qsort(l, fst, lst):
    # base case
    if fst >= lst: return

    i, j = fst, lst
    pivot = l[random.randint(fst, lst)]

    while i <= j:
        while l[i] < pivot: i += 1
        while l[j] > pivot: j -=1

        if i <= j: 
            l[i], l[j] = l[j], l[i]
            i, j = i + 1, j - 1
    
    qsort(l, fst, j)
    qsort(l, i, lst)

l = [1, 2, 4, 1, 2, 5, 5, 6, 1, 110, 15]
qsort(l, 0, len(l) - 1)
print(l)


## ---------------------------------------- Merge Sort ----------------------------------

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








## ----------------------------------------Tim Sort -------------------------------------
# TimSort Implementation in Python
# Why because insertion sort is good for small data o(n) but  on large data the worst case is o(n^2)
# And merge is good but the space complexity is high bcz it stops spliting array until one element is left. So much space is used in recursive calls
# So Tim bring the benefit of both world 
# So his algo divide 32 or 64 len array bcz in practical it number for insertion sort to sort the array in 0(n) time complexity
# And Sorting it merge these array using merge sort 
# Tim calls these splits arrays Runs




# Run size (Python internally chooses dynamically, but we fix it for simplicity)
MIN_RUN = 32

def insertion_sort(arr, left, right):
    """Sorts the subarray arr[left:right+1] using insertion sort."""
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge(arr, l, m, r):
    """Merges two sorted halves arr[l:m+1] and arr[m+1:r+1]."""
    left = arr[l:m+1]
    right = arr[m+1:r+1]

    i = j = 0
    k = l

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

def tim_sort(arr):
    n = len(arr)

    # Step 1: Sort individual subarrays of size MIN_RUN using insertion sort
    for start in range(0, n, MIN_RUN):
        end = min(start + MIN_RUN - 1, n - 1)
        insertion_sort(arr, start, end)

    print("After Insertion Sort:",arr)

    # Step 2: Merge runs
    size = MIN_RUN
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), n - 1)

            if mid < right:
                merge(arr, left, mid, right)

        size *= 2


# Example usage
if __name__ == "__main__":
    arr = [5, 21, 7, 23, 19, 10, 3, 8, 15, 1]
    print("Original array:", arr)
    tim_sort(arr)
    print("Sorted array:", arr)

