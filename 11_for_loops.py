import string 


# ** For loops **

# In lesson 8 we talked about while loops. While loops kept running until their
# condition evaluated to `False`. Do you remember why this was dangerous? If 
# the condition was never `True`, the while loop could keep running forever! 

# For loops solve this problem! 

# For loops work by "iterating over" every item in a set. This means that they
# run once for every item in a set. After that, they're done. 

# Check out this example
my_list = [1, 2, 3]
for number in my_list: 
    print(number)
# When you run this code, the loop runs three times and then stops! 

# Every time the loop is run, `number` is set equal to the next item in 
# `my_list`. In technical terms, `number` is known as the "iteration variable" 
# and `my_list` is an "iterator". The basic syntax of a for loop is: 
"""
for iteration_variable in iterator: 
    do_something(iteration_variable)
"""

# For loops can loop over several different data types. Let's see some of them
# below.
print()

# ** For loops with lists ** 
print("For loops with lists:")

# The example above is an example of iterating over a list. Here's another:
for num in [1, 2, 3]: 
    print("Twice", num, "is", num*2)
print()

# You can loop over the elements and the indexes of a list at the same time 
# using a function called `enumerate`:
for i, elt in enumerate(["zero", "one", "two"]):
    print("The element at index", i, "is", elt)
print()

# You can also loop over a list backwards! 
for num in reversed([1, 2, 3]):
    print(num)
print()

# ** For loops with strings ** 
print("For loops with strings:")

# Interestingly, you can write a for loop over a string as well. In this case,
# the variable `letter` becomes every letter in the string. 
for letter in "aeiou": 
    print(letter, "is a vowel")
print()

# ** For loops with ranges of numbers ** 
print("For loops with ranges of numbers")

# What if you just want your loop to run a fixed number of times? Python 
# has an easy way of doing that too. 
num_times_to_run = 3
for i in range(num_times_to_run): 
    print("I am running!")
print()
# Note that when looping over numbers, the variable `i` for index is commonly 
# used for the iteration variable

# The Python function `range` creates a sequence of numbers. `range` can be 
# used three different ways.

# 1. If you use range with one argument `end`, it creates a sequence of
# numbers starting at 0 and ending with `end - 1` (ranges, like lists, 
# are 0-indexed--they start with 0, not 1!). As in the example above, this is 
# really useful if you want your loop to run `end` times.  print("Range with end only")
end = 10
for i in range(end):
    print("i is", i)
print()

# 2. If you use range with two arguments, `start` and `end`, it 
# creates a sequence of numbers starting at `start` and ending with
# `end - 1`. The loop runs `end-start` times.
print("Range with start and end")
start = 5
for i in range(start, end):
    print("i is", i)
print()

# 3. If you use range with three arguments, `start`, `end`, and 
#    `step`, then the sequence is every number between `start` and `end-1` 
#    (inclusive) at intervals of `step`. `step` can be negative! 
print("Range with start, end, and step")
step = 2
for i in range(start, end, step): 
    print("i is", i)
print()

# ** Exercises ** 
# 1. Write a for loop that finds the biggest number in this list that is 
#    divisible by 3. 
#    * Question: why are we looping over a list of numbers here instead of 
#      using range? 
print("Exercise 1")
numbers = [1, 5, 6.7, 9, -1, -5, -6, -30, 30]
#Your code here: should print 30 
print()

# 2. Write a for loop that prints out every letter in the alphabet and its 
#    numerical position, like so.
"""
    a: 1
    b: 2
    c: 3
    ...
"""
#    Hint: take a look at the "string constants" on this page
# https://docs.python.org/2/library/string.html#string-constants
print("Exercise 2")
# Your code here. 
print()

# 3. Write a for loop using `range` that prints every odd number between 33 and
#    77, inclusive, in reverse order. 
print("Exercise 3")
# Your code here
print()

# 4. A Caesar cipher, also known as a shift cipher, is a very simple encryption
#    technique. Every letter in the encrypted message is replaced by the letter
#    at a certain shift down the alphabet. For example, with a shift of +3, 
#    A->D, B->E, etc. You can read more here: 
#    https://en.wikipedia.org/wiki/Caesar_cipher
#    Fill in the function `caesar_cipher`, which takes in a message and an
#    integer value to shift and returns the encrypted message.
print("Exercise 4")

def caesar_cipher(message, shift): 
    pass # Your code here

message_to_encrypt = "bet you cant read this"
encrypted_message = caesar_cipher(message_to_encrypt, 3)
expected_message = "ehw brx fdqw uhdg wklv"
print("Expected message:", expected_message)
print("Your message:", encrypted_message)
print("Do they match?", encrypted_message == expected_message)
