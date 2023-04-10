import gensim, nltk, os
import plotly.express as px
import pandas as pd
import numpy as np

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

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

def plot_topic(topic_num, topn=20):
    topic_data = {"words":[], "weights":[]}

    for word, weight in lda.show_topic(topic_num, topn=topn):
        topic_data["words"].append(word)
        topic_data["weights"].append(weight)

    df = pd.DataFrame(topic_data)

    fig = px.bar(df, x="words", y="weights")
    fig.show()

plot_topic(8, topn=15)


doc_lda = lda.get_document_topics(processed_corpus[0], minimum_probability=0.0)
doc_data = {"topic_num":[d[0] for d in doc_lda], "topic_weight":[d[1] for d in doc_lda]}
doc_df = pd.DataFrame(doc_data)
fig = px.bar(doc_df, x="topic_num", y="topic_weight")
fig.show()


# look at topic prevelance across full corpus
# get all topics
all_doc_topics = [lda.get_document_topics(processed_corpus[i],minimum_probability=0.0) for i in range(len(processed_corpus))]

corpus_lda = np.sum(np.array(all_doc_topics), axis=1)
corpus_data = {"topic_num":[i for i in range(10)], "topic_weight":corpus_lda}
corpus_df = pd.DataFrame(corpus_data)
fig = px.bar(corpus_df, x="topic_num", y="topic_weight")
fig.show()