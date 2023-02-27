import os

titles = []
texts = []

for root, dirs, files in os.walk("corpus"):
    for fname in files:
        if fname[0] != ".":
            
            with open(os.path.join(root, fname), 'r', encoding='utf8') as rf:
                text = rf.read()
                titles.append(fname[:-4])
                texts.append(text)

print(titles)