import re

my_string = "This string 2023 has many numbers 18, 1572, and 2021."

# findall
results = re.findall(r'\d+', my_string)
print(results)

# finditer
results = re.finditer(r'\d+', my_string)

for r in results:
    print(r)