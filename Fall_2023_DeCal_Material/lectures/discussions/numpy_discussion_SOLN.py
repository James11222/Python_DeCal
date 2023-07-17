import numpy as np

# PROBLEM 1

"""
    Make a function that takes in an array. Reshape the array 
    so that it becomes a square matrix. Finally reverse the
    multi-dimensional array and return it.
"""

def reverseArray(arr):
    """
    >>> myArr = np.random.random(16)
    >>> reverseArray(myArr)
    array([[0.99145874, 0.25070908, 0.18436908, 0.70286743],
       [0.08599012, 0.33552297, 0.61514196, 0.19393074],
       [0.74513446, 0.90204978, 0.95634375, 0.98563639],
       [0.30663176, 0.03018382, 0.62689752, 0.99972597]])]])

    >>> badLength = np.random.random(6)
    >>> reverseArray(badLength)
    Array length or dimension is not supported. Please try again.

    >>> wrongDim = np.random.random(4)
    >>> reverseArray(np.reshape(wrongDim, (2, 2)))
    Array length or dimension is not supported. Please try again.'
    """
    # if statement can be omitted but it is nice to look out for edge cases
    if round(len(arr)**(1/2))**2 != len(arr) or arr.ndim > 1:
        print('Array length or dimension is not supported. Please try again.')
        return None
    dimension = int(len(arr)**(1/2))
    arr = np.reshape(arr, (dimension, dimension))
    reversed = arr[::-1, ::-1]
    return reversed



# PROBLEM 2: NO FAKES HERE

"""
    Given an array, return its sorted version with only the unique 
    elements, along with the count for each value.

    P.S. There is an easy way and a hard way xp
"""

def uniqueCounts(myArr):
    """
    >>> arr = np.array([10, 2, 5, 10, 8, 2, 8, 9])
    >>> uniqueCounts(arr)
    (array([ 2, 5,  8,  9, 10]), array([2, 1, 2, 1, 2]))
    """
    unique, frequency = np.unique(myArr, return_counts = True)
    return unique, frequency



# PROBLEM 3: NO FAKES HERE

"""
    Given an array, replace the values that are less than the mean
    of the array with the mean.
"""

def conditionedArr(myArr):
    """
    >>> newArr = np.array([1, 2, 3, 1, 3])
    >>> conditionedArr(newArr)
    array([2, 2, 3, 2, 3])
    """
    mean = np.mean(myArr)
    myArr[myArr < mean] = mean
    return myArr



# PROBLEM 4: WHERE IS YOUR PLACE IN LIFE?

"""
    You are given a sorted array and an input or multiple inputs. 
    Your job is to find the index or indices where you could
    place the input so that the array is still sorted.
"""

def sortAndInsert(arr, inputVal):
    """
    >>> sortArr = [1, 2, 3, 4, 7]
    >>> sortAndInsert(sortArr, 5)
    4

    >>> sortedArr = [1, 3, 7, 20, 32]
    >>> sortAndInsert(sortArr, [5, 18, 24, 26])
    array([4, 5, 5, 5])
    """
    if np.sort(arr) != arr:
        arr = np.sort(arr)
    return np.searchsorted(arr, inputVal) 