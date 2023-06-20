# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

person = {
    'first_name': 'Van',
    'last_name': 'Morrison',
    'age': 77
}

print(person['age'])
print(person.get('first_name'))
person['occupation'] = 'singer-songwriter'

for key in person:
    print(key + ': ' + str(person[key]))

print(person.keys())

person['songs'] = ['Brown Eyed Girl', 'Slim Slow Slider', 'Crazy Love']

clone = person
copycat = person.copy()

person['songs'].append('Moondance')
print(person)
print(copycat) # A shallow copy

copycat.pop('songs')
print(copycat) 
print(len(copycat))
