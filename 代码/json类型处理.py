import requests
import pandas as pd
import json
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/88.0.4324.182 Mobile Safari/537.36 '
}
cookies = {'ASP.NET_SessionId': '5o21lf55ohhulveflzr0zdav'}
# url = 'http://8.135.30.80:8888/admin/user/users.aspx?page=6&action=edit&params=364558'
for id in range(10000):
    url = 'http://8.135.30.80:8888/admin/user/UserEdit.aspx?action=usergamedata&userId=' + str(
        id + 364500) + '&agentId=3'
    response = requests.get(url, cookies=cookies)
    f = open(str(id + 364500) + ".html", 'w', encoding='UTF-8')
    f.write(response.content.decode('UTF-8'))
    f.close()
    print(response.content.decode('utf-8)'))
    dic = response.text
    print(dic)
    js = response.json()
    if js['code'] == -1:
        print('没有记录')
    else:
        for i in js['data']:
            print(i)
        with open('1.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['用户ID', '游戏ID', '胜局', '输局', '平局', '输赢', '波动算法', '目标金币值', '概率'])
            for i in js['data']:
                #       writer.writerows(i['id'] + "" + i['cell']['bond_nm'] + "" + i['cell']['stock_id'])
                writer.writerow(
                    [str(id + 364500), i['GameID'], i['VictoryCount'], i['DefeatCount'], i['DrewCount'], i['WinOrLoss'],
                     i['AlgoTargetGold'], i['AlgoRate'], i['GameName']])

# dict = {1: 1, 2: 'aa', 'D': 'ee', 'Ty': 45}
# for value in dic.values():
#   print(value)
# 字典里面套字典
# data = pd.DataFrame()
# data = data.append(pd.read_html("1.html", encoding='UTF-8'), ignore_index=True)
# print(data)
# data.to_csv('1.csv', encoding='utf_8_sig', mode='a', index=0, header=0)

# http://8.135.30.80:8888/admin/user/UserEdit.aspx?action=usergamedata&userId=364558&agentId=3
