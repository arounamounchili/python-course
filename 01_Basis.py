"""
Python Basis
"""


""" 01 - First Programme """

print("Hello World!")


""" 02- Comments: simple and multi line comments """

# This is a simple comment
""" 
First comment in the first line.
Second comment in the second line
"""


""" 03- Variables """

name = "Python"  # or name = 'Python'
age = 20
height = 12.4
print(name)

# in python variable can be reassigned
name = "Programming"
age = "No age"  # The data type can be change

# Case-sensitive
weight = 64
Weight = 72     # weight and Weight are different
print(weight)
print(Weight)

# Verify the type of any variable/objet in Python using the function type()
print(type(name))
print(type(height))


""" 04- Arithmetic operators in Python """

# Addition: use the + sign
print(10 + 33 + 2)  # 45

# Subtraction
print(10 - 3)       # 7

# Multiplication
print(12 * 4)       # 48

# Division
print(13 / 2)       # 6.5
print(10 / 2)       # 5.0
print(10 // 2)      # 5 (use a double forward slashes to get integer)

# Find a remainder divided by another number
print(19 % 3)       # 1 (3*6 + 1)

# Power
print(4 ** 2)       # 16
print(pow(10, 2))   # 100
