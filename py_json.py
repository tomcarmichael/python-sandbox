# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

user_json = '{"first_name": "John", "last_name": "Lennon"}'

user = json.loads(user_json)

print(user)
print(user['first_name'])

person = '{"first_name": "Van", "last_name": "Morrison", "age": "77"}'

person_json = json.dumps(person)

print(person_json)
