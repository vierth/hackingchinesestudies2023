import re

# if we want specify that something happens 3
# we do so with curly brackets 
# {3}

result = re.search(r'a{3}', 'Will we match a or aaa')
print(result)

# match something {,3} zero to 3
# match something 3 or more times {3,}
# match somethin 3 to 7 times {3, 7}
r'\d{4}'