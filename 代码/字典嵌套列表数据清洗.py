import json
import requests
import csv
import os

os.makedirs('./image/', exist_ok=True)
# h = 0

with open("1.txt", "r", encoding="utf8") as f:
    data = f.readline()
    text = data.split('{"resultCode":1,"dataCollection":null,"message":"执行成功","success":true}')
    print(text[1])

with open('1.csv', 'w', encoding='utf-8-sig', newline="")as ff:
    lens = len(text)
    csv_writer = csv.writer(ff)
    csv_writer.writerow(["UserId", "NickName", "PORTRAIT", "ID_CARD_PERSON", "ID_CARD_EMBLEM"])
    for i in range(lens):
        u = text[i]
        try:
            m = json.loads(u)
            print()
            print(m['dataCollection']['userId'])
            # 输出userid
            print(m['dataCollection']['identities'][0])
            print(m['dataCollection']['identities'][0]['url'])
            print(m['dataCollection']['identities'][2]['url'])
            print(m['dataCollection']['identities'][3]['url'])
            csv_writer.writerow([m['dataCollection']['userId'], m['dataCollection']['nickname'],
                                 m['dataCollection']['identities'][0]['url'],
                                 m['dataCollection']['identities'][2]['url'],
                                 m['dataCollection']['identities'][3]['url']])
            userid = m['dataCollection']['userId']
            print(type(userid))
            print(userid)
            url1 = m['dataCollection']['identities'][0]['url']
            url2 = m['dataCollection']['identities'][2]['url']
            url3 = m['dataCollection']['identities'][3]['url']
            r1 = requests.get(url1)
            with open('./image/' + str(userid) + '_1.png', 'wb') as f:
                f.write(r1.content)
            r2 = requests.get(url2)
            with open('./image/' + str(userid) + '_2.png', 'wb') as f:
                f.write(r2.content)
            r3 = requests.get(url3)
            with open('./image/' + str(userid) + '_3.png', 'wb') as f:
                f.write(r3.content)
        except:
            with open('66.txt', 'a', encoding='utf8', newline="")as mm:
                mm.write(u)
        pass
