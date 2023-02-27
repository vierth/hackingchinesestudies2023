import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

with open('analects.txt','r', encoding='utf8') as rf:
    text = rf.read()

text = text[text.find("CONFUCIAN ANALECTS."):text.find("End of Project Gutenberg Etext")]

doc = nlp(text[:1000])

# style = "dep" dependency tree
# style='ent' named entities
displacy.serve(doc, style="ent", port=8080)
