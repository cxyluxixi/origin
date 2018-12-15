import re
import requests
from bs4 import BeautifulSoup
import time
import random
import json
import uuid
import redis



small = 6311932  #2018.11.28号最小值5730003
eachDic = {}
fileUrl = ''
hd = {'user-agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1'} 
# 最大值：6730462


# r = redis.StrictRedis(host="47.104.101.207", port=6379, db=21, password="Pa88####")

def main():
    urls = ['http://news.bioon.com/article/{}.html'.format(str(i)) for i in range(small, small+1)]

    for url in urls:
        # if r.exists(str(uuid.uuid3(uuid.NAMESPACE_DNS,url))) == 0:
            getShengWuGuText(url)
            time.sleep(random.randint(1, 5))
        # else:
            # print('已经爬过的',url)

# 爬取网页的html代码文本
def getShengWuGuHTML(url, code='uft-8'):
    try:
        r = requests.get(url,headers = hd)
        # r.raise_for_status()
        r.encoding = code
        return r
    except:
        print('网页代码文本爬取失败')
        pass


# 爬取单个页面的标题，日期，和正文


def getShengWuGuText(eachUrl):
    # 全部html文本
    html = getShengWuGuHTML(eachUrl)
    print(html.status_code)

    if html.status_code == 404:
        print('网页404,pass')
    elif html.status_code == 403:
        print('403，程序休息5分钟')
        time.sleep(20000)
        getShengWuGuText(eachUrl)    
    else:
        print('ok')
        soup = BeautifulSoup(html.text, 'html.parser')

        # earchUrl
        print(eachUrl)

        # 标题
        divTitleAndDate = soup.find('div', {'class': 'title5'})
        print(type(divTitleAndDate))
        title = divTitleAndDate.find('h1').text

        # 日期
        date_needToCut = divTitleAndDate.find('p').text
        date = re.findall(r"\d{4}-\d{2}-\d{2}", date_needToCut)
        dateText = date[0]  # 日期列表转化为字符串

        # 获取文件名url
        fileUrl = eachUrl[-12:-5]

        #id
        idUrl= uuid.uuid3(uuid.NAMESPACE_DNS,eachUrl)
        print(idUrl)

        # 正文
        listArticle = soup.find('div', attrs={'class': 'text3'})
        print(listArticle)
        if len(listArticle):
            pText = ''
            print("标题：", title)
            print("日期：", dateText)
            print('下面都是正文：')

            # 获取正文div的子节点
            # for i in listArticle.children:
            #     p = str(i)
            #     pp = re.sub(r'<[^>]+>',"",p)
            #     ppp = re.sub(r'\n|\r','',pp)
            #     pText = pText + ppp
            # print(pText)

            # 添加字段到字典
            eachDic['id'] = str(idUrl)
            eachDic['标题'] = title
            eachDic['日期'] = dateText
            eachDic['正文'] = pText


            # 将每个网页解析后的字典信息保存到文件里
            fileName = 'shengWuGuText-' + fileUrl + '.txt'
            path = '/Users/luxixi/Downloads/huimeiyijian/'
            print(fileName)
            with open(path + fileName,"w") as f:
                f.write(json.dumps(eachDic,ensure_ascii=False))
            # r.set(str(uuid.uuid3(uuid.NAMESPACE_DNS, eachUrl)), eachUrl)
        else:
            print('没有正文，只添加uuid，并不保存文本文件，跳过') 
            # r.set(str(uuid.uuid3(uuid.NAMESPACE_DNS, eachUrl)), eachUrl)



if __name__ == '__main__':
    main()


