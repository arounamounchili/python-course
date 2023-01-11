""" 05- Dictionaries:
                    Dictionaries are used to store data values in key:value pairs.
                    A dictionary is a collection which is ordered, changeable and
                    do not allow duplicates."""

english_to_french_dictionary = {
    "Hello": "Salut",
    "Phone": "Telephone",
    "Mic": "Micro"
}
print(english_to_french_dictionary)

book_info = {
    "name": "Python Programming for Beginners",
    "ISBN": "5678-8839-3833-9833",
    "year": 2022,
}
print(book_info)

# To access specific elements in the dictionary, we simply use keys
hello_translation = english_to_french_dictionary["Hello"]   # Salut
phone_translation = english_to_french_dictionary['Phone']   # Phone
print(f'La translation of \'Hello\' in frensh is \'{hello_translation}\'')
print(f'La translation of \'Phone\' in frensh is \'{phone_translation}\'')

# Get the value of an element using get()
mic_translation = english_to_french_dictionary.get("Mic")
print(mic_translation)

# Create dictionaries using dict()
books_authors = dict([
    ("Socrate", "L'art de penser dans le vide"),
    ("Pythagoras", 'La formule de la puissance au carrée')
])
print(books_authors)
print()

# How to add new values to a dict
symbols = {'a': 'alfa', 'b': 'beta', 'd': 'delta'}
print(symbols)
symbols['g'] = 'gamma'
print(symbols)

# modify an element in the dictionary
symbols['a'] = "alpha"
print(symbols)

# Remove elements from a dict
symbols = {'a': 'alfa', 'b': 'beta', 'd': 'delta'}
symbols.pop('b')
print(symbols)

# Get the length of a dict
symbols = {'a': 'alfa', 'b': 'beta', 'd': 'delta'}
print(len(symbols))

# Membership
symbols = {'a': 'alfa', 'b': 'beta', 'd': 'delta'}
print('a' in symbols)
print('e' not in symbols)
print()

# Get Keys, get Values and get Items
my_keys = symbols.keys()
print(my_keys)

my_values = symbols.values()
print(my_values)

my_items = symbols.items()
print(my_items)

print()
# Loop through a dictionary
symbols = {'a': 'alfa', 'b': 'beta', 'd': 'delta'}
for s in symbols:
    print(symbols[s])
print()


""" 06- Sets: Set is a collection that is unordered, unmodifiable and unindexed.
              No duplicate members
"""

vowels = {"a", "e", "i", "o", "u", "y"}
print(vowels)

# Get the length
print(len(vowels))
print()

# Access Items: You cannot access items in a set by referring to an index or a key
set1 = {12, "23", 2, 5}
for i in set1:
    print(i)
print()

# Add items
vowels = {"a", "e", "i", "o", "u"}
vowels.add("y")
print(vowels)
print()

# Add sets or lists or tuple or sets
vowel1 = {"a", "e", "i"}
vowel2 = {"o", "u", "y"}
vowel1.update(vowel2)
print(vowel1)
