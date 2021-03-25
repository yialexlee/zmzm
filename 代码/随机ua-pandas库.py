import requests
import pandas as pd
import time
import random

user_agent_list = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/61.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
    ]
headers = {random.choice(user_agent_list)}
cookies = {'JSESSIONID': 'C252C3A8C89A11E6BD415C1E0A033E22'}
for i in range(8970):
    url = 'http://sy.youmobeng.cn/BullPoker/adm/listUser?currentPage=' + str(i) + '&nickName=&userType=&pid=&agentId='
    response = requests.get(url, cookies=cookies)
    f = open(str(i) + ".html", 'w', encoding='UTF-8')
    f.write(response.content.decode('UTF-8'))
    f.close()
    data = pd.DataFrame()
    data = data.append(pd.read_html(str(i) + ".html", encoding='UTF-8'), ignore_index=True)
    print(data)
    data.to_csv('1.csv', encoding='utf_8_sig', mode='a', index=0, header=0)
    time.sleep(0.5)
