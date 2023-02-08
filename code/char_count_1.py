# this program calculates the most common character in a string

my_string = "In the year 1878 I took my degree of Doctor of Medicine of the University of London, and proceeded to Netley to go through the course presecripjdlakfj;aovpieujralm/ekdf/a."

# create empty string for character
most_common_character = ""
# create tracker for how often character occurs
most_common_frequency = 0

# use a for loop to go through each character
for char in my_string:
    char_frequency = my_string.count(char)

    # if char_frequency is greater than most_common_frequency then this char
    # is the most frequent character
    if char_frequency > most_common_frequency:
        most_common_frequency = char_frequency
        most_common_character = char

print(f'THe most common chracter is {most_common_character}: {most_common_frequency}')