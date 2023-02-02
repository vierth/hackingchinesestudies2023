# sometimes we might want to check how long strings are
my_string = "Hello, my name is Paul Vierthaler"

string_length = len(my_string)
print(string_length)

print(len(my_string))

# sometimes we might want to get a small part of a string
# indexes for strings and other python objects start at 0
# indices are called up using []
print(my_string[0])

# get the last character we can use negative numbers
print(my_string[-1])
print(my_string[len(my_string)-1])

# print first ten characters
print(my_string[:10])

# 4 to 11
print(my_string[4:10])

# character 8 to the end
print(my_string[8:])
