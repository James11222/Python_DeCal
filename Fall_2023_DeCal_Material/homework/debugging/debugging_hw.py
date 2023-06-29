# DEBUGGING HOMEWORK

""" Most of this homework is taken from or inspired by the CS61A 
    debugging practice worksheet from Spring 2022 """

# PROBLEM 1
""" You're writing your own implementation of the map function which 
takes in a one-argument function and applies it to every element in a list
and returns a new list. However, you are running into some bugs.

The is what you expect to happen:
>>> def double(x):
        return x*2
>>> lst = [1, 2, 3]
>>> my_map(double, lst)
[2, 4, 6]

This is the code you've written so far:
    1 def my_map(func, seq):
    2   res = []
    3   for i in seq:
    4       curr = func(seq[i])
    5       res.append(curr)
    6   return res
    
This is the error you get:
    >>> my_map(double, lst)
    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        File "/Users/yourname/pydecal/my_map.py", line 4, in my_map
            curr = func(seq[i])
    IndexError: list index out of range"""

 # PART 1
""" What line is your error on? """
print("The error is on line: ", "YOUR ANSWER HERE")

# PART 2
""" Rewrite that line to correct the error
    Please keep the code in quotes!"""
print("The line should be: ", "YOUR CODE HERE")