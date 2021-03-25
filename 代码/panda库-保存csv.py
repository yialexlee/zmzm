import requests
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/87.0.4280.141 Safari/537.36 '
}
cookies = {'JSESSIONID': 'C252C3A8C89A11E6BD415C1E0A033E22'}
for i in range(10):
    url = 'http://sy.youmobeng.cn/BullPoker/adm/listUser?currentPage=' + str(i) + '&nickName=&userType=&pid=&agentId='
    response = requests.get(url, cookies=cookies)
    f = open(str(i) + ".html", 'w', encoding='UTF-8')
    f.write(response.content.decode('UTF-8'))
    f.close()
    data = pd.DataFrame()
    data = data.append(pd.read_html(str(i) + ".html", encoding='UTF-8'), ignore_index=True)
    print(data)
    data.to_csv('1.csv', encoding='utf_8_sig', mode='a', index=0, header=0)

# 多了可以保存html格式
