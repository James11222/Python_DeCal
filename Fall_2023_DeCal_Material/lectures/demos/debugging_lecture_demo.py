# show how to add docstrings and use them to help solve the issue
def add(x, y):
    # add 2 doctests to test
    return x - y # should be x + y

# show how to use print statements
def factLoop(n):
    """
    Uses a loop to return a factorial of n but returns 0 instead :(
    >>> factLoop(3)
    6
    """
    total = 1
    for i in range(n): # should be 1, n
        # print what i is
        total *= i
    return total


# unexpected output example
def eachDigit(num):
    """
    Uses a loop to print out each digit in num but it prints zero forever
    (there's a catch: i accidentally forgot to reassign num so it prints 
    out 5 forever - see if students can catch that)
    What we want:
    >>> eachDigit(12345)
    5
    4
    3
    2
    1
    """
    while num >= 0: # should be > 0
        currDigit = num % 10
        print(currDigit)
        # reassign num to num \\ 10