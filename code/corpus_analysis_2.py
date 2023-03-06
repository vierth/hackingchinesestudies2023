import re, os

with open('analects.txt','r', encoding='utf8') as rf:
    text = rf.read()

text = re.sub(r"\n", '', text)
text = re.sub(r"\s+", " ", text)
chapters = re.split(r'(CHAP\. [IVXCL]+\.)', text)
chapters = [c.strip() for c in chapters]

chapters = chapters[1:]

if not os.path.isdir('analects'):
    os.mkdir('analects')

['Title of Chpat', "text of chpater", "title chapter 2", 'text chapter 2']

for i in range(0, len(chapters), 2):
    title = chapters[i].replace(".", "")
    with open(os.path.join('analects', f"{title}.txt"), 'w', encoding='utf8') as wf:
        wf.write(chapters[i+1])
