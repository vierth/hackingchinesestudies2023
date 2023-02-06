# if statements are useful when executing code on a conditional
# basis.
# we use a code block to this.
# in python code blocks start with a colon (:) and are indicated
# with tabs

if 10 < 20:
    print("this is true")

if 10 > 20:
    print("this will never run")

print('and the code continues')

# if else statements allow you to eexecute a different block of
# code if the first statement is false
if 30 < 20:
    print("This isn't ture and should never run")
else:
    print("Good, because 30 is not less than 20")

# elif lets us add multiple conditions
if 10 > 10:
    result = "10 is larger than 10"
elif 10 == 10:
    result = "10 is equal to 10"
elif 10 < 10:
    result = "10 is smaller than 10"
else:
    result = "everything is meaningless"

print(result)

# so be careful of situations like this:
a = 10

if a > 1:
    print("a is closest to 1")
elif a > 5:
    print("a is clostest to 5")
elif a == 10:
    print("a is 10")