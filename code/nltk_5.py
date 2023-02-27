import nltk
import matplotlib.pyplot as plt

# open the analects
with open("analects.txt", 'r', encoding='utf8') as rf:
    analects = rf.read()

# find start of text
start_point = analects.find("CONFUCIAN ANALECTS.")
# find end of text
end_point = analects.find("End of Project Gutenberg Etext")

# clean text
analects = analects[start_point:end_point]

# tokenize text into words
tokens = nltk.word_tokenize(analects)

# clean up this list of tokens
filtered_tokens = []
for token in tokens:
    if token.isalnum():
        filtered_tokens.append(token.lower())

# filtered_tokens = [token.lower() for token in tokens if token.isalnum()]

# Create a Text Object
analects_text = nltk.Text(filtered_tokens)

print("words in the analects similar to 'government'")
analects_text.similar('government')

# make a lexical dispersion plt
# give it a list of words, and see where they occur iwthin the text
analects_text.dispersion_plot(["rites", "ritual", "government"])

plt.show()

# getting collocations
analects_text.collocations()

frequencies = nltk.FreqDist(analects_text)
print(frequencies['and'])

print(frequencies.most_common(10))