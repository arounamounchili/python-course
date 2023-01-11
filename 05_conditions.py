"""
Conditions: python supports the logical conditions from mathematics:
            - Equals: a == b
            - Not Equals: a != b
            - Less than: a < b
            - Less than or equal to: a <= b
            - Greater than: a > b
            - Greater than or equal to: a >= b
"""

""" if statements """
age_player1 = 18
age_player2 = 25

if age_player1 < age_player2:  # We test whether age_player1 is less than age_player2
    # Python relies on indentation to define scope in the code
    print("Player 1 is younger than player 2")  # Whitespace at the beginning of a line

# elif: if the previous conditions were not true, then try this condition
age_player1 = 26
age_player2 = 25

if age_player1 < age_player2:
    print("Player 1 is younger than player 2")
elif age_player1 > age_player2:
    print("Player 1 is older than player 2")


# else: if all previous conditions were not true, execute this condition
somme1 = 5000
somme2 = 5000

if somme1 < somme2:
    print("Somme 1 is less than somme 2")
elif somme1 > somme2:
    print("somme 1 is greater than somme 2")
else:
    print("Somme 1 is equal somme 2")

# if .. else
number1 = 10
if number1 > 10:
    print("Hello, Welcome to the programming course")
    print("number1 is greater 10")
else:
    print("Number1 is not greater than or equal to 10.")


# And, or
score1 = 12
score2 = 15
average = 10

if score1 > average and score2 > average:
    print("score1 and score2 are above the average")

score2 = 9
if score1 < average or score2 < average:
    print("score1 or score2 are bellow the average")


# Nested if
somme = 20000
if somme < 50000:
    somme = somme - 10000
    if somme < 3000:
        somme = somme + 500
    else:
        somme = somme - 10000
else:
    somme = somme*2

print("La somme est: ", somme)
