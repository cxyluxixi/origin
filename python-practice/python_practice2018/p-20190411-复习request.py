import requests
import re 
from bs4 import BeautifulSoup
from lxml import etree
import random
import time

page = [1,2,3,4,5,6,7,8]
print(page)
nlist = []

def getHTML(url):
    try:
        r = requests.get(url,timeout = 15)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print('网页html文本获取成功')
        return r
    except:
        print('获取html文本失败，无法开始解析')
        return ''

def getNews():
    for i in page:
        url = 'http://www.hbsrsksy.cn/hbksy/002/002002/{}.html'.format(i)
        html = getHTML(url)
        # soup = BeautifulSoup(html.text,"html.parser")
        soup2 = etree.HTML(html.content.decode('utf-8')) #content.decode('')
        news = soup2.xpath('/html/body/div[2]/div[2]/div[2]/div[2]/ul//li/a/@title')
        # print(news)
        for new in news:
            nlist.append(new)
        time.sleep(random.randint(1,3))
    print(nlist)
    return nlist

if __name__ == "__main__":
    getNews()