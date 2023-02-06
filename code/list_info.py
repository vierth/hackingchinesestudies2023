# lists hold zero or more elements in a specific order
# we can create lists in at least two ways
my_list = []
another_list = list()

integer_list = [1, 3, 4, 6, 9]

# lists in python can contain any pthon object
string_list = ["my", "nmae", "is", "paul", "vierthaler"]

# python allows different kinds of data in a list
mixed_list = [2, 'one', 5.4, "hello"]

# lists can contain lists
nested_list = [[1,2], [2,4], [8,9]]

# getting info is just like strings
print(string_list[0]) # last item -1

# If we try to get an item beyond the end of the list
# we get an error
# string_list[100]

print(string_list[1:3])

# check the length of a list
len(string_list)

# we can add things to a list with append
string_list.append("hello")
print(string_list)

# remove the last item from a list
deleted_word = string_list.pop()
print(string_list)
print(deleted_word)

# remove item at index
string_list.pop(1)
print(string_list)

# insert item at index
string_list.insert(1, "name")
print(string_list)

# change item at index
string_list[2] = "captain"
print(string_list)