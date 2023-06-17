# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Armando'

print('hello ' + name)

name = 'Lucien'

age = 33

# String Formatting

# Arguments by position

print('Hello, my name is {name} and I am {age}'.format(name=name, age=age))

# F-Strings - Available in Python 3.6 and later 

print(f"Hello, I'm {name} and I am of the age {age}")

print(f"Hi there {name.capitalize()} and I am of the age {age}")


# String Methods
