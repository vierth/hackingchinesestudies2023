import re

# \d  matches a number 0 to 9
result = re.search(r'\d', 'It is the year 2023.')
print(result)

# \D match anything that is not a number
result = re.search(r'\D', 'It is the year 2023.')
print(result)

# \s matches a whitespace
result = re.search(r'\s', 'It is the year 2023')
print(result)

# \S matches NOT a whitespace
result = re.search(r'\S', 'It is the year 2023')
print(result)

# there are other whitespace characters
# \n new line
# \t tab character

# \w matches letters or numbers
result = re.search(r'\w', 'It is the year 2023')
print(result)

# \W matches not letters or numbers
result = re.search(r'\W', 'It is the year 2023')
print(result)

# . This matches everything EXCEPT new lines
result = re.search(r'.', 'It is the year 2023.')
print(result)

# \b matches a word boundary
result = re.search(r'\bship', "My spaceship is a ship.")
print("my spaceship is a ship".find("ship"))
print(result)

# ? makes something optional
result = re.search('humou?r', "this is how brits spell humour")
print(result)

# + Used in conjunction with something else to search for something one or more times
result = re.search(r'\d+', 'It is the year 2023.')
print(result)

# * Find something that occurs zero or more times
result = re.search(r'humou*r', 'humor')
print(result)

# * Find something that occurs zero or more times
result = re.search(r'humou*r', 'humouuuur')
print(result)

# * Find something that occurs zero or more times
result = re.search(r'humou*r', 'humour')
print(result)