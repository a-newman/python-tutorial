# ** Imports ** 
print("Imports:")

# So far, most of the code that we have written in Python has all been inside
# one file. But what if you have a big project and you want to split your code
# between files? Or what if you want to use a function that someone else wrote? 

# This is where imports come in! 

# Imports are a way of loading code from another file for use in your own file.

# For instance, say we have a file that contains several useful functions for
# calculating the geometry of circles. This file is called `geometry_circle.py`
# Open the file now and take a look at what it contains.

# We can make use of these useful functions in our own code by "importing" the 
# file `geometry_circle.py`, like so:
import geometry_circle

# Now, we can use the functions inside `geometry_circle.py` like this: 
my_circle_radius = 2
my_circle_area = geometry_circle.area_circle(my_circle_radius)
print("The area of a circle with radius", my_circle_radius, "is", 
    my_circle_area)

# Note that we accessed the function `area_circle` inside the file 
# `geometry_circle` by using a dot: `geometry_circle.area_circle`

# What if there is a function that you want to use a lot, and you don't want
# to have to write the name of the file every time you use it? In that case,
# it is possible to import specific functions from a file. 

from geometry_circle import circumference

# Now, you can use `circumference` without specifying the name of a file
my_circle_circumference = circumference(my_circle_radius)
print("Circumference is:", my_circle_circumference)

# You can also import constants, like integers are strings, from a file!
print("My favorite circle radius is:", 
    geometry_circle.MY_FAVORITE_CIRCLE_RADIUS)

print()

# ** Built-in Python modules ** 
print("Built-in modules:")

# Python has a lot of really helpful built-in packages that let you do things
# like creating new files, representing dates and times, and even running an
# http server! Packages that are part of the "Python Standard Library" require
# no additional downloading or configuration to use. 

# Some built-in Python packages that I really like are: 
# - string: useful string helper funcions and constants (remember 
#   `string.ascii_lowercase`?
# - datetime: classes for doing calculations with dates and times
# - random: provides functions for shuffling and randomly selecting from lists,
#   and for generating random numbers/coin flips.
# - time: useful for timing operations
# - copy: contains useful helper functions for copying nested lists and dicts
# - math: mathematical constants and operations (for example, `math.pi`)
# - os: functions for working with the operating system and file system
# - pickle and json: lets you save Python objects as json or binary objects

# Using these packages is really easy. Here are some examples:

import math 
print("The value of pi is:", math.pi)

import datetime
print("The current time is:", datetime.datetime.now())

import string 
print("Here are all the digits:", string.digits)

# Look at the documentation for the Python standard library to find out what
# other packages are available: 
# https://docs.python.org/3/library/

print()

# ** External Python modules ** 

# What if you want to use code that someone else has written--code that is not
# part of the standard library, but also is not part of your own code base? 

# Fortunately, there are many useful libraries--standalone code bases--written 
# in Python that we can make use of.
# Python also provides its own package manager. A package manager is a system
# for sharing and downloading pieces of code--in this cases, Python libraries.
# Python's package manager is called pip. 

# pip is easy to use. If you know the name of the package you want to install,
# you can do it from the command line. For instance, pretend you want to 
# install the package `requests`, which allows you to make http requests. 
# Then you could type this in the terminal: 
# `pip install requests`

# After that is done, you could then import the requests library like so: 
# `import requests`

# Note 1: if you are using an IDE such as PyCharm, you may need to install 
# packages via the IDE. Here are instructions for how to install packages using
# PyCharm: 
# https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html

# Note 2: It is advised, although not required, to use virtual environments
# (venvs) when installing packages. Virtual environments are sort of like 
# sandboxes for your Python code. They let you have different dependencies
# (outside libraries) for different projects. They also let you simultaneously
# install different versions of the same package and keep track of which
# packages are required for which project. You can read more about virtual
# environments here: 
# https://docs.python.org/3/library/venv.html

# There are a ton of really useful python libraries out there! 

# ** Exercises ** 
print("Exercises:")
# 1. Use functions in the file `geometry_square.py` to print the perimeter and
#    area of a square with side length 1234.
print("Exercise 1:")
#Your code here
print()
# 2. Print all the files in this folder. Hint: check out the function 
#    `os.listdir`. 
print("Exercise 2:")
#Your code here
print()
# 3. Numpy is a very popular Python library that provides efficient functions
#    and data types for working with vectors and matrices--for instance, 
#    calculating cross products or matrix multiplications. Install numpy and
#    use it to calculate the cross product of the following two vectors. Hint:
#    see the documentation for the function `numpy.cross`: 
#    https://docs.scipy.org/doc/numpy/reference/generated/numpy.cross.html
print("Exercise 3:")
vec1 = [0, 1, 0]
vec2 = [1, 0, 0]
#Your code here
