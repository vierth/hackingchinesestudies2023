import gensim, nltk, os

titles = []
texts = []
for root, dirs, files in os.walk('fedpapers'):
    files = [file for file in files if file[0] != '.']
    for f in files:
        with open(os.path.join(root, f), 'r', encoding='utf8') as rf:
            text = rf.read()
            texts.append(text)
            titles.append(f[:-4])

lemmatizer = nltk.WordNetLemmatizer()

refined_texts = []
for text in texts:
    tokenized_text = nltk.word_tokenize(text)
    refined = [lemmatizer.lemmatize(word).lower() for word in tokenized_text if word.isalnum()]
    refined_texts.append(refined)

corpus_dictionary = gensim.corpora.Dictionary(refined_texts)
# no below: term must appear in at least 5 documents
# no above: term cannot appear in more than 70 percent of documents
corpus_dictionary.filter_extremes(no_below=5, no_above=0.7)

# prep corpus for gensim
processed_corpus = [corpus_dictionary.doc2bow(text) for text in refined_texts]

# gensim.corpora.Mmcorpus.serialize('mycorpus.mm', processed_corpus)
# gensim.corpora.Mmcorpus('mycorpus.mm')

lda = gensim.models.ldamodel.LdaModel(
    processed_corpus, num_topics=10, id2word=corpus_dictionary, iterations=500, passes=50
)

topics = lda.show_topics()
for topic in topics:
    print(topic)