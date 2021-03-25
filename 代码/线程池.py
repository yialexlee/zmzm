from threading import Thread, Lock
from time import *
from concurrent.futures import ProcessPoolExecutor

import requests


def test(c):
    # with lock:
    # 输出到不同到文件，不需要加锁了
    for b in range(1, 11):
        a = 'http://api.fund.eastmoney.com/FundGuZhi/' \
            'GetFundGZList?type=1&sort=3&orderType=desc&canbuy' \
            '=0&pageSize=200&pageIndex='
        page = str(b + 10 * c)
        url = a + page
        headers = {
            'Cookie': 'cowCookie=true; qgqp_b_id=db30f6383e9f0342f28f32752062a289; '
                      'st_si=93495102570451; st_asi=delete; intellpositionL=1524px; '
                      'intellpositionT=3037px; EMFUND1=null; EMFUND2=null; EMFUND3=null;'
                      ' EMFUND4=null; EMFUND5=null; EMFUND6=null; EMFUND7=null; EMFUND8=null;'
                      ' EMFUND0=null; EMFUND9=03-09 21:34:24@#$%u534E%u590F%u5927%u76D8%u7CBE%u900'
                      '9%u6DF7%u5408@%23%24000011; st_pvi=96303569725597; st_sp=2021-03-09%2021%3A'
                      '32%3A36; st_inirUrl=http%3A%2F%2Fdata.eastmoney.com%2F; st_sn=17; st'
                      '_psi=2021030922493891-112200304021-1442118872',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          '  Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.45',
            'Referer': 'http://fund.eastmoney.com/'}
        response = requests.get(url, headers=headers)
        # print(response.content.decode('utf-8'))
        f = open(str(c) + '.txt', 'w', encoding='utf-8')
        f.write(response.content.decode('utf-8'))
        f.close()
        sleep(0.005)
        # sleep(random.randint(1, 3))
        # js = response.json()
        # for i in js['Data']:
        #     print(i)
        #     for m in js['Data'][str(i)]:
        #         print(m)
        print(page)


if __name__ == "__main__":
    processPool = ProcessPoolExecutor(10)
    begin_sleep = time()
    future = processPool.submit(test, 0)
    future2 = processPool.submit(test, 1)
    future3 = processPool.submit(test, 2)
    future4 = processPool.submit(test, 3)
    #  threadPool后面是方法和参数
    processPool.shutdown(wait=True)
    second_sleep = time()
    run_time = second_sleep - begin_sleep
    print('时间', run_time)

# reference :https://www.cnblogs.com/xiaozi/p/6182990.html
# https://www.cnblogs.com/hoojjack/p/10846010.html
