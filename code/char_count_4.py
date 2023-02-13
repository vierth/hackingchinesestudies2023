# this program calculates the most common character in a string

my_string = "In the year 1878 aaaaaaaaaaaaaaI took my degree of Doctor of Medicine of the University of London, and proceeded to Netley to go through the course presecripjdlakfj;aovpieujralm/ekdf/a."
my_string = my_string.lower()
# if i use list instead of a string, i can save more than one value
most_common_character = []
# create tracker for how often character occurs
most_common_frequency = 0

unique_characters = set(my_string)

# use a for loop to go through each character
counter = 0
for char in unique_characters:
    if char != " ":
        counter += 1
        char_frequency = my_string.count(char)
        
        # if char_frequency is greater than most_common_frequency then this char
        # is the most frequent character
        if char_frequency > most_common_frequency:
            most_common_frequency = char_frequency
            most_common_character = [char]
        elif char_frequency == most_common_frequency:
            most_common_character.append(char)

        

print(f'The most common chracter is {most_common_character}: {most_common_frequency}')