""" 04- Sequence (list, tuple, range) """


# List: Lists are used to store multiple items in a single variable.
#       Lists are ordered, changeable, and allow duplicates values.

first = "Arouna"
second = "Ronald"
third = "Carlos"
fourth = "Freddy"

students_list1 = ["Arouna", "Ronald", "Carlos", "Freddy"]
print(students_list1, "\n")


# get the first element
students_list12 = ["Jean", "Joel", "Mbappe", "Messi"]
# indices:            0       1        2         3
print(students_list12[0])
print()

# changes the value of an element in the list
students_list12[0] = "Mounchili"   # get the first element
students_list12[1] = "Samuel"      # get the second element
students_list12[2] = "Diane"
students_list12[3] = "Sandra"
print(students_list12)
print()

# add a new element in the list
students_list12.append("Carolle")
print(students_list12)
print()


# List can contain different types of variables
number_of_people_in_classroom = [45.7, 67, "fifty", "twenty", 70, True]

# Slicing
ages = [10, 28, 35, 14, 45, 16, 7, 38]
print(ages[0:5:1])    # [10, 28, 35, 14, 45]
print(ages[2:5])    # [35, 14, 45]
print(ages[0::2])   # [10, 35, 45, 7]
print(ages[:5])     # [10, 28, 35, 14, 45]
print()

# List concatenation
my_list1 = ["a", "b", "c"]
my_list2 = ["d", "e", "f"]
my_list = my_list1 + my_list2
print(my_list)      # ['a', 'b', 'c', 'd', 'e', 'f']
print()


""" List methods """

# len() : get the length os a list
my_string = ["h", "e", "l", "l", "o"]
print(len(my_string))
print()

# append() : add an element to a list
my_string = ["h", "e", "l", "l", "o"]
my_list.append(",")
my_list.append("World")
print(my_list)

# insert() : add elements at specific indexes in a list
my_list2 = [1, 2, 3]
my_list2.insert(2, 4)
print(my_list2)

# pop() : delete elements from a list (remove the last element in the list
my_list3 = [1, 2, 3]
my_list3.pop()
print(my_list3)
my_list3.pop()
print(my_list3)

# pop()
my_list4 = [1, 2, 3]
my_list4.pop(1)  # delete the element at index 1
print(my_list4)

# del
my_list = [1, 2, 3]
del my_list[0]
print(my_list)

# remove()
my_list = [1, 4, 3]
my_list.remove(4)
print(my_list)

# reverse() : reverse the elements in a list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list.reverse()
print(my_list)      # [9, 8, 7, 6, 5, 4, 3, 2, 1]

# copy a list
my_list = ["Aaron", "Zidane", "Marco"]
# my_list_copy = my_list => my_list_copy will be a reference to my_list
my_list_copy = my_list.copy()   # or my_list_copy = list(my_list)
print(my_list_copy)


# Tuples: Tuples are collections that are ordered and unchangeable. Allows duplicate members."""

clothes = ("Shoes", "Jeans", "Short", "T-Shirt", "Jeans")
print(clothes)

# get the length
print(len(clothes))

# Create a tuple with one item
my_tuple = ("item 1", )     # add a comma after the item to create a tuple with only one item
# print(type(my_tuple))
print(my_tuple)

# Membership Check: We can check whether an element is part of a tuple
# using 'in' and 'not in'
clothes = ("Shoes", "Jeans", "Short", "T-Shirt")
print('Shoes' in clothes)       # True
print('Shoes' not in clothes)   # False

# Access Tuple items
my_tuple = (12, "a", "b", True, 0.1)
print(my_tuple[4])

# Range of Indexes
my_tuple = (12, "a", "b", True, 0.1, "e")
print(my_tuple[0:])
print(my_tuple[2:4])
print(my_tuple.index('b'))  # index = 2
print()

# Unpacking a Tuple
colors = ("green", "red", "yellow")
(green, red, yellow) = colors
print(green)
print(red)
print(yellow)

# Range

r1 = range(1, 10)
print(r1)
r2 = range(1, 10, 2)
print(r2)

for r in range(1, 10):
    print(r)
