import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/88.0.4324.182 Mobile Safari/537.36 '
}
cookies = {'ASP.NET_SessionId': '5o21lf55ohhulveflzr0zdav'}
url = 'http://8.135.30.80:8888/admin/user/users.aspx?page=6&action=edit&params=364558'
response = requests.get(url, cookies=cookies)
f = open("1.html", 'w', encoding='UTF-8')
f.write(response.content.decode('UTF-8'))
f.close()
# print(response.content.decode('utf-8)'))
js = response.json()
for i in js:
    print(i)

