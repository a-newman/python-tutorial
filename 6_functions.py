# ** Functions ** 

# A function is some lines of code that you can reuse multiple times. Here is
# an example of a function: 

def print_goodday(): 
    print("Thanks for coming!")
    print("Have a good day!")

# This is called a function declaration because you are defining a function 
# name and what it does. A function is declared using the `def` keyword. The 
# name of this function is print_goodday`. The code contained in the function 
# (the "body" of the function) is indented. 

# To call the function, write: 
print_goodday()

# Try running the code to see what it does!

print("\n")

# ** Function arguments **
print("Function arguments: ")

# Look at the following function: 

def add(x, y): 
    print(x, "+", y, "=", x+y)

# The variables x and y are special because they are inputs to the function. 
# These special variables are known as arguments. A function can have an 
# unlimited number of arguments separated by commas. You can call a function 
# with different arguments: 
add(1, 2)
add(10, 20)

# Function arguments are separated by commas. When you call a function, the 
# number of arguments you pass in must be equal to the number of arguments in
# the function declaration! 

print("\n")

# ** Return statements ** 
print("Return statements: ")

# It is possible to store the output of a function in a variable for later use.
# Inside a function, you can specify the output value using something called a 
# return statement. Look at the example below: 

def add_with_return(x, y): 
    val = x + y
    return val # this is a return statement

z = add_with_return(1, 2)
print("z=", z)

# In this example, `val` is known as the return value, and it is the value that
# will be stored in variable z. The return value can be any variable or 
# expression present in the function. 

# There are a couple of things to note about return values. First, if a return
# statement is run, the value is stored and the function stops running. 
# Observe the following example: 

def test_code_after_return(): 
    print("Before return statement: this code will be run")
    return 
    print("After return statement: this code will never run!")

test_code_after_return()

# Second, it is possible to not specify a return value, either by not including
# a return statement or by not specifying a value. In this case, the value
# that is stored is a special value in Python, `None`. See the following
# examples: 

def no_return_statement(): 
    pass # `pass` is a special Python keyword indicating an empty function body

def empty_return_statement(): 
    return

print("A function with no return statement returns:", no_return_statement())
print("A function with an empty return statement returns:", 
    empty_return_statement())

print("\n")

# ** Exercises **

print("Output from exercises:")

# 1. Write a function that prints out your name and call it.
# Your code here 

# 2. Write a function that takes in a number as an argument and prints out 
#    twice that number. Call it twice with two different numbers.
# Your code here

# 3. Modify your function from above so that instead of printing twice the 
#    number, it returns the result of the multiplication. Call the function
#    using the variable `inp` and store the result in the variable `output`.
inp = 3
output = 0
print("output should be 6:", output)

# 4. What happens when you pass in the wrong number of arguments? Uncomment the
#    code below to try it out. 
#add(1, 2, 3)

# 5. The body of a function is defined by its indentation level. Once you hit 
#    the end of the indented block that follows the `def` statement, you are
#    no longer in the function body. Look at the example below: 
def where_does_the_function_end(): 
    print("Line A is inside the function") # Line A 
    print("Line B is inside the function too") # Line B
    print("is Line C inside the function?") # Line C 
print("Line D is outside the function") # Line D

where_does_the_function_end()

#   Which line runs first? Why? If you're not sure why, ask someone! 
#   Now try unindenting Line C. How does this change the order in which the
#   lines are run? 
