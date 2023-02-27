# you can return part of hte match with groups
import re

# groups are rformed with ()
some_html = "<a href='www.yahoo.com'>"
some_more_html = "<div summary='www.google.com'>"

r'www\..+\.com'
result = re.search(r"<a href='(.+)'>", some_more_html)
print(result)
print(result.group(1))

my_string = "This occured on pages 336-338"
result = re.search(r'(\d+)-(\d+)', my_string)
print(result.group(1), result.group(2))
print(result.groups())