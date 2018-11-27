#encoding-utf-8
import requests
from bs4 import BeautifulSoup
import re
import jieba
import wordcloud 
from scipy.misc import imread


# 创建保存爬取数据的数组Movie
Movie =  [['name','movie categories','year','nation'],]

# 爬取目标网站的单独一个网页
def getHTMLText(url,code='urf-8'):
       
    try:      
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        return ''

# 解析爬取每个网页的html信息，并保存到数组Movie里
def getMovieList(MovieUrl):
    html = getHTMLText(MovieUrl,'utf-8')
    soup = BeautifulSoup(html,'html.parser')
    MovieList = soup.find('ul',attrs={"class":'movie-list'})
    MovieLinkList = MovieList.find_all('h2')
    
    for i in range(len(MovieLinkList)):
                val = MovieLinkList[i].text
                # print(val)
                val = val.replace('】','【')
                val = val.split('【')
                if len(val) != 9:
                    pass
                else:
                    movieName = val[0]
                    movieAttr = val[5]
                    movieYear = val[3]  
                    movieNation = val[7]
                    Movie.append([movieName,movieAttr,movieYear,movieNation])
            

    return Movie


# 将保存好的数组Movie变成字符串，写入文件保存
def writeFile(content):
    f = open('movielist.txt','r+')
    for i in range(len(content)):
        for m in range(len(content[i])):
            f.write(str(content[i][m]))
        f.write('\n')
    
    f.close()

#主程序，设置爬取总网页数，调用函数爬取 
def main(page_num):
    urls = ['http://www.dysfz.vip/{}?o=2'.format(str(i))for i in range(1,page_num+1)]
    for url in urls :
        getMovieList(url)
        writeFile(Movie)
    makeMovieWordCloud('movielist.txt','q.jpg')
    # for item in Movie:
    #     print(item)
    

#mask 用来设置生成词云的形状，默认长方形
def makeMovieWordCloud(fileName,imageName):
    mask = imread(str(imageName))
    file1 = open(str(fileName), "r", encoding="utf-8")
    t = file1.read()
    file1.close()
    ls = jieba.lcut(t)
    txt = " ".join(ls)
    w = wordcloud.WordCloud(\
        width=100,height=100,\
        font_path='/Users/luxixi/luxixi2018/githubpractice/simhei/SimHei.ttf',mask=mask)
    w.generate(txt)
    w.to_file('movieWordCloud.jpg')

main(5)