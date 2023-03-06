import re
import csv

with open('sikuquanshu.txt', 'r', encoding='utf8') as rf:
    text = rf.read()

'''
{{Novel|[[../]]|卷三•經部三|卷002|卷004|卷}}
'''
page_regex = re.compile(r'Novel\|.+?•(.部)')

'''
==《[[周易義海撮要]]》•十二卷{{*|兩淮馬裕家藏本}}==
'''

book_regex = re.compile(r'==《(.+?)》•([一二三四五六七八九十百]+)卷')

subcat_regex = re.compile(r'==(.+?)類[一二三四五六七八九十百]+')
# results = re.split(r'Novel\|.+?•(.部)', text)
results = page_regex.split(text)

results = results[1:]

outputdata = []
rawoutput = []
for i in range(0, len(results), 2):
    category = results[i]
    content = results[i+1]
    subcat = subcat_regex.search(content)
    if subcat:
        subcat = subcat.group(1)
    else:
        subcat = ""
    books = book_regex.finditer(content)
    for book in books:
        book_title = book.group(1).replace("[", "").replace("]", "")
        book_length = book.group(2)
        temp_data = [category, subcat, book_title, book_length]
        rawoutput.append(temp_data)
        book_data_string = "\t".join(temp_data)
        print(book_data_string)
        outputdata.append(book_data_string)

with open('book_data.tsv', 'w', encoding='utf8') as wf:
    wf.write("\n".join(outputdata))

with open('book_data.csv', 'w',  encoding='utf8') as wf:
    writer = csv.writer(wf, delimiter=",")
    for row in rawoutput:
        writer.writerow(row)