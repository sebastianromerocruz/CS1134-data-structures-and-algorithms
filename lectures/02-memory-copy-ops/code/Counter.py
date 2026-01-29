"""
Print function functionality
- If you want to print multiple things in one line, use the the following:
    print(value_1, value_2, value_3, ..., value_x, value_y, value_z)
    These will be printed separated by a single space by default
    "The print function is printing values of three arguments"
- String concatenation
- sep parameter
- end parameter: by default, print adds a newline character at the end
"""
area_code = 917
first_part = 123
second_part = 4567

print("Area code:", area_code, end="\n-------------\n", sep='/')
print("First:", first_part)
print("Second:", second_part)