# regular expressions will let us search for patterns within text
import re

# we can use them like regular search terms
my_string = 'hello, how are you?'

result = re.search('ello,  how', my_string)

print(result)

# get the string result
print(result.group())

# get the start of hte match, end of the match, and span
print(result.start())
print(result.end())
print(result.span())
