# There are a number of models you can download
'''
To download a model you run this from the terminal/command prompt

python -m spacy en_core_web_sm
python -m spacy zh_core_web_sm

sm small model
md medium model
lg large model
trf transform model

'''

import spacy

nlp = spacy.load("en_core_web_sm")

with open('analects.txt','r', encoding='utf8') as rf:
    text = rf.read()

text = text[text.find("CONFUCIAN ANALECTS."):text.find("End of Project Gutenberg Etext")]

doc = nlp(text[:1000])

doc.ents # named entities
doc.sents # sentences in teh document
doc.noun_chunks # noun chunk

for word in doc:
    print(word.text, word.pos_, word.dep_, word.lemma_)

print(spacy.explain("advmod"))