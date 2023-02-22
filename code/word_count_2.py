# this program calculates the most common character in a string

my_string = "In the year 1878?!!! aaaaaaaaaaaaaaI took my degree of Doctor of Medicine of the University of London, and proceeded to Netley to go through the course presecripjdlakfj;aovpieujralm/ekdf/a."
my_string = my_string.lower().replace(",", "").replace(".", "")

delete_items = ["?", "!", ".", ","]
for item in delete_items:
    my_string = my_string.replace(item, "")

my_string_words = my_string.split(" ")

# create a dictionary to track the count of the words
word_counter = {}

unique_words = set(my_string_words)

# use a for loop to go through each character
for word in unique_words:
    word_counter[word] = my_string_words.count(word)

sorted_word_counter = sorted(word_counter, key=word_counter.get, reverse=True)    

# lets print words in order with their frequency
for word in sorted_word_counter[0:10]:
    print(word, word_counter[word])

print(sorted_word_counter[:10])
