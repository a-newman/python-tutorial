import time


# ** Dictionaries ** 

# Another super-important Python data type is a dictionary. 

# A dictionary maps objects, called keys, to other objects, called values. 
# It works a lot like a language dictionary! 
english_dictionary = {
    "dog": "an animal that barks and likes bones",
    "cat": "an animal that meows and likes yarn",
    "parrot": "a multicolored animal that flies and repeats words"
}

# A dictionary is surrounded by curly braces. Each key is separated from its 
# value by a colon, and key-value pairs are separated by commas. 
# In this example, the keys are the terms in the dictionary (in this case, the
# names of animals) and the values are the definitions. 

# In fact, Python lets us check out what our keys and values are! 
print("keys", english_dictionary.keys())
print("vals", english_dictionary.values())
print()

# If you know the key, it is really easy to find the corresponding object. 
print("The value corresponding to key 'dog' is:", english_dictionary['dog'])
# Like indexing into a list, find a value for a key uses brackets, but inside
# you put the key you want to find, not the index. 
print()

# You can add, change, or remove key-value pairs from a dictionary. The ability
# to modify an object after it is created is known as mutability, and we have
# seen that both list and dictionaries are mutable. 
dog_lovers_dict = english_dictionary.copy() 
dog_lovers_dict["dog"] = "The best animal ever!" # Change a key-value pair
dog_lovers_dict.pop("cat") # Removes the key `cat`
dog_lovers_dict["pug"] = "The cutest dog ever!" # add a new key-value pair
print("dog_lovers_dict:", dog_lovers_dict)
print()

# Dictionaries are UNordered, meaning that there is no correct ordering of the 
# elements. Once some keys are in a dictionary, there is no way to tell which
# keys were added first! 

# ** Dictionary types ** 

# Like lists, dictionaries can contain many different data types. 
double_dictionary = {1:2, 2:4, 3:6} # a dictionary made up of ints
# the keys and values do not have to have the same types
int_to_string_dictionary = {1:"one", 2:"two", 3:"three"}
# in fact, neither the keys nor the values have to be all of the same type! 
messy_dictionary = {1: "one", "two": 2, 0: ["zero", "zed", "cero"]}

# However, there is one important restriction on what data types can be in a
# dictionary. Values can be any data type, but keys MUST be an unmutable data
# type. Like we have already discussed, unmutable means that the data type 
# cannot be modified after it was created. (If you are curious why that is, 
# ask Anelise!)
# This means that lists and dictionaries are valid values, but are not valid 
# keys! 

# ** Dictionaries and for loops 

# Much like we could write a for loop over a list, we can also write one for
# a dictionary! One way to do this is to iterate over all the keys in the 
# dictionary use the `.keys()` method. This is good if you only need the keys.
for key in english_dictionary.keys(): 
    print("The word", key, "is in our dictionary.")
print()

# If you want the keys as well as the values, you can use the method `items`: 
for key, val in english_dictionary.items(): 
    print(key, "means '", val, "'")

print()

# ** Useful methods ** 

# Like lists, dictionaries provide many useful methods. Here is the Python 
# documentation on dictionaries: 

# https://docs.python.org/3/library/stdtypes.html#typesmapping

# ** Exercises ** 
# 1. What happens if you try to find a key in a dictionary that doesn't exist?
print("Exercise 1")
#    Try it out! 
#print(english_dictionary['turtle'])
#    What about if you try to add a key to a dictionary that is an unsupported
#    (mutable) type? 
#english_dictionary[['pidgeon', 'dove', 'parrot']] = "see entry for bird"
print()
# 2. Remember the caesar cipher from the last tutorial? Turns out it's a little
#    easy to crack, so let's try something a little more complex. 
#    In this new version, every letter in the alphabet is encrypted as a random
#    different letter. The mapping from nonencrypted letter to encrypted letter
#    is stored in the following dictionary: 
print("Exercise 2")
caesar_cipher_dict = {'a': 'k', 'b': 'g', 'c': 'v', 'd': 'i', 'e': 'j', 
    'f': 'b', 'g': 'd', 'h': 'u', 'i': 'p', 'j': 'c', 'k': 'y', 'l': 'm', 
    'm': 't', 'n': 'h', 'o': 's', 'p': 'l', 'q': 'n', 'r': 'q', 's': 'r', 
    't': 'a', 'u': 'x', 'v': 'e', 'w': 'w', 'x': 'z', 'y': 'o', 'z': 'f'}
#    Fill in the following function to encrypt the message
def caesar_cipher_complex(message, caesar_cipher_dict): 
    pass # Your code here

message_to_encrypt = "bet you cant read this"
encrypted_message = caesar_cipher_complex(message_to_encrypt, 
    caesar_cipher_dict)
expected_message = "gja osx vkha qjki aupr"
print("Expected_message:", expected_message)
print("Your message:", encrypted_message)
print("Do they match?", encrypted_message == expected_message)
print()

# 3. How do you get the number of elements in a dictionary? Check the docs to
#    find out! 
# 4. Should you use a list or a dictionary in each of these circumstances? 
#    a. You are designing a competitor to Google translate. Given a word in 
#       English, you want to be able to quickly find the same word in Catalan.
#    b. You are volunteering at a marathon. You want to keep track of runners
#       and their assigned ids in the order that they finish the race. 
#    c. You are deciding who to invite to your birthday party. You want to 
#       keep track of the names of the people you are inviting. 
#    d. You are designing a server to log in users to your website. You want to
#       be able to look up someone's password given their username. 

# 5. (OPTIONAL) Another possible way of storing key-value pairs is a list of 
#    length-2 lists. Consider this alternative data structure for our English 
#    dictionary: 
print("Exercise 5")
list_dictionary = [
    ["dog", "an animal that barks and likes bones"],
    ["cat", "an animal that meows and likes yarn"],
    ["parrot", "a multicolored animal that flies and repeats words"]
]
#    Why should you use a Python dictionary instead? 
#    Below is a function that creates a Python dictionary and a "list 
#    dictionary". Each stores the same `n` elements. Then, it times how long it 
#    takes to look up the values for each of those `n` keys in each data type.
def list_dict_vs_dict(n): 
    # If you are 
    print("Running test with size", n)
    d = {i : str(i) for i in range(n)}
    list_d = [[i, str(i)] for i in range(n)]

    # time the normal dictionary
    start_time_d = time.time()
    for i in range(n): 
        temp = d[i]
    end_time_d = time.time()
    time_d = end_time_d - start_time_d

    # time the list dictionary
    start_time_list_d = time.time()
    for i in range(n): 
        temp = [elt[1] for elt in list_d if elt[0] == i][0]
    end_time_list_d = time.time()
    time_list_d = end_time_list_d - start_time_list_d

    print("List dictionary took", 
        time_list_d/time_d, 
        "times longer than a normal dictionary")

#    Look at the output from the following test runs. Do you see a relationship
#    Between the size of our dictionary and the relative performance of the two
#    methods? Why is a Python dictionary better than a list dictionary? 
list_dict_vs_dict(10)
list_dict_vs_dict(10**2)
list_dict_vs_dict(10**3)
list_dict_vs_dict(10**4)
#    If you are curious about how a dictionary works, or you want
#    clarification about what is happening inside the function above, please
#    ask!!!!
