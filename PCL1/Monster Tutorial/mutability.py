def demonstrate_mutability():
    print("=== PYTHON TYPE MUTABILITY DEMONSTRATION ===\n")
    
    # 1. Numbers (Immutable)
    print("1. NUMBERS (Immutable)")
    integer = 42
    print(f"Integer before:", integer, f"(id: {id(integer)})")
    integer += 1
    print(f"Integer after:", integer, f"(id: {id(integer)})")
    
    try:
        # Numbers don't support item assignment
        integer[0] = 5
    except TypeError as e:
        print(f"Error when trying to modify integer directly: {e}")
    
    float_num = 3.14
    print(f"\nFloat before:", float_num, f"(id: {id(float_num)})")
    float_num += 0.01
    print(f"Float after:", float_num, f"(id: {id(float_num)})")
    
    try:
        # Floats don't support item assignment
        float_num[0] = 5.0
    except TypeError as e:
        print(f"Error when trying to modify float directly: {e}")
    
    # 2. Strings (Immutable)
    print("\n2. STRINGS (Immutable)")
    text = "hello"
    print(f"String before:", text, f"(id: {id(text)})")
    text += " world"
    print(f"String after:", text, f"(id: {id(text)})")
    
    try:
        # Strings don't support item assignment
        text[0] = 'H'
    except TypeError as e:
        print(f"Error when trying to modify string directly: {e}")
    
    # 3. Tuples (Immutable)
    print("\n3. TUPLES (Immutable)")
    tup = (1, 2, 3)
    print(f"Tuple:", tup)
    
    try:
        tup[0] = 5
    except TypeError as e:
        print(f"Error when trying to modify tuple: {e}")
    
    # 4. Lists (Mutable)
    print("\n4. LISTS (Mutable)")
    lst = [1, 2, 3]
    print(f"List before:", lst, f"(id: {id(lst)})")
    lst.append(4)
    print(f"List after append:", lst, f"(id: {id(lst)})")
    lst[0] = 100
    print(f"List after modification:", lst, f"(id: {id(lst)})")
    
    # 5. Dictionaries (Mutable)
    print("\n5. DICTIONARIES (Mutable)")
    dict_example = {'a': 1, 'b': 2}
    print(f"Dict before:", dict_example, f"(id: {id(dict_example)})")
    dict_example['c'] = 3
    print(f"Dict after adding key:", dict_example, f"(id: {id(dict_example)})")
    dict_example['a'] = 100
    print(f"Dict after modifying value:", dict_example, f"(id: {id(dict_example)})")
    
    # 6. Sets (Mutable)
    print("\n6. SETS (Mutable)")
    set_example = {1, 2, 3}
    print(f"Set before:", set_example, f"(id: {id(set_example)})")
    set_example.add(4)
    print(f"Set after adding element:", set_example, f"(id: {id(set_example)})")
    
    # 8. Bytes (Immutable)
    print("\n8. BYTES (Immutable)")
    bytes_example = b'hello'
    print(f"Bytes:", bytes_example)
    
    try:
        bytes_example[0] = 65
    except TypeError as e:
        print(f"Error when trying to modify bytes: {e}")

if __name__ == "__main__":
    demonstrate_mutability()