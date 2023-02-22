import nltk

# open the analects
with open("analects.txt", 'r', encoding='utf8') as rf:
    analects = rf.read()

# find start of text
start_point = analects.find("CONFUCIAN ANALECTS.")
# find end of text
end_point = analects.find("End of Project Gutenberg Etext")

# clean text
analects = analects[start_point:end_point]

# NLTK comes with a variety of tools to hoelp us tokenize the text
# Sentence tokenizer
sentences = nltk.sent_tokenize(analects)

# word tokenizer
words = nltk.word_tokenize(analects)
print(words[100:110])

