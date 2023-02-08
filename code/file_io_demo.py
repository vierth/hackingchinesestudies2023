# reading and writing to files is important in python

# write to file
# be very careful
# this creates a new file if none exists
# it deletes and overwrites a file if it does exist
# write_file = open("demo.txt", "w", encoding="utf8") 
# write_file.write("Writing to file!!!!!!!!")
# write_file.write("More stuff to put in file")
# write_file.close()

with open('demo.txt', 'w', encoding="utf8") as write_file:
    write_file.write("write stuff to file.")

with open('demo.txt', 'a', encoding="utf8") as append_file:
    append_file.write("\nwrite more stuff to file")

print("done writing to file")

with open('demo.txt', 'r', encoding="utf8") as read_file:
    text = read_file.read()

print(text)
