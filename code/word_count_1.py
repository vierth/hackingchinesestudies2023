# this program calculates the most common character in a string

my_string = "In the year 1878 aaaaaaaaaaaaaaI took my degree of Doctor of Medicine of the University of London, and proceeded to Netley to go through the course presecripjdlakfj;aovpieujralm/ekdf/a."
my_string = my_string.lower()

my_string_words = my_string.split(" ")

# if i use list instead of a string, i can save more than one value
most_common_word = []
# create tracker for how often character occurs
most_common_frequency = 0

unique_words = set(my_string_words)
print(unique_words)
# use a for loop to go through each character
counter = 0
for word in unique_words:
    counter += 1
    word_frequency = my_string_words.count(word)
    
    # if char_frequency is greater than most_common_frequency then this char
    # is the most frequent character
    if word_frequency > most_common_frequency:
        most_common_frequency = word_frequency
        most_common_word = [word]
    elif word_frequency == most_common_frequency:
        most_common_word.append(word)

        

print(f'The most common word is {most_common_word}: {most_common_frequency}')