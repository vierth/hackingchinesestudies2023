import re, os

with open('analects.txt','r', encoding='utf8') as rf:
    text = rf.read()

text = re.sub(r"\n", '', text)
text = re.sub(r"\s+", " ", text)
chapters = re.split(r'CHAP\. [IVXCL]+\.', text)
chapters = [c.strip() for c in chapters]

if not os.path.isdir('analects'):
    os.mkdir('analects')

for i, chapter in enumerate(chapters):
    with open(os.path.join('analects', f"{i}.txt"), 'w', encoding='utf8') as wf:
        wf.write(chapter)
