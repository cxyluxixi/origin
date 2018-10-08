import requests as r
import time

def getUrlText(url):
    try:
        address = r.get(url)
        address.raise_for_status()
        address.encoding = address.apparent_encoding
        return address.text[:100]
    except:
        print('爬取该网页信息出错')


if __name__=="__main__":
    url= input("请输入需要爬的网址，形如http://....../")
    start_time = time.perf_counter()
    for i in range(100):
        getUrlText(url)
        t = time.perf_counter()
        print('第{}次爬取，耗时{:.5}s'.format(i,t-start_time))
    end_time = time.perf_counter()
    print('100次爬取网页最终耗时{:.5}s'.format(end_time-start_time))
