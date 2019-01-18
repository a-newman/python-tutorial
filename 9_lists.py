import copy


# ** Lists ** 

# So far, we have seen simple data types like numbers and strings. But what
# if we want to store a collection of objects? For instance, maybe we want to
# store the weather forecast for the next week. 

# Python lets us do this with something called a list: 

forecast = ["sunny", "windy", "sunny", "snowy", "rainy", "rainy", "sunny"]

# Lists are surrounded by brackets and the elements are separated by commas.

# Lists don't just have to contain strings; in fact, they can contain any data
# type, like integers. 
temperature_forecast = [10, 9, 2, 2, 3, 6, -1]

# The same list can contain different data types
tomorrow_forecast = ["sunny", 10]

# Lists can contain even contain other lists! 

full_forecast = [
    ["sunny", 10], # Monday
    ["windy", 9],  # Tuesday
    ["sunny", 2],  # ... 
    ["snowy", 2],
    ["rainy", 3],
    ["rainy", 6],
    ["sunny", -1]
]

# Lists can be empty 
empty_list = []

# You can print lists the same way you print other data types
print(full_forecast)

print("")

# ** Indexing ** 

print("Indexing: ")

# Lists are ordered: that means that the order of the elements matters. In 
# fact, you can get elements from a list by their position, or index, in the
# list. 
# You index into a list using brackets, like so:
print("The forecase for Monday is:", full_forecast[0])
print()

# Careful! Python lists are 0-indexed, meaning that the first element has index
# 0, not index 1! If the list has length L, the last element has 
# index L-1. 
indexes = ["zero", "one", "two"]
print("The element at index 0 is:", indexes[0])
print("The element at index 1 is:", indexes[1])
print("The element at index 2 is:", indexes[2])
print()

# You can also assign elements using list indices! 
british_indexes = indexes[:] # make a copy...we'll explain this below!
british_indexes[0] = "zed" 
print("british_indexes", british_indexes)
print()

# ** List length and negative indexing ** 
print("Negative indexing:")

# What if you want to grab the last element from a list, or the second-to-last
# element? 

# We mentioned above that the last element of the list has index length-1. One 
# way you could find the last element is that you could find the list's length
# and calculate the correct index. You can get the length of a list using 
# Python's inbuilt function `len`.
indexes_length = len(indexes)
print("Length of indexes:", indexes_length)
print("Last element in indexes:", indexes[indexes_length-1])
print("Second-to-last element in indexes:", indexes[indexes_length-2])
print()

# However, there is an easier way to do this...negative indexing! 

# Negative indexes count backwards from the end of the list (so index -1 refers 
# to the last element, index -2 refers to the second-to-last element, etc)
print("The element at index -1 is:", indexes[-1])
print("The element at index -2 is:", indexes[-2])
print("The element at index -3 is:", indexes[-3])
print()

# ** Slicing ** 

print("Slicing: ")

# You can also use indexes to pick out more than one element from a list. 
# Selecting a subset of a list is known as "slicing". 

# To get a slice of a list, you need to choose two indexes: a start and an
# end. They are put inside brackets and separated by a colon, like so: 
long_indexes = ["zero", "one", "two", "three", "four"]
start_index = 1
end_index = 4
middle_indexes = long_indexes[start_index:end_index]
print("middle indexes:", middle_indexes)
# Note that the slice includes the first index and excludes the end index! 

# You can choose to omit either the start or end index. In this case, Python
# will set the default start index to 0 and the default end index to `len(L)-1`
print("without start index", long_indexes[:end_index])
print("Without end index", long_indexes[start_index:])
print("Without start or end index", long_indexes[:])
print()

# Now you know why writing `L[:]` creates a copy of list `L`: it creates a 
# slice that contains the entire list! 

# ** Exercises ** 
print("Output of exercises:")

# 1. What happens when you try to use a list index that doesn't exist? 
#    Uncomment the following lines and find out! 
print("Exercise 1")
#print(long_indexes[1000])
#print(long_indexes[-1000])
#    How about when you try to slice beyond the range of a list? 
#print(long_indexes[:1000])

# 2. What is the problem with the following function? Fix it! 
#    Hint: This kind of error is known as an "off-by-one" error, and it's a 
#    common bug! 
print("Exercise 2")

def print_list(L): 
    i = 1
    while i <= len(L): 
        print(L[i])
        i += 1

# Uncomment this to test the function!
#print_list([1, 2, 3])

print()

# 3. Write a while loop to print all the elements of a list backwards. 
print("Exercise 3")

def print_list_backwards(L):
    # Your code here
    pass

print_list_backwards([1, 2, 3])

print()

# 4. What is the difference between the following two ways of grabbing the
#    second element in a list? Hint: what data type do they return?
print("Exercise 4")

fruits = ["apples", "oranges", "bananas"]
oranges_indexed = fruits[1]
oranges_sliced = fruits[1:2]
print("oranges_indexed:", oranges_indexed)
print("oranges_sliced", oranges_sliced)
print()

# 5. Write a function called "trim" that takes a list `L` and an integer 
#    `margin` and returns a version of `L` with the first `margin` and last
#    `margin` elements removed.
print("Exercise 5")
def trim(L, margin): 
    # Your code here 
    pass

print("Should be ['two']:", trim(long_indexes, 2))
