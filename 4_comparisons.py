# ** Numerical comparisons ** 

# Python supports comparisons between different numbers. 
# The result of a comparison is a boolean. 
# A boolean is a special data type that can only take on one of two values:  
# `True` or `False`.
# Note that `True` and `False` are capitalized!!!

print("Examples of numerical comparisons:")

x = 10
y = 5.0
print("x=", x)
print("y=", y)

# Greater than/ Less than: 
print("x>y is", x>y)
print("x<y is", x<y)

# Greater than or equal/Less than or equal: 
print("x>=y is", x>=y)
print("x<=y is", x<=y)

# Equals
# Note that a single equals sign is used to assign a value to a variable; 
# a double equals sign checks if two values are equal
print("x==y is", x==y)
print("x==10 is", x==10)

print("\n")

# ** Equality for non-strings ** 

# The equality comparison `==` can be used on any data type, not just numbers. 
# It checks if two variables or data types refer to the same thing. 
# For instance: 
print("1=='hello' is", 1=="hello")
print("'hi'=='hello' is", "hi"=="hello")
print("'hello'=='hello' is", "hello"=="hello")

# ** Exercises ** 
print("Output of exercises")

# 1. What is the difference between `x=10` and `x==10`? If you aren't sure, ask
#    Anelise or one of your classmates to make sure you understand! 
# 2. Write code below that checks if 3 times 5 + 10 is greater than 20 and 
#    prints the result. 
# Your code here
# 3. Above, we talked about using `==` to check if two values of any data type
#    are the same. But what happens if you try to compare different data types
#    using a different comparison operator? Try it below.
#print(3 > "hello")
