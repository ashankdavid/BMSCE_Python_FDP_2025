# Definition: A tuple is an ordered, immutable collection of items.

# Properties:
# Ordered
# Immutable
# Allows duplicate elements

myTuple = (1, 2.5, "Coders", 'a', 5, "Coders", "Coders")
anotherTuple = tuple(range(10))

# accessing elements in tuples
print(myTuple[0])
print(myTuple[1:3])
print(myTuple[-2])

# Operations on Tuples
# 1) Concatenating of 2 tuples using + operator
tuple1 = (1,2,3)
tuple2 = (4,5,6)
resultTuple = tuple1 + tuple2
print(resultTuple)

# 2) Repetition of tuples
originalTuple = (1,2,3)
repeatedTuple = originalTuple * 3
print(repeatedTuple)

# 3) Membership of element in a tuple
sampleTuple = (1,2,3,4,5)
print(3 in sampleTuple)
print(10 in sampleTuple)
print(3 not in sampleTuple)
print(10 not in sampleTuple)

# Length of a tuple
Length = len((1,2,3,4,5,8,6))
print(Length)

# Indexing (Finding the index of an element in a tuple)
index = myTuple.index("Coders")
print(index)

# Counting (Counting the number of occurance of an element in a tuple)
count = myTuple.count("Coders")
print(count)

# Note - There are only 2 inbuilt tuple functions - index and count
# why? - because tuples are immutable, they cannot be modified
# sooo we have a very limited options in tuples

# Once the Tuple is created u cannot change anything into it
# This is Tuples