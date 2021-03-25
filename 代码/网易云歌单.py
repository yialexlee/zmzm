import requests
import fake_useragent
from bs4 import BeautifulSoup
import csv

ua = fake_useragent.UserAgent()
for y in range(38):
    url = 'https://music.163.com/discover/playlist/?order=hot&cat=全部&limit=35&offset=' + str(35 * y)
    headers = {'User-Agent': ua.random}
    response = requests.get(url, headers=headers)
#    print(response.content.decode('UTF-8'))
    f = open(str(y) + '.html', 'w', encoding='UTF-8')
    f.write(response.content.decode('UTF-8'))
    f.close()
    res = response.text
    soup = BeautifulSoup(res, 'html.parser')
    item = soup.select('.msk')

    m = len(item)
    for n in range(m):
        b = item[n]
        text = str(b)
        print(text)
        with open('1.txt', 'a', encoding='UTF-8') as f:
            f.write(text)
            f.write('\n')
        with open('2.csv', 'a', encoding='utf-8-sig', newline="") as t:
            head = ['歌单名']
            writer = csv.writer(t, head)
            writer.writerow([text])
