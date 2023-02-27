import re

# character sets are created with square brakets
result = re.search(r'[abc]', 'can you run this restaurant')
print(result)

# match ranges
r'[a-e]'
r'[0-9]' # matches numbers equals \d
r'[a-zA-Z]'
r'[a-zA-Z0-9]' # equivelant to \w

# match not a
r'[^a]'

# match a literal .
# \.
# \+
# \*