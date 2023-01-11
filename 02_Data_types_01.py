"""
Data types:
            1- Numbers (int, float, complex)
            2- Booleans (bool)
            3- Text ou String (str)
            4- Sequence (list, tuple, range)
            5- Mapping (dict)
            6- Set (set)
            7- Binary (bytes, bytearray)
            8- None (NoneType)
"""


""" 01- Numbers in Python: integers, floats, complex """

# Integers
number1 = -1000
number2 = 10000
result1 = number1 + number2
print("The result is: ", result1)


# Floats
height = 1.82
print("The height is: ", height)

x = 76.34e3   # e or E indicate the power of 10
print("x is: ", x)


# Complex numbers
complex_number1 = 3 + 6j
complex_number2 = 10 + 3j
print("\nThe complex number 1 is: ", complex_number1)
print("The complex number 2 is: ", complex_number2)
result2 = complex_number1 - complex_number2
print("The result: ", result2, "\n")


# Type conversion
a = 19      # int
b = 3.5     # float
c = 3j      # complex

x = float(a)    # convert from int to float
y = int(b)      # convert from float to int
z = complex(a)  # convert from int to complex
print(type(x))
print(type(y))
print(type(z))
print("\n")


""" 02- Booleans """

is_major = True         # True can be interpreted as 1
is_red = False          # False can be interpreted as 0
is_greater = 36 > 67    # False

print("The value of is_major is: ", is_major)
print("The value of is_greater is: ", is_greater)
print("\n")


""" 03- Text ou String (str) """

school_name = "University of Colorado"
name = 'Arouna'
print(school_name)
two_lines = "This is the first line \nand this is a second line"
print(two_lines)

# Multiline String
paragraph = """This is a first sentence that is written in this line.
The second sentence begin  here, and it is followed by a comma."""
print(paragraph)
print()
paragraph = '''This is a first sentence that is written in this line.
The second sentence begin  here, and it is followed by a comma.'''
print(paragraph)
print("\n")


# String operators

# concatenate strings using the + operator
first_string = "First"
second_string = "Second"

concatenated_string = first_string + " " + second_string
print(concatenated_string)

repeated_string = first_string * 5
print(repeated_string)


""" String built-in methods """

# len() : is a method use to get a length of a string
my_name = "Mounchili"
print("The length of my name is: ", len(my_name))

# lower() : converts all characters of a string into lower case
my_name = "AROUNA"
print(my_name.lower())

# upper() : converts all characters of a string into uper case
greeting = "hello"
print(greeting.upper())

# strip() : removes white spaces that can be in the beginning or the end of a string
greeting = " Hello   "
print(greeting.strip())

# split() : convert a string into an array of substrings based on a specific
# pattern that is mentioned as the separator
sentence = "We can use the split method to split this sentence in an array"
print(sentence.split(" "))
print()


# String value can not be changed after declaration
my_string = "Hello!"
# my_string[1] = "a"  # not allowed because string are immutable

# replace() : is a method to replace a character or a substring of a string
# with another character or substring
greeting = "Hello"
modified_greeting = greeting.replace("e", "a")
print(modified_greeting)    # Hallo


""" String formatting """

user = "Arouna"

# format()
greeting = "Hello, {}. Welcome to the Python programming course".format(user)
print(greeting)

greeting = "Hello, {1}. Welcome to the {0} course".format(user, "C/C++")
print(greeting)

name = "Mounchili"
today = "Saturday"
greeting = f"Good evening {name}. Today is {today}!"
print(greeting)



