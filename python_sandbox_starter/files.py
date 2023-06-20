# Python has functions for creating, reading, updating, and deleting files.

new_file = open('my_file.txt', 'w')

print(f'new_file is stored locally as {new_file.name}')
print(f'Is closed? {new_file.closed}\nOpening mode: {new_file.mode}')

new_file.write('Python is pretty, pretty good\n')
new_file.close()

new_file = open('my_file.txt', 'a')
new_file.write('Its not so different from Ruby...')
new_file.close()

new_file = open('my_file.txt', 'r')
first_word = new_file.read(7)
print(first_word)

full_text = new_file.read()
print(full_text)
new_file.close()
