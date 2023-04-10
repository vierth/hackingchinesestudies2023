import spacy

with open('sanguo.txt','r',encoding='utf8') as rf:
    text = rf.read().replace("\n", "")[:10000]

nlp = spacy.load("zh_core_web_trf")
doc = nlp(text)

for sent in doc.sents:
    for ent in sent.ents:
        print(ent, ent.label_)
    