"""
Classes / Objects: A class is like an object constructor, or a blueprint for
                   creating objects. An object has properties and methods
"""


# Object-Oriented Programming represents a way of organizing a program using classes and objects


# Create a Class: We can use  the class of Person as a blueprint to create as many
# instances as we want of it that we call objects
class MyClass:
    x = 10
    y = 100


# create an Object
my_object = MyClass()
print(my_object.x)
print(my_object.y)


# The __init__() Function: is used to initialise the object
class Person:
    # The self parameter is the reference to the current instance of the class
    # and is used to access variables that belong to the class
    def __init__(self, firstname, lastname, age):   # Special method
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


person1 = Person("Arouna", "Mounchili", 26)
print(person1.firstname, person1.lastname, person1.age)

print(person1)


# The __str__() Function: controls what should be returned when the class
# objet is represented as a string
class Person:
    # The init method is called when an instance of the class is created
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def __str__(self):
        return f"{self.lastname} {self.firstname} is {self.age} years old.\n"


person1 = Person("Arouna", "Mounchili", 26)
print(person1)


# object Methods: Methods are functions that belong to the object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def change_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age


person1 = Person("Raoul", 24)
print(person1.name)
print(person1.age)
person1.change_name("Henry")
person1.set_age(19)
print(person1.name)
print(person1.age, "\n")

# Modify object properties
person1.name = "Ismael"
print(person1.name)

# Delete object properties
del person1.name
# print(person1.name)  #Error ('Person' object has no attribute 'name')

# Delete Object
del person1


"""
Inheritance: Inheritance allows us to define a class that inherits all the
             methods and properties from another class.
             Parent class (base class) is the class being inherited from.
             Child class (derived class) is the class that inherits from another class
"""


# Create a Parent Class
class Vehicle:
    def __init__(self, name, number_of_wheels):
        self.name = name
        self.number_of_wheels = number_of_wheels

    def __str__(self):
        return f"{self.name} with {self.number_of_wheels} wheels\n"


# Create an object
vehicle1 = Vehicle("Mercedes", 4)
print(vehicle1)


# Create a Child Class
class Car(Vehicle):
    pass


car1 = Car("VW", 4)
print(car1)


#
class Bike(Vehicle):
    # When you add the __init__() function, the child class will no longer
    # inherit the parent's __init__ function
    def __init__(self, name, number_of_wheels, is_electric):
        # Use the super() function that will make the child inherit all
        # properties and methods from its parent
        super().__init__(name, number_of_wheels)
        self.is_electric = is_electric
        self.battery_level = None

        self.init_battery_level()

    def __str__(self):  # this override the the __str__() method in the parent class
        return f"{self.name} with {self.number_of_wheels} wheels and " \
               f"the Battery level is {self.battery_level}\n"

    def init_battery_level(self):
        if self.is_electric:
            self.battery_level = 100


e_bike = Bike(name="Velonix", number_of_wheels=2, is_electric=True)
print(e_bike)
print(f"The battery level is : {e_bike.battery_level}")

normal_bike = Bike("city Bike", 2, False)
print(normal_bike)
print(f"The battery level is : {normal_bike.battery_level}")

