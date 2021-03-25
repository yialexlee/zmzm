import requests
import pandas as pd

# url = 'http://sy.youmobeng.cn/BullPoker/adm/listUser?currentPage=1&nickName=&userType=&pid=&agentId='
urls = [
    'http://sy.youmobeng.cn/BullPoker/adm/listUser?currentPage={}&nickName=&userType=&pid=&agentId='.format(number)
    for number in range(0, 100)
]
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/87.0.4280.141 Safari/537.36 '
}
cookies = {'JSESSIONID': 'C252C3A8C89A11E6BD415C1E0A033E22'}
for url in urls:
    response = requests.get(url, cookies=cookies)
    f = open('1.html', 'w', encoding='UTF-8')
    f.write(response.content.decode('UTF-8'))
    f.close()
    data = pd.DataFrame()
    data = data.append(pd.read_html('1.html', encoding='UTF-8'), ignore_index=True)
    print(data)
    data.to_csv('1.csv', encoding='utf_8_sig', mode='a', index=0, header=0)

# tocsv格式必须要utf_8_sig,mode='a'就是不覆盖原来的数据，index和header是行列的索引
# 每次写文件都要注意编码，否则会乱码
# 没有多线程，没有session，保持登录，循环不够优化，不需要urls也是可以实现的，
