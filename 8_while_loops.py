import random

# ** While Loops ** 

# What if you want your code to do something over and over again until some
# condition is met? 

# For instance, maybe you're writing code for a timer
# and you want to keep checking how much time has passed until you have waited
# the correct amount of time. 

# Then you should use a while loop. Check out the example: 

time_to_count = 10
seconds_passed = 0

while seconds_passed < time_to_count: # this is called the condition 
    print("ticks_passed:", seconds_passed)
    seconds_passed += 1 # increase seconds_passed by 1
print("Timer done!")

print("\n")

# At the beginning of the loop, the condition (`seconds_passed < time_to_count`)
# is evaluated. If the condition is `True`, then the body of the loop--the
# indented block that follows the while condition--is run. If the condition 
# is `False`, then it continues with the rest of the code. 

# A really important thing to consider when writing a while loop is 
# "termination": making sure that at some point, the condition will evaluate to
# `False`. Otherwise, the loop will run forever! 

# ** Break ** 

# There is one exception to the idea of termination. Consider this while loop: 
n_tries = 0
while True: 
    n_tries += 1
    n = random.randint(1, 10) # chooses a random number between 1 and 10
    if n == 10: 
        break
print("Outside of loop; took", n_tries, "tries")

# Clearly, the condition here will never be `False`! They key here is the word
# `break`. This keyword causes Python to "break" out of the loop and continue
# with the next line of code. Note that writing a "while True" loop can be 
# dangerous, because it is not clear when the loop will terminate. If possible,
# state the condition explicitly. You should reserve "while True" for 
# situations where you really do have to continue doing something forever, or 
# where it is not clear how many times you will have to do something. 

# ** Exercises ** 

# 1. Write a while loop that prints all the numbers from 1 to 10. 
# Your code here. 
# 2. What is wrong with this code? 
# count = 10
# while (count < 100): 
#     print(count)
#     count = count - 1
