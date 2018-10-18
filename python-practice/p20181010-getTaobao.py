import requests
import re
def getHtmlText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text 
    except:
        return ""

def parsePage(ls,html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html) #获得商品价格
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html) #获得商品名称
        for i in range(len(plt)):
            price = eval(plt[i].split(":")[1])
            title = eval(tlt[i].split(":")[1])
            ls.append([title,price])
            # 这里不能使用ls = ls.append(......)
            # 因为这里append返回NoteType,无法再次赋值
            # 所以直接使用ls.append就可以了
            
    except:
        print("")


def printGoodsList(ls):
    print("\t{:6}\t{:10}\t{:4}".format("序号","商品名称","价格"))
    count = 0
    for g in ls:
        count = count + 1
        print("\t{:4}\t{:10}\t{:4}".format(count,g[0],g[1]))

def main():
    goods = "女士西装套装"
    depth = 2
    start_url = "https://s.taobao.com/search?q="+ goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + "%s=" +str(44*i)
            html = getHtmlText(url)
            parsePage(infoList,html)
        except:
            continue
    printGoodsList(infoList)

main()