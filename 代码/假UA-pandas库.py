import requests
import pandas as pd
import time
import random
import fake_useragent

ua = fake_useragent.UserAgent()
cookies = {'JSESSIONID': '854DB37C43E3FD0DDDE2CFEDDFF81E50'}
for i in range(64860):
    headers = {'User-Agent': ua.random}
    url = 'http://sy.youmobeng.cn/BullPoker/adm/listAgentScoreRecord?currentPage=' + str(i) + '&ownerId=&costType=&startDate=&endDate='
    response = requests.get(url, headers=headers, cookies=cookies)
    f = open(str(i) + ".html", 'w', encoding='UTF-8')
    f.write(response.content.decode('UTF-8'))
    f.close()
    data = pd.DataFrame()
    data = data.append(pd.read_html(str(i) + ".html", encoding='UTF-8'), ignore_index=True)
    print(data)
    data.to_csv('1.csv', encoding='utf_8_sig', mode='a', index=0, header=0)
    time.sleep(1)
