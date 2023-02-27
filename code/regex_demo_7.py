# some operators in regex are "Greedy"
# + is greedy, matches longest pattern
# * is greedy, matches longest pattern
# +? is not greedy, matches shortest patter

import re

my_string = "arglebargle"
result = re.search(r'a.+e', my_string)
print(result.group())

result = re.search(r'a.+?e', my_string)
print(result.group())

my_html = "<div> This is a little bit of html</div>"
result = re.search(r'<.+?>', my_html)
print(result)