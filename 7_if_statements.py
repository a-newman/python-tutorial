# ** If-else statements ** 

# We have learned about variables and function arguments. What if you want your
# code to behave differently based on the value of a variable or a function # argument? 

# For instance, maybe you are trying to decide whether you are going to ski 
# today. Your decision depends on the weather conditions. If it is very windy,
# you will stay home; otherwise you will go up to the slopes. We can represent
# your thought process using an if-else statement:  

def will_i_go_skiing(is_windy): 
    print("If is_windy is", is_windy, ", then I will...")
    if is_windy: 
        print("stay indoors :(")
    else: 
        print("go skiing!")

will_i_go_skiing(True)
will_i_go_skiing(False)

print("\n")

# An if statement takes in a boolean value (in this case, the variable 
# `is_windy`). If the boolean is `True`, then the indented block under the `if`
# part of the statement runs. Otherwise, the indented block under the `else`
# statement runs. 

# If statements do not need to have an else block! Consider the following
# example: 

def complain_if_windy(is_windy): 
    print("if_windy is", is_windy)
    if is_windy: 
        print("Darn! I hate the wind.")

complain_if_windy(True)
complain_if_windy(False)

# In this case, the second print statement will run if `is_windy` is `True`; 
# otherwise nothing happens. 

print("\n")

# ** If-elif-else statements ** 

# It is possible to have more than two options for a variable! Check out this
# example: 
weather_forecast = "sunny" # try changing this variable! 

def print_weather(weather_forecast): 
    print("The forecast reads...'", weather_forecast, "'")
    if weather_forecast == "sunny": # the first statement starts with `if`
        print("It's sunny!")
    elif weather_forecast == "windy": # you can have many `elif` clauses 
        print("It's windy!")
    elif weather_forecast == "snowing": 
        print("It's snowing!")
    else: # the last `else` statement is optional
        print("Unrecognized weather pattern")

print_weather("sunny")
print_weather("windy")
print_weather("snowing")
print_weather("tornado")

# Here, Python checks the booleans after all the `if` and `elif` statements 
# until one of them is `True` and then runs the next indented block. If none
# of the `if` or `elif` booleans are `True` and there is an else block, Python
# runs that. 

print("\n")

# ** Exercises ** 
print("Output from exercises:\n")

# 1. Fill in the following function so that it returns "Too hot" if temp is
#    greater than 21, "Too cold" if temp is less than 21, and "Just right" if
#    if temp equals 21.
print("\nExercise 1")
def hows_the_temperature(temp): 
    pass

print("Should say 'Too hot':", hows_the_temperature(30))
print("Should say 'Too cold':", hows_the_temperature(15))
print("Should say 'Just right':", hows_the_temperature(21))


# 2. Fill in the following function so that it returns a/b if b is not 0, 
#    otherwise it returns the string "Cannot divide by zero"
print("\nExercise 2")
def safe_divide(a, b): 
    pass

print("Should print 3:", safe_divide(6, 2))
print("Should print 'Cannot divide by zero':", safe_divide(6, 0))
