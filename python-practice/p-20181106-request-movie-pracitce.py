#encoding-utf-8
import requests
from bs4 import BeautifulSoup
import re


Movie =  [['name','movie categories','year','nation'],]
def getHTMLText(url,code='urf-8'):
       
    try:      
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        return ''


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

def writeFile(content):
    f = open('movielist.txt','w+')
    f.seek(0)
    for i in range(len(content)):
        strMovie = ''
        for m in range(len(content[i])):
            strMovie.join(content[i][m])  
            f.write(strMovie+'\n')
    
    f.close()
def main(page_num):
    urls = ['http://www.dysfz.vip/{}?o=2'.format(str(i))for i in range(1,page_num+1)]
    for url in urls :
        getMovieList(url)
        writeFile(Movie)
    for item in Movie:
        print(item)

    


main(5)