# loops allow for code to be executed many times
i = 0

# while i < 10:
#     print(i, "is not yet 10")
#     # i = i + 1
#     i += 1

# functionally the same with a for loop\
for i in range(10):
    print(i)

# # we can expand this range function a bit
for i in range(0, 10, 2):
    print(i, "is not yet 10")

my_list = ["a", "b", "c", "d"]

for letter in my_list:
    print(letter)

my_string = "chugalug"

for char in my_string:
    print(char)