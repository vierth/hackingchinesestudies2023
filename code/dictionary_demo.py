# dictionaries let you store information using a key value pair

# create an empty dictionary
my_dictionary = {}
my_dictionary = dict()

# create a dictionary with some values:
ages = {"Paul":39, "Padma":25, "gorp": 155}

# dictionaries have no inherent order
print(ages)

# get values from dictionary with square brackets
pv = ages["Paul"]
print(pv)

# add a value to the dictionary
ages["blobo"] = 45
print(ages)

# print(ages['yawn'])
print(ages.keys())
print(ages.values())

for name, age in ages.items():
    print(name, age)

# for key, val in zip(ages.keys(), ages.values()):
#     print(key, ages[key])