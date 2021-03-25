import requests
from bs4 import BeautifulSoup
import re
import csv
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/88.0.4324.182 Mobile Safari/537.36 '
}
cookies = {'ASP.NET_SessionId': '5o21lf55ohhulveflzr0zdav'}
for i in range(64663):
    url = 'http://8.135.30.80:8888/admin/user/users.aspx?action=edit&params=' + str(i + 300000)
    r = requests.get(url, cookies=cookies)
    f = open(str(i + 300000) + ".html", 'w', encoding='UTF-8')
    f.write(r.content.decode('UTF-8'))
    f.close()
    demo = r.text  # 服务器返回响应
    soup = BeautifulSoup(demo, "html.parser")
    a = soup.select('#tbPhone')
    b = a[0]
    text = str(b)
    res = re.sub(r'\D', "", text)
    print(res)
    with open('1.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['ID', 'Phone'])
        writer.writerow([str(i + 300000), res])
