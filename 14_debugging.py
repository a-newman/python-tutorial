# ** Debugging ** 

# Debugging is an incredibly important skill, for any programming language!

# Your biggest tool when debugging Python code is one of our oldest friends...
# the print statement! You can using `print` as a window into the state of
# your program. If your code is producing unexpected results, the first thing
# you should do is to check your assumptions--that is, print out some variables
# at some point during the execution of your program and make sure that their
# values are what you think they are! If they are not, you have found a 
# problem--try to figure out why.

# Your second biggest tool are error messages. If your code is throwing an 
# error, read it closely, including the line numbers it gives you and the 
# "stack trace" (the list of functions that were being run when the error 
# occurred). Error messages in Python are often quite useful for figuring out
# what went wrong and where. 

# Your third big tool is the Internet! If you see an error that you do not 
# understand, Google it! Likely someone else has had the same problem and
# asked a question about it online. 

# Let's get some practice debugging In the following exercises, debug the 
# given piece of code so that it produces the desired results. 

# ** Exercises ** 

# 1. The following code should print the BMI (Body Mass Index) of each of three
#    patients. The BMI is given by a patient's weight (in kg) divided by the 
#    height (in meters) squared. 
#    This exercise is taken from: https://swcarpentry.github.io/python-novice-inflammation/09-debugging/index.html
print("Exercise 1")

patients = [[70, 1.8], [80, 1.9], [150, 1.7]]
BMIs = []

def calculate_bmi(weight, height):
    return weight / (height ** 2)

for patient in patients:
    weight, height = patients[0]
    bmi = calculate_bmi(height, weight)
    BMIs.append(bmi)

print("Expected BMIs:", [21.604938, 22.160665, 51.903114])
print("Calculated BMIs:", BMIs)
print()

# 2. 
print("Exercise 2")
# This code should print only the odd-indexed numbers in the alphabet.
import string
alphabet_list = list(string.ascii_lowercase)
for i, char in enumerate(alphabet_list): 
    if i % 2 == 0: 
        del alphabet_list[i]
print("Expected letters:", [char for i, char in enumerate(list(string.ascii_lowercase)) if i %2 != 0])
print("Calculated letters:", alphabet_list)
print()
