import requests
from multiprocessing import Process, Lock
from time import *
import random


class Run(Process):
    def __init__(self, c):
        super().__init__()
        self.c = c

    def run(self, lock=Lock()):
        # with lock:
        # 输出到不同到文件，不需要加锁了
        for b in range(10):
            a = 'http://api.fund.eastmoney.com/FundGuZhi/' \
                'GetFundGZList?type=1&sort=3&orderType=desc&canbuy' \
                '=0&pageSize=200&pageIndex='
            page = str(b + 10 * self.c)
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
            f = open(str(self.c) + '.txt', 'w', encoding='utf-8')
            f.write(response.content.decode('utf-8'))
            f.close()
            sleep(0.05)
            # sleep(random.randint(1, 3))
            # js = response.json()
            # for i in js['Data']:
            #     print(i)
            #     for m in js['Data'][str(i)]:
            #         print(m)
            print(page)

        # 输出是无序的


def main():
    begin_sleep = time()
    p1 = Run(0)
    p2 = Run(1)
    p3 = Run(2)
    p4 = Run(4)
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    second_sleep = time()
    run_time = second_sleep - begin_sleep
    print('主线程')
    print('时间', run_time)


if __name__ == '__main__':
    main()

# 多进程搞定，但是没有考虑抛出异常，以及进程同步锁（可以用写入不同文件来解决）。手动设置进程可以改成设置一次进程数量。没有用fakeUA以及写入csv
# https://blog.csdn.net/qq_37851620/article/details/103835106
# https://www.jb51.net/article/156762.htm
# https://www.cnblogs.com/jiangfan95/p/11439207.html 没有用if __name__ == "__main__":，代码是报错的
# https://docs.python.org/zh-cn/3/library/multiprocessing.html
# https://www.cnblogs.com/zhoudayang/p/5474053.html
