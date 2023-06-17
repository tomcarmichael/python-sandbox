# A List is a collection which is ordered and changeable. Allows duplicate members.

numbers = [1, 2, 3]

other_list = list((1, 2, 3))
print(numbers, other_list, type(numbers), type(other_list))

veg = ['aubergine', 'fennel', 'celeriac']
print(len(veg))

veg.append('potato')
print(veg)

veg.remove('fennel')

veg.reverse()
print(veg)

veg.sort(reverse=True)
print(veg)

copy_veg = veg

veg[1] = 'kale'
print(copy_veg, copy_veg == veg)