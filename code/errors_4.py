my_dict = {"hello":"jim", "goodbye":"tim"}

try:
    my_dict["jim"]
except KeyError:
    print("jim is not in dictionary")