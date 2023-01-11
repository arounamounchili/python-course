"""
Functions: A function is block of code that you can use over and over again,
           rather than writing it out multiple times. Functions enable programmers
           to break down or decompose a problem into smaller chunks, each of which
           performs a particular task.
"""


# Creating a Function
def my_function():
    print("This is our first function")
    print("This is our first function")


# Calling a function
my_function()


# Arguments: We can pass information into functions as arguments
def greeting(name):
    print(f'Hello, {name}')


def greeting2(name1, name2):
    print(f'Hello, {name1} and {name2}')


greeting("CCB")
greeting2("Jules", "Julie")
print()


# Keyword Arguments: we can also send arguments with the key = value syntax
# This way the order of the arguments does not matter
def greeting2(name1, name2):
    print(f'Hello, {name1} and {name2}')


greeting2(name2="Mounchili", name1="Arouna")


# greeting2("Arouna", "Mounchili")


# Default Parameter Value
def greeting(name="No name"):
    print("Hello, " + name)


greeting()
greeting("Ronald")


# Passing a List as an Argument
def show_list(my_list):
    for i in my_list:
        print(i)
    print()


show_list(["Arouna", "Ronald", "Carlos", "Freddy"])
students = ["Samuel", "Rony", "Daniel", "Fred"]
show_list(students)


# Returns Values
def addition(number1, number2):
    return number1 + number2


a = 12
b = 8
result = addition(a, b)
print(f'The addition of a and b is: {result}\n')


def convert_to_euro(dollar):
    return dollar * 1.001


def convert_to_cent(euro):
    return euro * 100


def convert_to_km(meters):
    return meters / 1000


dollar_to_euro = convert_to_euro(10)
print(dollar_to_euro)

meters_to_km = convert_to_km(1000)
print(meters_to_km)
