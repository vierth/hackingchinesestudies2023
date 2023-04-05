import os, nltk, re
import hanziconv

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import PCA
import numpy as np

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
        chunks = chunk(text)
        print(len(chunks))
        texts.extend(chunks)
        chunk_titles = [f[:-4] for i in range(len(chunks))]
        print(len(chunk_titles))
        titles.extend(chunk_titles)

vectorizer = TfidfVectorizer(use_idf=False, max_features=100, analyzer="char")
counts = vectorizer.fit_transform(texts)
# We need to make this a dense array
countMatrix = counts.toarray()


# Lets perform PCA on the countMatrix:
pca = PCA(n_components=2)
myPCA = pca.fit_transform(countMatrix)


# title to int we need to transform labels to integers:
title_to_int = {d:i for i,d in enumerate(color_dict.keys())}


# To plot this we will need some information (note I do this step by step. This
# is not necessary with only two classes, but handy when you have many more:
# First, let's get the unique items. Here we are coloring the data by year
unique_titles = list(color_dict.keys())

# We want these classes to be integers starting at zero
title_class = [i for i in range(len(unique_titles))]


# Let's make a new representation for each document that is just these integers
# and it needs to be a numpy array
# text_class
text_class = np.array([title_to_int[t] for t in titles])


# Make a list of the colors
colors = [color_dict[title] for title in unique_titles]

for col, class_num, title in zip(colors, title_class, unique_titles):
    plt.scatter(myPCA[text_class==class_num,0],myPCA[text_class==class_num,1],label=title,c=col)

# Let's add a legend! matplotlib will make this for us based on the data we 
# gave the scatter function.
plt.legend()
plt.show()