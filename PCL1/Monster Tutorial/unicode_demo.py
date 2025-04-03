def hex_and_unicode_demo():
    print("=== HEXADECIMAL AND UNICODE DEMONSTRATION ===\n")
    
    # 1. Basic Hex Numbers
    print("1. Hexadecimal Basics:")
    hex_numbers = {
        10: 0xA,
        15: 0xF,
        16: 0x10,
        26: 0x1A,
        255: 0xFF,
        256: 0x100
    }
    
    for decimal, hex_val in hex_numbers.items():
        print(f"Decimal: {decimal}")
        print(f"  Hex (using 0x): {hex_val}")
        print(f"  Hex (using hex()): {hex(decimal)}")
        print(f"  Hex (formatted): {decimal:02X}")
        print()
    
    # 2. Unicode and Hex
    print("\n2. Unicode and Hexadecimal Representation:")
    characters = {
        'A': 0x41,      # Latin Capital A
        'Z': 0x5A,      # Latin Capital Z
        'a': 0x61,      # Latin Small A
        'z': 0x7A,      # Latin Small Z
        '0': 0x30,      # Digit Zero
        '9': 0x39,      # Digit Nine
        '£': 0xA3,      # Pound Sign
        '€': 0x20AC,    # Euro Sign
        '😀': 0x1F600   # Grinning Face
    }
    
    for char, code in characters.items():
        print(f"Character: {char}")
        print(f"  Unicode Code Point: U+{code:04X}")
        print(f"  Hex: {hex(code)}")
        print(f"  Decimal: {code}")
        print(f"  UTF-8 Bytes: {char.encode('utf-8').hex(' ')}")
        print()
    
    # 3. Working with Hex in Bytes
    print("\n3. Hex in Bytes and Conversions:")
    # Create bytes from hex string
    hex_string = "48 65 6C 6C 6F"  # "Hello" in hex
    bytes_from_hex = bytes.fromhex(hex_string)
    print(f"Hex string: {hex_string}")
    print(f"As bytes: {bytes_from_hex}")
    print(f"As string: {bytes_from_hex.decode('ascii')}")
    
    # Convert string to hex bytes
    text = "Hello, World!"
    hex_bytes = text.encode('utf-8').hex(' ')
    print(f"\nOriginal text: {text}")
    print(f"As hex bytes: {hex_bytes}")
    
    # 4. Hex Color Examples
    print("\n4. Hex Colors:")
    colors = {
        'Red': '#FF0000',
        'Green': '#00FF00',
        'Blue': '#0000FF',
        'White': '#FFFFFF',
        'Black': '#000000',
        'Purple': '#800080'
    }
    
    for color, hex_code in colors.items():
        # Convert hex color to RGB
        rgb = tuple(int(hex_code[i:i+2], 16) for i in (1, 3, 5))
        print(f"Color: {color}")
        print(f"  Hex: {hex_code}")
        print(f"  RGB: {rgb}")
        print()

    # 5. Advanced Unicode Examples
    print("\n5. Advanced Unicode and Hex:")
    # Show different script systems
    scripts = {
        'Latin': 'Hello',
        'Greek': 'Γειά σου',
        'Cyrillic': 'Привет',
        'Arabic': 'مرحبا',
        'Devanagari': 'नमस्ते',
        'Chinese': '你好',
        'Japanese': 'こんにちは'
    }
    
    for script, text in scripts.items():
        print(f"\n{script} Script: {text}")
        print("Character codes:")
        for char in text:
            print(f"  '{char}': U+{ord(char):04X}")
            print(f"    UTF-8: {char.encode('utf-8').hex(' ')}")
            
    # 6. Hex Math Operations
    print("\n6. Hexadecimal Mathematics:")
    a = 0xFF    # 255
    b = 0x0F    # 15
    
    print(f"a = 0xFF ({a})")
    print(f"b = 0x0F ({b})")
    print(f"a + b = 0x{a + b:02X} ({a + b})")
    print(f"a - b = 0x{a - b:02X} ({a - b})")
    print(f"a * b = 0x{a * b:02X} ({a * b})")
    print(f"a / b = {a / b:.2f}")
    print(f"a & b = 0x{a & b:02X} ({a & b})")  # Bitwise AND
    print(f"a | b = 0x{a | b:02X} ({a | b})")  # Bitwise OR
    print(f"a ^ b = 0x{a ^ b:02X} ({a ^ b})")  # Bitwise XOR

if __name__ == "__main__":
    hex_and_unicode_demo()