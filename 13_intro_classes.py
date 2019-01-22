# ** Classes ** 

# In addition to objects like lists and dictionaries, Python also lets you
# define your own data types. These are known as classes. 

# Classes can be pretty complicated, but the basics are fairly simple. Skim the
# following links to learn more about how classes work: 

# Introduction to classes: 
# https://www.w3schools.com/python/python_classes.asp

# Python 3 documentation about classes: 
# https://docs.python.org/3/tutorial/classes.html

# ** Exercises **

# 1. Below, write a class called Fraction that represents a real fraction. 
#    It should have two fields, `numerator` and `denominator`, which are 
#    passed in in the __init__ function. It should also support a method
#    `multiply(other_fraction)`, which takes in a `Fraction` and returns 
#    another `Fraction` representing the product of itself and `other_fraction`.
class Fraction: 
    def __init__(self, numerator, denominator): 
        # save numerator and denominator as fields of this class with the same
        # name
        # Your code here
        pass

    def multiply(self, other): 
        # return a new Fraction whose `numerator` is the product of this 
        # class' numerator and other's numerator
        # and whose `denominator` is the product of htis class' denominator and
        # other's denominator
        # Your code here
        pass

# Test your code
f1 = Fraction(1, 2) # represents the fraction 1/2
f2 = Fraction(3, 4) # represents the fraction 3/4
product = f1.multiply(f2) # represents (1/2)*(3/4) = 3/8
print("Product (should be 3/8): " 
    + str(product.numerator) + "/" + str(product.denominator))
