import requests
from bs4 import BeautifulSoup
import time 
import random



def getLinkRank2(url):
    start=1
    for start in range(2):  
        html=requests.get(url+str(start),headers=headers)
        start+=1  
        soup = BeautifulSoup(html.text, 'html.parser')
        
        # 找到职位搜索页面中每个职位
        for item in soup.find_all('div','job-primary'):
            shuchu=[]
            shuchu.append(item.find('div','job-title').text)#职位名     
            
            #读取每个职位的详细信息页面
            xinzi=item.find('span','red').string
            xinzi=xinzi.replace('k','')
            xinzi=xinzi.split('-')
            shuchu.append(xinzi[0]) #薪资范围最低
            shuchu.append(xinzi[1]) #薪资范围最高
            
            yaoqiu=item.find('p').contents
            shuchu.append(yaoqiu[0].string  if len(yaoqiu)>0 else 'None') #地点
            shuchu.append(yaoqiu[2].string  if len(yaoqiu)>2 else 'None') #经验
            shuchu.append(yaoqiu[4].string  if len(yaoqiu)>4 else 'None') #学历
            
            gongsi=item.find('div','info-company').find('p').contents
            shuchu.append(gongsi[0].string  if len(gongsi)>0 else 'None') #公司行业
            shuchu.append(gongsi[2].string  if len(gongsi)>2 else 'None') #融资阶段
            shuchu.append(gongsi[4].string  if len(gongsi)>4 else 'None') #公司人数
            
            shuchu.append(item.find('div','info-publis').find('p').string.replace('发布于','')) #发布日期
            shuchu.append(item.find('div','info-publis').find('h3').contents[3].string) #发布人
            
            print('\t'.join(shuchu))

            # 获取每个职位链接中的详情
            link=item.find('div','info-primary').find('h3').find('a')['href']
            xq=getDetails(link)
            shuchu.append(xq)      
            print('\t'.join(shuchu))
            time.sleep(random.randint(1,3))
            

def getDetails(link):
    xq_html=requests.get('https://www.zhipin.com'+link,headers=headers)
    xq_soup= BeautifulSoup(xq_html.text, 'html.parser')
    miaoshu=xq_soup.find('div','job-sec').find('div','text').text #获得标记的内部文字
    miaoshu=miaoshu.lstrip().rstrip() #去除开头和结尾的空格
    return miaoshu


if __name__ == "__main__":
    url='https://www.zhipin.com/c101020100/h_101020100/?query=%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD&page='
    headers={
    'user-agent':'Mozilla/5.0'
    }
    hud=['职位名','薪资1','薪资2','地点','经验','学历','公司行业','融资阶段','公司人数','发布日期','发布人']
    print('\t'.join(hud))
    getLinkRank2(url)
    

