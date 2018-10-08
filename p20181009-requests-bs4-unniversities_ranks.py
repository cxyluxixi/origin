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
    for tr in soup.find_all("tbody").children:
        if isinstance(tr, bs4.element.Tag):
            tdList = tr('td')
            univList = univList.append([tdList[0].string,tdList[1].string,tdList[2].string])

    pass

def printUnivList(univList,num):
    for i in range(num):
        univ = univList[i]
        print("{:<10}\t{:<6}\t{:<10}\t".format(univ[0],univ[1],univ[2]))

    print("Rank" + str(num))

def main():
    univInfo = []
    url = ""
    html = getUrlText(url)
    fillUnivList(univInfo,html)
    printUnivList(univInfo,50)

main()