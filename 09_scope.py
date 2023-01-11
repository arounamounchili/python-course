"""
Scope: A variable is only available within the region in which it was created.
"""


""" Local Scope """


# A variable created inside a function is available inside that function

def say_hello():
    hello = "Hello, World!"
    print(hello)


say_hello()
# print(hello) # NameError: name 'hello' is not defined

# Function Inside Function: The local variable can be accessed from a function
# within the function


def say_hello():
    name = "Inteligencia"

    def my_name():
        print("Hello, " + name + "\n")
    my_name()


say_hello()


""" Global Scope """

# A variable created in the main body of the Python code is a global variable.

name = "Inteligencia"


def say_good_morning():

    def my_name():
        print("Good morning, " + name + "\n")
    my_name()


say_good_morning()

# Naming Variables

age = 24


def change_age():
    age = 26
    print("In the function your age is: " + str(age))


change_age()
print("Outside the function your age is: " + str(age))
print()


# Global Keyword
def say_morning():
    global morning
    morning = "Inteligencia"
    print(morning)


say_morning()
print(morning)


# Use the global keyword to change the value of a global variable inside a function

price = 240.0


def change_price():
    global price
    price = 26
    print("In the function The price is: " + str(price))


change_price()
print("Outside the function your price is: " + str(price))