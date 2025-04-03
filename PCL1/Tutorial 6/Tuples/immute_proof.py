# No need to understand try/except statements. Just run the file

my_tuple = (1, 2, 3)
try:
    my_tuple[1] = 4  # This will raise an error
except TypeError as e:
    print("Error:", e)
