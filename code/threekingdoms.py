import spacy
import itertools

with open('novels/sanguo.txt', 'r', encoding='utf8') as rf:
    three_kingdoms = rf.read()

nlp = spacy.load('zh_core_web_sm')

doc = nlp(three_kingdoms)

cooccurence = []
weights = []
for i,sent in enumerate(doc.sents):
    # print(i, len(doc.sents))
    temp_people = []
    
    for ent in sent.ents:
        if ent.label_ == "PERSON" and ent.text not in temp_people:
            temp_people.append(ent.text)
        # print(ent, ent.label_)
    if len(temp_people) > 1:
        cooccurence.append(temp_people)
        weights.append(10)
    
edges = ["Source\tTarget\tType"]

for weight,cooccure in zip(weights, cooccurence):
    # comse from https://codereview.stackexchange.com/questions/256952/python-get-all-unique-pair-combinations-from-list-of-elements
    pairs = list(itertools.combinations(cooccure, 2))

    for pair in pairs:
        edges.append("\t".join([pair[0], pair[1], "Undirected", str(weight)]))
print(edges)
with open("three_kingdoms_net.tsv", "w", encoding='utf8') as wf:
    wf.write("\n".join(edges))
