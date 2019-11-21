""" 
This file is used for peak-finding algorithms.


"""


import math
import random


def find_peak(a):
    """ The idea of this peak_finder in a array is to find a single peak in
    logarithmic time. """
    ln = len(a)
    if ln == 1:
        return 0
    if ln == 2:
        if a[0] >= a[1]:
            return 0
        return 1

    mid = math.floor(ln/2)

    if a[mid] <= a[mid - 1]:
        return find_peak(a[:mid]) 

    if a[mid] <= a[mid + 1]:
        return find_peak(a[mid:]) + mid

    return mid

arr = [random.randint(1, 50) for x in range(10)]
print(arr)
i = find_peak(arr)
print("Peak {} at index {}\n".format(arr[i], i))



def find_2d_peak(a):
    """ Now, using a 2-D array, find any peak available.
    The idea of this function is to recurse through in O(N) time.

    This function could be perhaps be further optimized by using the 
    find_peak() function located above.
    """
    i = 0 
    j = 0
    left_right = False
    up_down = False
    while not all([left_right, up_down]):   # Terrible programming. Am I right?
        # The idea of this implemention is to follow a direction until you 
        # can no longer turn anywhere else. Most similar to a game of snake.

        left_right = False
        j_peak = horizontal(a, i, j) 
        if j == j_peak:
            left_right = True
        else:
            j = j_peak 

        up_down = False
        i_peak = vertical(a, i, j)
        if i == i_peak:
            up_down = True
        else:
            i = i_peak
            left_right = False

    return(i, j)

def horizontal(a, i, j):
    while j != 0 and a[i][j - 1] > a[i][j]:    
        if j == 1:
            return 0
        j -= 1 

    n = len(a[i]) - 1
    while j != n and a[i][j + 1] > a[i][j]:
        if j == n - 1:
            return n
        j += 1
    return j

def vertical(a, i, j):
    while i != 0 and a[i - 1][j] > a[i][j]:    
        if i == 1:
            return 0
        i -= 1 

    n = len(a) - 1
    while i != n and a[i + 1][j] > a[i][j]:
        if i == n - 1:
            return n
        i += 1

    return i


rows = random.randint(2, 6) 
cols = random.randint(2, 6)
arr_2d = [[random.randint(1, 50) for x in range(rows)] for y in range(cols)]
[print(row) for row in arr_2d]
i, j = find_2d_peak(arr_2d)
print("Peak {} at index {}, {}".format(arr_2d[i][j], i, j))

