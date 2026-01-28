# initialising list
integers = [1, 2, 3]

# printing its type
print(f"The {integers} object is of type {type(integers)}")

# converting list using iter()
iterator = iter(integers)

# and printing its type
print(f"The {iterator} object is of type {type(iterator)}")

# using next() to print iterator values
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator)) # error