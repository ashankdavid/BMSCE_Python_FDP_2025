# Definition: A set is an unordered collection of unique elements.

# Properties:
# Unordered
# Mutable
# Does not allow duplicate elements

my_set = {1, 2, 3, 4}
print(my_set)

my_set.add(5)
print(my_set)
my_set.remove(2)  # Raises an error if the element is not present
print(my_set)
my_set.discard(2)  # Does not raise an error if the element is not present
print(my_set)
my_set.pop()  # Removes and returns an arbitrary element
print(my_set)
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union = set_a | set_b  # {1, 2, 3, 4, 5}
intersection = set_a & set_b  # {3}
difference = set_a - set_b  # {1, 2}



