# -*- coding:utf-8 -*-
import requests
import re
import xlwt
from bs4 import BeautifulSoup
from datetime import datetime
import codecs
import os


now = datetime.now()             #开始计时
print(now)

# 创建文件目录
image_dir = "/Users/luxixi/Downloads/douban/image/"
if not os.path.exists(image_dir):
    os.makedirs('/Users/luxixi/Downloads/douban/image/')

txtfile = codecs.open("/Users/luxixi/Downloads/douban/top250.txt",'w','utf-8')
url = "http://book.douban.com/top250?"

header = { "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.13 Safari/537.36",
           "Referer": "http://book.douban.com/"
           }
    
#下载图片
def download_img(imageurl,imageName = "xxx.jpg"):
    rsp = requests.get(imageurl, stream=True)
    image = rsp.content
    path = image_dir + imageName +'.jpg'
    #print(path)
    with open(path,'wb') as file:
        file.write(image)

#建立Excel
workbook = xlwt.Workbook(encoding='utf-8')
sheet = workbook.add_sheet('book_top250',cell_overwrite_ok=True)

item = ['书名','别称','评分','评价人数','封面','图书链接','出版信息','标签']
for i in range(1,9):
    sheet.write(0,i,item[i-1])
        
s = requests.Session()      #建立会话
s.get(url,headers=header)

for i in range(0,250,25):  
    geturl = url + "/start=" + str(i)                     #要获取的页面地址
    print("Now to get " + geturl)
    postData = {"start":i}                                #post数据
    res = s.post(url,data = postData,headers = header)    #post
    
    #BeautifulSoup解析
    soup = BeautifulSoup(res.content.decode(),"html.parser")       
    table = soup.findAll('table',{"width":"100%"})        #找到所有图书信息的table
    sz = len(table)                                       #sz = 25,每页列出25篇文章
    for j in range(1,sz+1):                               #j = 1~25
        sp = BeautifulSoup(str(table[j-1]),"html.parser") #解析每本图书的信息
        #print(sp.div)
        imageurl = sp.img['src']                          #找图片链接
        bookurl = sp.a['href']                            #找图书链接
        bookName = sp.div.a['title']
        nickname = sp.div.span                            #找别名
        if(nickname):                                     #如果有别名则存储别名否则存’无‘
            nickname = nickname.string.strip() 
        else:
            nickname = "None"
        
        #print(type(imageurl),imageurl)
        #print(type(bookurl),bookurl)
        #print(type(bookName),bookName)
        #print(type(nickname),nickname)
        
        notion = str(sp.find('p',{"class":"pl"}).string)   #抓取出版信息,注意里面的.string还不是真的str类型
        #print(type(notion),notion)
        rating = str(sp.find('span',{"class":"rating_nums"}).string)    #抓取平分数据
        nums = sp.find('span',{"class":"pl"}).string                    #抓取评分人数
        nums = nums.replace('(','').replace(')','').replace('\n','').strip()
        nums = re.findall(r'(\d+)人评价',nums)[0]
        #print(type(rating),rating)
        #print(type(nums),nums)
        download_img(imageurl,bookName)                     #下载图片
        book = requests.get(bookurl)                        #打开该图书的网页
        sp3 = BeautifulSoup(book.content,"html.parser")     #解析
        taglist = sp3.find_all('a',{"class":"  tag"})       #找标签信息
        tag = ""
        lis = []
        for tagurl in taglist:
            sp4 = BeautifulSoup(str(tagurl),"html.parser")  #解析每个标签
            lis.append(str(sp4.a.string))
        
        tag = ','.join(lis)        #加逗号
        if tag == "":              #如果标签为空，置"无"
            tag = "None"
        
        # 写入Excel文件
        writelist=[i+j,bookName,nickname,float(rating),int(nums),imageurl,bookurl,notion,tag]
        for k in range(0,9):
            if(k == 5):
                continue
            sheet.write(i+j,k,writelist[k])
            txtfile.write(str(writelist[k]))
            txtfile.write('\t')
        txtfile.write(u'\r\n')
        
    workbook.save("/Users/luxixi/Downloads/douban/booktop250.xls")

end = datetime.now()    #结束计时
print(end)
print("程序耗时： " + str(end-now))
txtfile.close()