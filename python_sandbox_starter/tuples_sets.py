# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
drinks = ('espresso', 'IPA', 'lemonade')

drink = ('milkshake')
print(f'the variable drink is a {type(drink)}')

drink = ('milkshake',) # Trailing comma required
print(f'the variable drink is a {type(drink)}')

try:
    drinks[1] = 'kombucha'
except(TypeError):
    print('tuples are immutable dummy!')

del drink

try:
    print(drink)
except(NameError):
    print('DUH ... you just deleted the tuple named drink')

# A Set is a collection which is unordered and unindexed. No duplicate members.

my_set = {'Ben Nevis', 'Crib Goch', 'Mont Blanc'}
print('Ben Nevis' in my_set)

my_set.remove('Mont Blanc')
print(len(my_set))

print(f'the contents of my_set before clearing: {my_set}')
my_set.clear()
print(f'the contents of my_set after clearing: {my_set}')