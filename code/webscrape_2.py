from bs4 import BeautifulSoup

with open('wiki_george.html', 'r', encoding='utf8') as rf:
    html = rf.read()
    soup = BeautifulSoup(html, "html.parser")


links = soup.find_all('a')

for link in links:
    link_text = link.string
    link_url = link.get("href")
    print(f"{link_text}: {link_url}")