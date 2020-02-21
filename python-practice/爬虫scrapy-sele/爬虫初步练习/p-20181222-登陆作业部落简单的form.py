# import requests 
# import numpy as np 
# import xlwt 

# # url后面的参数列表，后面get url时传参使用
# indexList = np.arange(0,251,25)
# url = ''


# def getHTML(url, code='uft-8'):
#     for index in indexList: 
#         urlIndexDict = {'start':index}
#         try:
#             r = requests.get('https://book.douban.com/top250',params=urlIndexDict)
#             r.raise_for_status()
#             r.encoding = code
#             return r
#         except:
#             print('网页代码文本爬取失败')
#             pass

# d ={'start':'25'}
# r = requests.get('https://book.douban.com/top250',params=d)
# print(r.cookies) 
# #<RequestsCookieJar[<Cookie bid=gHfL_2a_mWo for .douban.com/>]>
# # print(r.headers)
# headers = {'User-Agent':'Chrome/10'}
# rr = requests.get('https://book.douban.com/top250',headers = headers)
# print (rr.request.headers['User-Agent'])



# # params 也是加到url后面的参数，一般当参数是键值对时使用
# params={"mobile":'TestingenvironmentVIPB.mobile_online',"psw":'TestingenvironmentVIPB.password_real'}
# rrr = requests.get('https://book.douban.com/top250',params = params,headers= headers)
# print(rrr.url)



# # 如果需要在请求中添加cookie，可以实例化一个RequestCookieJar的类，
# # 然后把值set进去，最后在get,post方法里面指定cookies参数就行了，
# import requests
# from requests.cookies import RequestsCookieJar
 
 
# url = "http://fanyi.baidu.com/v2transapi"
 
# cookie_jar = RequestsCookieJar()
# cookie_jar.set("BAIDUID", "B1CCDD4B4BC886BF99364C72C8AE1C01:FG=1", domain="baidu.com")
 
# res = requests.get(url, cookies=cookie_jar)
# print(res.status_code)

import requests 
import re 
from bs4 import BeautifulSoup



url = 'https://www.zybuluo.com/login'
header ={
    'Cookie': 'JSESSIONID=51D2DD917E6553DE2BFA2C7735A97C19; UM_distinctid=16763134ecb239-08da4d516a871-1e396652-13c680-16763134ecc52a',
    'User_agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

s= requests.session()
response = s.get(url)
header = response.headers

datas = {
    'login': 'MMMMMM',
    'password': 'MMMM',
    'human':'',
    'form.submit': ''
}
mm = s.post('https://www.zybuluo.com/login', data=datas)
print(mm.status_code)
r = re.findall('username',mm.text)
print(r[0])


