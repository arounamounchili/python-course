# 1- Intro

# 2- What you can do with python

# 3- Installation: python and VSCode

# 4- Your fist Program (Create Project and Hello World

print("Hello World!")
print("This is our second print")
print()

# 5-  Variables:  Hoe to declare variable

age = 25  # int
print(age)
weight = 78.6  # float
print(weight)
last_name = "Mounchili"  # String
first_name = 'Inteligencia'  # String
print(last_name, ' ', first_name)
is_major = True  # Boolean
is_active = False  # Boolean
print(is_major)
print(is_active)

# Variable type
print(type(age))
print(type(weight))
print(type(last_name))
print(type(is_major))
print()


# 6- String

greeting = " Hello Python "
print(greeting.upper())
print(greeting.lower())
print(greeting.lstrip())
print(greeting.rstrip())
print(greeting.strip())
print(greeting)
print(greeting.find('o'))
print('Python' in greeting)
greeting = greeting.replace('Python', 'C++').strip()
print(greeting)
print()


# 7- Arithmetic Operators

x = 12
y = 18
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)
print(11 % 2)
x += 1
print(x)
x -= 3
print(x)
print(x)

operator_precedence = 10 + 39 * 2 + 2 * (34 + 5)
print(operator_precedence)
# etc.


# 8- convert Variable

height = 180
height_to_float = float(height)
print(height_to_float)
age = 15.0
age_to_int = int(age)
print(age_to_int)
# int()
# float ()
# bool()
# str()
print()


# 9- User Input

# input("What is your name? ")
# name = input("What is your name? ")
# print("your name is: " + name)

# age = input("Enter your age: ")
# age = int(age) + 1
# print("Happy Birthday, you are " + age + "Years old.)


# 10- IF Statement

price = 20000
if price > 10000:
    print("The Price is greater than 10000")

price = 8000
if price > 10000:
    print("The Price is greater than 10000")
else:
    print("The Price is less than 10000")

if price > 10000:
    print("The Price is greater than 10000")
elif price > 5000:
    print("The Price is greater than 5000")
else:
    print("The Price is less than 10000")

"""
name = input("What is your name? ")
age = int(input("How old are you?"))
is_major = age > 18

if name.lower() == "python" and is_major == True:
    print("Welcome my Birthday Party")


if name.lower() == "java" or name.lower() == "javascript":
    print("Bye Bye")
"""
print()


# 11- Loops

print("1")
print("2")
print("3")
print("4")
print("5")

# for i in range(1, 100, 2):
for i in range(10):
    print(i)

i = 0
while i <= 5:
    i += 1
    print(i)

print()


# 12- Lists

my_cars = ["VW", "Ford", "Mercedes", "NISSAN"]
#           0       1         2          3
print(my_cars)
print(my_cars[0])
print(my_cars[3])   # print(my_cars[-1])

my_cars[0] = "Volkswagen"
print(my_cars)

print(len(my_cars))

my_cars.append("Peugeot")
print(my_cars)

my_cars.insert(2, "Jaguar")
print(my_cars)

print(my_cars[0:2])

print("Bugatti" in my_cars)
print("Volkswagen" in my_cars)

for car in my_cars:
    print(car)

print()


# 13- Tuples

fruits = ("Banana", "Orange", "Apple")
print(fruits)
print(fruits[0])
print(len(fruits))
print()


# 14- Functions

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


# Function with a Return Value
def addition(number1, number2):
    result_addition = number1 + number2
    return result_addition


a = 120
b = 80
result = addition(a, b)
print(f'The addition of a and b is: {result}\n')
