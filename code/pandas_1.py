import pandas as pd
from pandas import Series
import nltk


number_list = [1, 2, 3, 4, 5, 6]
my_series = Series(number_list)

with open("analects.txt", "r", encoding='utf8') as rf:
    text = rf.read()

word_tokens = nltk.word_tokenize(text)

word_series = Series(word_tokens)
word_counts = word_series.value_counts()

series_index = word_counts.index

print(word_counts["humanity"])
print(word_counts[0])

print(word_counts.get("iguana"))

print(word_counts * 2)

print(word_counts + word_counts)