# Definition: A list is an ordered, mutable collection of items.

# Properties:
# Ordered
# Mutable
# Allows duplicate elements

mylist = [1, 2, 3, 4, 5]  # Syntax of list using []
anotherlist = list(range(2, 101, 2))

# Operations of List in Python
# 1) Access Elements from mylist
print("on 3rd index we have ", mylist[3])  # reference operator []
print("on 0th index we have ",mylist[0])
print(mylist[2:4])
print("on Last index we have ",mylist[-1])

# 2) Modifying the Element
# Because Lists are mutable we can Modify the list
mylist[3] = 400

# 3) printing the list
# 2 ways of printing lists or any collection in python
# 1st way:
print(mylist)
# 2nd way:
for i in mylist:
    print(i, end=" ")
print()

# 4) adding the elements to a list
# append()  it will add an element at the last of the list
mylist.append(6)
mylist.append(7)
for i in range(8, 11):
    mylist.append(i)
print(mylist)

# insert()  it will add the element at the particular index
mylist.insert(6, 5000)
mylist.insert(3, "CodersArcade")
mylist.insert(11, "HII")
print(mylist)

# 5) Removing an element from the list
mylist.remove(5000)
mylist.pop()
del mylist[3]
print(mylist)

# 6) other functions
print(len(mylist))  # this will give u the length of the list
mylist.sort(reverse=True)  # this will sort the elements in the list
print(mylist)


print(anotherlist)
