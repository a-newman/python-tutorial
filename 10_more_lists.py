# ** Strings as lists ** 

# You guys are already pretty familiar with strings. But it might surprise you 
# to learn that strings are basically a special kind of list that only holds
# characters! 

# You can do a lot of the same things to strings as you can to lists. For
# instance, you can index into strings. 
s = "Hello, world!"
print("s[0]:", s[0])

# You can find the length 
print("len(s):", len(s))

# You can slice 
print("s[7:]:", s[7:-1])

# You can easily transform a string into a list of characters
print("s as a list:", list(s))

# One thing that strings cannot support is changing individual characters. 
# In fact, once you have created a string, you can't modify it at all. 
# The ability to modify an object after it has been created is known as 
# "mutability", and we will learn more about it in the next section. 

# This line is illegal!!!
#s[0] = "h"

print()

# ** Methods and Lists ** 
print("Methods and Lists:")

# In Python, any piece of data of any type (including ints, floats, strings,
# and lists) is known as an object. 

# Objects contain special functions known as methods. A method is a function
# that acts on a specific object. The methods available to an object depend
# on its type. 

# You access methods of an object by writing the object or its variable name,
# followed by the function name and its arguments, like so: 
# my_object.method_name(arg1, arg2)

# For instance, all objects have a method called `__str__` that returns a 
# string version of that object
two = 2
two_str = two.__str__()
print("two is an:", type(two))
print("two_str is an:", type(two_str))
print()

# Be careful: some methods "mutate" their object, meaning that they change the
# data contained in that object. We'll see some examples of such "mutator 
# functions" in the next section.

# ** Important functions for working with lists **

# 1. len 
print("len:")

# You can get the length of the list by using the Python function `len`. Note
# that `len` is not a method! 
my_list = [1, 2, 3]
print("List", my_list, "has length", len(my_list))

print()

# 2. sort
print("sort:")

# Sort orders the elements in a list. 
numbers = [1, 4, 2, 3, 0]
numbers.sort() 
print("Sorted numbers:", numbers)

# You can also sort strings by alphabetical order. 
letters = ["c", "a", "b"]
letters.sort()
print("Sorted letters:", letters)

# Note that `sort` is a mutator method! `L.sort()` modifies the order of the 
# elements in `L` and returns `None`. 

print()

# 3. append and extend
print("append and extend:")

# These functions let you add elements to a list. Both are mutator methods!

# append adds a single item to the back of a list. 
my_list = [1, 2, 3]
my_list.append(4)
print("my_list after append:", my_list)

# extend takes in another list and appends all of the elements from that list,
# in order, to the back of my_list. 
my_list.extend([5, 6, 7])
print("my_list after extend:", my_list)

print()

# 4. Other functions

# There are a ton of other useful list methods! Take a look at the Python 
# documentation on lists to learn more about them. 

print("Learn more about lists here:", 
    "https://docs.python.org/2/tutorial/datastructures.html#more-on-lists")
print()

# ** Exercises ** 
print("Output of exercises:")

# 1. What is the problem with the following code? Fix it! 
print("Exercise 1")
some_floats = [1.4, 1.2, 2.9]
sorted_floats = some_floats.sort()
print("Here are the sorted floats!", sorted_floats)
print()

# 2. Write a function that removes all instances of the number 13 from a list.
#    Hint: you might find the methods `count` and `remove` useful.
print("Exercise 2")

def remove_13(L):
    # Your code here
    pass

list_with_13s = [13, 2, 13, 4, -1, 13]
remove_13(list_with_13s)
print("Used to have 13s, but now should be [2, 4, -1]:", list_with_13s)
print()

# 3. What happens when you try to change a single character of a string? 
print("Exercise 3")
#    Uncomment the following line to find out
#s[0] = "H"
#    What is another way you could get the same result? Fill in the function
#    below, which takes in a string `s`, an index `index`, and a character
#    `new_char` and returns a string that is the same as `s` except it has
#    `new_char` in position `index`. Hint: use slicing. 
#    What about your method prevents it from throwing an error? If you don't
#    understand, ask for help! 
def string_item_assign(s, index, new_char): 
    pass

print("Should be 'hello, world!':", string_item_assign(s, 0, 'h'))
