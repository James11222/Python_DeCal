""" DEBUGGING DISCUSSION """

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



# PROBLEM 2

""" 
Some people on the internet have run into problems with their code.
It's your job to help them figure it out!

Here is the code:

    1 percentages = [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0]
    2 max_score = 300
    3
    4 scores = [[int(percent * max_score) for percent in percentages]
    5
    6 print('Scores corresponding to the given percentages, on a scale out of 300:')
    7 print(scores)
    
The expected output is:
    Scores corresponding to the given percentages, on a scale out of 300:
    [300, 270, 240, 210, 180, 150, 120, 90, 60, 30, 0]
    
But instead you get:
    File '/Users/yourname/pydecal/scores.py;, line 6
        print('Scores corresponding to the given percentages, on a scale out of 300:')
        ^
    SyntaxError: invalid syntax
"""

# PART 1
""" What line is your error on? """
print("The error is on line: ", "YOUR ANSWER HERE")

# PART 2
""" Rewrite that line to correct the error
    Please keep the code in quotes!"""
print("The line should be: ", "YOUR CODE HERE")


# PROBLEM 3

"""
You wrote some code for class but you have run into an unexpected output.
You are trying to calculate the bmi based on data you have. Somehow, the
calculated BMI always seems to be the same no matter what data you input
into it. Here's what you have:

    1 patients = [[70, 1.8], [80, 1.9], [150, 1.7]]
    2
    3 def calculate_bmi(weight, height):
    4    return weight / (height ** 2)
    5
    6 for patient in patients:
    7    weight, height = patients[0]
    8    bmi = calculate_bmi(height, weight)
    9    print(f'Patient's BMI is: {bmi}')

The output you get is:
    Patient's BMI is: 0.000367
    Patient's BMI is: 0.000367
    Patient's BMI is: 0.000367

Modify the code so that it works as intended.
** Try to only change 2 lines! **
"""

patients = [[70, 1.8], [80, 1.9], [150, 1.7]]

def calculate_bmi(weight, height):
    return weight / (height ** 2)

"YOUR CODE HERE"
