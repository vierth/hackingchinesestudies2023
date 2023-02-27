import nltk

with open('analects.txt', 'r', encoding="utf8") as rf:
    analects = rf.read()

analects = analects[analects.find("CONFUCIAN ANALECTS."):analects.find("End of Project Gutenberg Etext")]

analects_tokens = nltk.word_tokenize(analects)

filtered_tokens = [token.lower() for token in analects_tokens if token.isalnum()]

length_of_analects = len(filtered_tokens)
print(f"The Analects is {length_of_analects} words long.")

unique_words = set(filtered_tokens)
print(f"The Analects contians {len(unique_words)} unique words")

lex_div = len(unique_words)/length_of_analects
print(f"It's lexical diversity is {lex_div:.3f}")

stopwords = list(nltk.corpus.stopwords.words('english'))
no_stopword_analects =[token for token in filtered_tokens if token not in stopwords]

