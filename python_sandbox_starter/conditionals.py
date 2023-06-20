# If/ Else conditions are used to decide to do something based on something being true or false

x = 10
y = 5

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

if x > y:
    print(f'{x} is greater than {y}, and I have proved my incredible programming skills')

# Logical operators (and, or, not) - Used to combine conditional statements


if x > 2 and x < 11:
    print('x is between 3 and less than 10 inclusive')
if y == False or y > 0:
    print('y is False or a positive integer')

# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object

my_list = [1, 2, 3]

if x not in my_list:
    print(f'{x} is not in my_list')

# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

my_other_list = my_list

if my_other_list is my_list:
    print('the lists reference the same object in memory')

my_third_list = my_list.copy()

if my_third_list is not my_list:
    print('the copied list does not reference the same object in memory')

word = 'hello'
other_word = 'hello'

if word is other_word:
    print('strings in Python must be primitive and immutable')
