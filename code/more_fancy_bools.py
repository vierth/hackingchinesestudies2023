i = 6

# to evaluate to True all statements MUST be true
if i < 10 and i > 5:
    print("i is less than 10 and greater than 5")

# to evaluate to True or statements can be either or
if i > 10 or i < 5:
    print("matched criteria")

# you can use parantheses to control order evaluation
if (i > 5 and i < 10) or i > 100:
    print("matches")