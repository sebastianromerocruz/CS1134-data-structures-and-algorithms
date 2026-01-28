"""
We simulate the following for-loop:

string = "abc"

for char in string:
    print(char)
"""
string = "abc"
str_iterator = iter(string)
is_done = False  # flag to stop loop

# while we still have characters...
while not is_done:
    try:
        # attempt to SAFELY expose the next character
        char = next(str_iterator)
    except StopIteration:
        # unless we're done, in which case end loop
        is_done = True
        continue

    # otherwise, simple print the character
    print(char)