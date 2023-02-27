import spacy

with open('corpus/shuihu.txt', 'r', encoding='utf8') as rf:
    text = rf.read()

nlp = spacy.load("zh_core_web_trf")
doc = nlp(text)

for word in doc:
    print(word.text, word.pos_)