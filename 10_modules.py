"""
Modules: A module is like a library. It's a file that content functions that
         you can include and use in your application.
"""


# Use Module
import module1

module1.say_hello("Romeo")


# Renaming a module
import module1 as md

addition = md.addition(4, 6)
print(addition)


# Import From Modules
from module1 import subtraction

print(subtraction(5, 6))
