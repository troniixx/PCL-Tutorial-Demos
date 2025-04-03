my_set = {1, 2, 3, 5}
print("My set:", my_set)

mixed_set = {1, "Hello", 3.14}
print("Mixed set:", mixed_set)

my_set.add(4)
print("After adding 4:", my_set)
my_set.remove(2)
print("After removing 2:", my_set)

set_a = {1, 2, 3}
set_b = {3, 4, 5}

union_set = set_a | set_b
intersection_set = set_a & set_b
difference_set = set_a - set_b

print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference:", difference_set)

my_list = [1, 2, 2, 3, 4, 4, 5]
unique_set = set(my_list)
print("Unique elements:", unique_set)

