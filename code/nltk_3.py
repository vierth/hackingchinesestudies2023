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

# combined sentence and word tokenization
# creater an enmoty list for the results
sentence_word_tokens = []

sentences = nltk.sent_tokenize(analects)

for sentence in sentences:
    words = nltk.word_tokenize(sentence)
    sentence_word_tokens.append(words)

print(sentence_word_tokens[100:110])

s_w_tokens = [nltk.word_tokenize(sentence) for sentence in nltk.sent_tokenize(analects)]

sentences = ["." for sentence in nltk.sent_tokenize(analects)]

nums = ["_" for i in range(10)]

