import requests
from bs4 import BeautifulSoup


def get(chapter):
    chapter1 = str(chapter)
    r = requests.get('https://www.trxs.cc/tongren/5033/{}.html'.format(chapter1))
    content = r.text.encode(r.encoding).decode(r.apparent_encoding,errors='ignore')
    soup = BeautifulSoup(content)
    text = soup.find('div', {'class': 'read_chapterDetail'})
    text = text.find_all('p')
    str1 = ""
    for i in text:
        # j=i.text()
        if len(i.contents) != 0:
            str1 = str1 + i.contents[0]
        else:
            str1 = str1 + "\n"
    return str1

get(15)
f = open('shendetiaosepan.txt', 'a',encoding='utf-8')
for i in range(1, 429):
    print(i)
    str1 = get(i)
    f.write(str1)
f.close()
