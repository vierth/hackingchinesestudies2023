# We can turn strings into lists very easily
name = "My name is Paul Vierthaler"

name_as_list = list(name)
print(name_as_list)

# turn string into list of words
name_as_words = name.split(" ")
print(name_as_words)

print(name.split("is"))

new_string = "|".join(name_as_words)
print(new_string)

min([1, 4, 8, -9])
max([1, 4, 8, -9])

int_list = [1, 4, 8, -9]
# to sort a list in place
int_list.sort()
int_list.sort(reverse=True)

# in place if you like
print(sorted(int_list, reverse=True))
 
print(int_list)