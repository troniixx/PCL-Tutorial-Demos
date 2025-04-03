def find_element(nested, value):
    for sublist in nested:
        if value in sublist:
            return True
    return False


nested_list = [[3, 2], [1, 4], [5, 0]]
print("Is 5 in the nested list?", find_element(nested_list, 5))

nested_list = [[1, 2, 3],
                [4, 5, 6], 
                [7, 8, 9]]

nested_list_alpha = [["world"],
                ["hello"], 
                [7, 8, 9]]

print("First sublist:", nested_list[0])
print("Element at [1][2]:", nested_list[1][0])  # Output: 6

print("First sublist in nested alpha list:", nested_list_alpha[0])
print("First word in alpha list:", nested_list_alpha[0][0])
print("First letter in alpha list:", nested_list_alpha[0][0][0])
