# Python contains many useful methods that tell us about
# the contents of our variables.
# The first method we'll talk about is
# count()
greeting = "Hello, how are you today?"

# count the number of a's in this sentence
a_frequency = greeting.count("a")
print(a_frequency)

# search for a string by using a variable
my_search_term = "e"
my_search_results = greeting.count(my_search_term)
print(my_search_results)