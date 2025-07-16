# Dictionary is a type of collection in python,
# Which is mutable means I can add or remove ,or I can do
# Any operation into the dictionary

# Definition: A dictionary is an unordered collection of key-value pairs.

# Properties:
# Unordered (Python 3.7+ maintains insertion order)
# Mutable
# Keys are unique
# Basic Operations:

dict1 = {
        'name': 'samarth',
        'age': 18,
        'city': 'Bangalore'
        }

dict2 = {
        'name': 'preethi',
        'age': 24,
        'city': 'Bangalore'
        }

dict3 = {
        'names': ['samarth', 'preethi'],
        'ages': [18, 24],
        'cities': ['bangalore', 'bangalore'] }

# printing the dictionaries and accessing the vales in it
print(dict1)
print(dict2['name'])

# adding a value into a dictionary
dict1['job'] = 'Student'
dict2['job'] = 'Student'

print(dict1)

# Removing a element
# 1) pop()
# 2) popitem()
# 3) del
# 4) clear()

# 1) POP()
dict1.pop('city')
print(dict1)

# age = dict1.pop('age')
# print(age)
# print(dict1)

# 2) POPITEM()
# popitem() will delete the latest key entered
# in the dict1
dict1.popitem()
print(dict1)

# 3) del key
del dict2['city']
print(dict2)

# 4) clear()
dict3.clear()
print(dict3)

# Dictionary functions
# 1) keys()
# 2) values()
# 3) items()
# 4) get(key)
# 5) update()

mydict = {
        'name': 'Ashank',
        'age': 30,
        'city': 'Jhansi'
        }

keys = mydict.keys()
print(type(keys))
for i in keys:
    print(i)
print(list(keys))
print(keys)

values = mydict.values()
print(type(values))
for i in values:
    print(i)

print(values)

items = mydict.items()
print(type(items))
for i in items:
    print(i)

print(items)

print(mydict.get('name'))
print(mydict.get('city'))
print(mydict.get('job'))

mydict.update({'city': 'Bangalore'})
print(mydict)

dictionary = {}
numItems = int(input("Enter How many elements u want?"))
for i in range(numItems):
    key = input('Enter a Key: ')
    value = input('Enter a Value: ')
    dictionary[key] = value

print("The Dictionary is: ", dictionary)