import os, nltk, re
import hanziconv

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances
from scipy.cluster.hierarchy import linkage, dendrogram

import matplotlib.pyplot as plt

color_dict = {"xiyouji":"green", "jinpingmei":"magenta", "sanguo":"grey", "shuihu":"purple"}

def clean(text):
    text = hanziconv.HanziConv.toSimplified(text)
    text = re.sub(r'\s+', "", text)
    text = re.sub(r'\n', '', text)
    return text

def chunk(text, length=10000):
    loops = len(text)//length
    return [text[i*length:(i+1)*length] for i in range(loops)]

def div_chapter(text):
    return re.split(r'第[一二三四五六七八九十百]+回', text)

ignore_files = set(["LICENSE.txt", ".DS_Store",".git_ignore"])

titles = []
texts = []
for root, dirs, files in os.walk('novels'):
    files = [f for f in files if f not in ignore_files]
    for f in files:
        with open(os.path.join(root, f),'r', encoding='utf8') as rf:
            text = rf.read()
        text = clean(text)
        chunks = div_chapter(text)
        print(len(chunks))
        texts.extend(chunks)
        chunk_titles = [f[:-4] for i in range(len(chunks))]
        print(len(chunk_titles))
        titles.extend(chunk_titles)

vectorizer = TfidfVectorizer(use_idf=False, max_features=100, analyzer="char")
counts = vectorizer.fit_transform(texts)

# let's measure the similarities between all of our documents
similarity = cosine_similarity(counts)

# we want to cluster these documents together
linkages = linkage(similarity, 'ward')

# use scipy's dendrogram to visualize it
dendrogram(linkages, labels=titles, orientation='right', leaf_font_size=8, leaf_rotation=45)

# clean up the plot a bit
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.title("Dendrogram of Analects Chapters")
plt.tight_layout()


ax = plt.gca()

labels = ax.get_ymajorticklabels()

for label in labels:
    label.set_color(color_dict[label.get_text()])



plt.show()