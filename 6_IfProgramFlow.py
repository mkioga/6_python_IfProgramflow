
# ======================
# 6_IfProgramflow.py:
# ======================


# To comment a block of code, highlight it, then ctrl + /

# < > = comparisons and and or comparisons

age = int(input("How old are you "))
if age >= 16 and age <= 65:             # Tests if age is between 16 and 65
    print("You are between 16 and 65 yrs and can work")

# The and has a lower priority than the conditional operators <, >, =
# So above condition evaluates as expected. With <,>,= being evaluated before the and
# But to make things a lot clearer, we should add brackets.

print("="*30)
age = int(input("How old are you "))
if (age >= 16) and (age <= 65):             # Tests if age is between 16 and 65
    print("You are between 16 and 65 yrs and can work")

# Another way to write above code is this

print("="*30)
age = int(input("How old are you "))
if 16 <= age <= 65:             # Tests if age is between 16 and 65
    print("You are between 16 and 65 yrs and can work")

# You can also write it using just < and >

print("="*30)
age = int(input("How old are you "))
if 15 < age < 66:             # Tests if age is more than 15 and less than 66
    print("You are between 16 and 65 yrs and can work")

# We can also do same test using OR command

print("="*30)
age = int(input("How old are you "))
if (age < 16) or (age > 65):
    print("You are too young or too old to work")
else:
    print("You are between 16 and 65 yrs and can work")

# Testing for true or false in python
# This prints x is true because in python, true is 1 and false is 0
# So if anything is non-zero or non-empty value, it evaluates to true
# and since x is set to string value false, it has something and evalueates to true

print("="*30)
x = "false"
if x:
    print("x is true")


# Another way to use this true (something there) and false (something not there)

print("="*30)
x = input("Please enter some text: ")
if x:
    print("You entered this text: '{}'". format(x)) # put '{}' to have '' around words
else:
    print("You did not enter anything")

# Boolean testing in python
# Boolean is a binary variable, having two possible values called “true” and “false.”.
# you see that None (a keyword), 0, 0.0 and all the other signs evaluate to False
# NOTE we have a .format at the end where it is pulling the numbers

print("="*30)
print("""False: {0}
None: {1}
0: {2}
0.0: {3}
empty list []: {4}
empty tuple []: {5}
empty string []: {6}
empty string []: {7}
empty mapping []: {8}
""".format(False, bool(None), bool(0), bool(0.0), bool([]), bool(()), bool(''), bool(""), bool({})))




# Using "not". This reverses the current scenario
# in below code, note that not, False and True are keywords
# Need to start with Caps for False and True
# Answer shows that not False is true and not True is false
# Also note that False returns a zero and True returns a one

print("="*30)
print(not False)
print(not True)


# Here is how to do a test using not

print("="*30)
age = int(input("Please enter your age: "))
if not(age < 18):
    print("You are 18 and over and old enough to vote")
else:
    print("Please come back in {} years".format(18 - age))



# Using the "in" keyword
# Note that this is case sensitive. So M is not equal to m

print("="*30)
name = "Mwongera"
print(name)
print()
letter = input("Please type a letter: ")
if letter in name:
    print("Congrats! your letter '{}' is in 'Mwongera'".format(letter))
else:
    print("Your letter '{0}' is not in name 'Mwongera'".format(letter))


# you can also add the "not" test to reverse things

print("="*30)
name = "Mwongera"
print(name)
print()
letter = input("Please type a letter: ")
if letter not in name:
    print("Your letter '{0}' is not in name 'Mwongera'".format(letter))
else:
    print("Congrats! your letter '{}' is in 'Mwongera'".format(letter))


# I will try above code but use double {} to see if it works
# This one works. Pay attention to brackets. Thats where the initial errors came from

print("="*30)
name = "Mwongera"
print(name)
print()
letter = input("Please type a letter: ")
if letter not in name:
    print("Your letter '{0}' is not in name '{1}'".format((letter), (name)))
else:
    print("Congrats! your letter '{0}' is in name '{1}'".format((letter), (name)))