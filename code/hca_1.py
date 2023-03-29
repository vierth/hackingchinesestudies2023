import os, nltk

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances
from scipy.cluster.hierarchy import linkage, dendrogram

import matplotlib.pyplot as plt

ignore_files = set(["LICENSE.txt", ".DS_Store",".git_ignore"])

titles = []
texts = []
for root, dirs, files in os.walk('analects'):
    files = [f for f in files if f not in ignore_files]
    for f in files:
        with open(os.path.join(root, f),'r', encoding='utf8') as rf:
            text = rf.read()

        texts.append(text)
        titles.append(f[:-4])

vectorizer = TfidfVectorizer(use_idf=False, max_features=100)
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
plt.show()