my_string = "Hello, my name is Paul Vierthaler name"

# return where name occurs
result = my_string.find('name')

print(result)

# if the search term is not found it returns -1
no_result = my_string.find('how')
print(no_result)