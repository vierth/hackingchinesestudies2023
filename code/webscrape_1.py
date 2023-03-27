# if you are going access the internet inside of loop be good citizen and slow it down
# import time
# time.sleep(1)

import urllib.request

url = "https://en.wikipedia.org/wiki/Grigorios_Konstantas"

with urllib.request.urlopen(url) as request:
    contents = request.read()

# turn bytes into a string
html_string = contents.decode()

with open('wiki_george.html', 'w', encoding='utf8') as wf:
    wf.write(html_string)

