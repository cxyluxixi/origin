import requests
import bs4 
from bs4 import BeautifulSoup
import xlwt 


def getHTML(url,codeStyle):
    try:
        r = requests.get(url,timeout= 300)
        r.raise_for_status()
        r.encoding = codeStyle
        return r.text 
    except:
        return ''

def getTableHead(hlist,html):
    soup = BeautifulSoup(html,'html.parser')
    th = soup.find('table').find('tr').children
    for t in th:
        if isinstance(t,bs4.element.Tag):
            hlist.append(t.text[:10])
    return hlist


def eachPageText(ulist,html):
    soup = BeautifulSoup(html,'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            td = tr('td')
            ulist.append([td[0].string,td[1].string,td[2].string,td[3].string,td[4].string])
    return ulist


def writeFile(hlist,ulist,fileName):
    workbook = xlwt.Workbook(encoding='utf-8')
    sheet = workbook.add_sheet(fileName,cell_overwrite_ok=True)
    for i in range(len(hlist)):
        sheet.write(0,i,hlist[i])
        for j in range(len(ulist)):
            for m in range(len(ulist[j])):
                sheet.write(j+1,m,ulist[j][m])
    workbook.save('/Users/luxixi/Downloads/'+fileName+'.xls')


if __name__ == "__main__":
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2018.html'
    codeStyle = 'utf-8'
    ulist = []
    hlist = []
    html = getHTML(url,codeStyle)
    hlist = getTableHead(hlist,html)
    print(hlist)
    ulist = eachPageText(ulist,html)
    writeFile(hlist,ulist,'universityList')
