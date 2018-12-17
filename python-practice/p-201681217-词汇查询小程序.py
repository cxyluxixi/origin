import requests
import re
from bs4 import BeautifulSoup
from lxml import etree


def getHTML(url):
    try:
        r = requests.get(url,timeout = 15)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print('获取html文本成功，返回对象r，开始解析')
        return r.text
    except:
        print('获取html文本失败，无法开始解析')
        return ''

def eachPage(url):
    html = getHTML(url)
    soup1 = BeautifulSoup(html,'html.parser')
    keyWord = soup1.find('h1',attrs={'class':'keyword'}).text.strip()
    soup2 = etree.HTML(html.text,'html.parser')

def main(url):
    eachPage(url)

if __name__ == "__main__":
    w = input('请输入需要查询的单词：')
    url = 'http://www.iciba.com/'+ w
    main(url)