import re
# we can match one thing or another with|
print(re.search(r'cat|dog|rat', "I like rat"))

# we can replace characters easily
my_string = "My      name  is Paul Vierthaler"
my_string = re.sub(r'\s+', " ", my_string)
print(my_string)

old_string = "My bname is P.  I use two space.  After every period.   Wow"
old_string = re.sub(r'\.\s+', '. ', old_string)
print(old_string)

my_string_2 = "Oh Captain, my Captain. Are you a General?"

# \g<1> : insert group 1 into result
#  \g<2> : insert group 2 into result
with_tags = re.sub(r'(Captain|General)', "<tag>\g<1></tag>", my_string_2)
print(with_tags)