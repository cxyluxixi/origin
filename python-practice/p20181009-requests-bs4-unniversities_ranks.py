# myself
import requests
from bs4 import BeautifulSoup
import bs4
def getUrlText(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def fillUnivList(univList, html):
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find("tbody").children:
        if isinstance(tr, bs4.element.Tag):
            tdList = tr('td')
            univList.append([tdList[0].string,tdList[1].string,tdList[2].string])

    pass

def printUnivList(univList,num):
    for i in range(num):
        univ = univList[i]
        print("{:<10}\t{:<10}\t{:<10}".format(univ[0],univ[1],univ[2]))
        # chr(12288)为utf-8limian的中文空格，一般用来填充，使得表格居中对齐
        # 例如"{0:<10}\t{1:{3}<10}\t{2:<10}".format(univ[0],univ[1],univ[2],chr(12288))

    print("Rank" + str(num))

def main():
    univInfo = []
    url = "http://www.zuihaodaxue.com/dingjianrencaipaiming2018.html"
    html = getUrlText(url)
    fillUnivList(univInfo,html)
    printUnivList(univInfo,50)

main()

# #CrawUnivRankingA.py
# import requests
# from bs4 import BeautifulSoup
# import bs4
 
# def getHTMLText(url):
#     try:
#         r = requests.get(url, timeout=30)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         return r.text
#     except:
#         return ""
 
# def fillUnivList(ulist, html):
#     soup = BeautifulSoup(html, "html.parser")
#     for tr in soup.find('tbody').children:
#         if isinstance(tr, bs4.element.Tag):
#             tds = tr('td')
#             ulist.append([tds[0].string, tds[1].string, tds[3].string])
 
# def printUnivList(ulist, num):
#     print("{:^10}\t{:^6}\t{:^10}".format("排名","学校名称","总分"))
#     for i in range(num):
#         u=ulist[i]
#         print("{:^10}\t{:^6}\t{:^10}".format(u[0],u[1],u[2]))
     
# def main():
#     uinfo = []
#     url = 'https://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
#     html = getHTMLText(url)
#     fillUnivList(uinfo, html)
#     printUnivList(uinfo, 20) # 20 univs
# main()


# # rawUnivRankingB.py
# import requests
# from bs4 import BeautifulSoup
# import bs4
 
# def getHTMLText(url):
#     try:
#         r = requests.get(url, timeout=30)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         return r.text
#     except:
#         return ""
 
# def fillUnivList(ulist, html):
#     soup = BeautifulSoup(html, "html.parser")
#     for tr in soup.find('tbody').children:
#         if isinstance(tr, bs4.element.Tag):
#             tds = tr('td')
#             ulist.append([tds[0].string, tds[1].string, tds[3].string])
 
# def printUnivList(ulist, num):
#     tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
#     print(tplt.format("排名","学校名称","总分",chr(12288)))
#     for i in range(num):
#         u=ulist[i]
#         print(tplt.format(u[0],u[1],u[2],chr(12288)))
     
# def main():
#     uinfo = []
#     url = 'https://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
#     html = getHTMLText(url)
#     fillUnivList(uinfo, html)
#     printUnivList(uinfo, 20) # 20 univs
# main()