import requests
import re
from bs4 import BeautifulSoup
from lxml import etree


# <div id="test2">你好，<font color=red>你的微信是多少？</font><div>

# 如果使用：
# data = selector.xpath('//div[@id="test2"]/text()').extract()[0]  
# 只能提取到“你好，”；
# 如果使用：
# data = selector.xpath('//div[@id="test2"]/font/text()').extract()[0]  
# 又只能提取到“你的微信是多少？”
# 到底我们要怎样才能把“你好，你的微信是多少”提取出来？
# 可以使用xpath的string(.)来达到目的
#     data = selector.xpath('//div[@id="test2"])
#     info = data.xpath('string(.)').extract()[0]



def getHTML(url):
    try:
        r = requests.get(url,timeout = 15)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print('获取html文本成功，返回对象r，开始解析')
        return r
    except:
        print('获取html文本失败，无法开始解析')
        return ''

def eachPage(ulist,url):
    html = getHTML(url)
    soup1 = BeautifulSoup(html.text,'html.parser')
    soup2 = etree.HTML(html.content.decode('utf-8'))
    keyWord = soup1.find('h1',attrs={'class':'keyword'}).text.strip()
    soundsDiv = soup1.find('div',attrs={'class':'base-speak'})
    sounds = ''

    # 去掉div中间的所有标签<>
    for i in soundsDiv.children:
        p = str(i)
        pp = re.sub(r'<[^>]+>',"",p)
        ppp = re.sub(r'\n|\r','',pp)
        sounds = sounds +' '+ ppp


    # meaningsUl = soup1.find('ul',{'class':'base-list'})
    # 单词意思的文本，全部找出来，形成一个列表meanings
    meanings = soup2.xpath('//li[@class="clearfix"]//span/text()')
    print(type(meanings))
    meaning = ''
    for j in meanings:
        m = re.match('[a-zA-Z.,]+',j) 
        #对每一项进行判断是否含有字母（表示词性），如果有，则换行没有则合并
        if m:
            meaning = meaning + '\n'+ j
        else:
            meaning = meaning + j

    print(keyWord)
    print(sounds)
    print(meaning)

def main(url,w):
    if w == 'q':
        exit    # 输入'q'退出查询
    else:
        eachPage(ulist,url)
    

if __name__ == "__main__":
    w = input('请输入需要查询的单词： (退出程序请按q）')
    url = 'http://www.iciba.com/'+ w
    ulist = {}
    main(url,w)