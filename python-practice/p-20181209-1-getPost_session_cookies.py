import requests 
import numpy as np 
import xlwt 

# url后面的参数列表，后面get url时传参使用
indexList = np.arange(0,251,25)
url = ''


def getHTML(url, code='uft-8'):
    for index in indexList: 
        urlIndexDict = {'start':index}
        try:
            r = requests.get('https://book.douban.com/top250',params=urlIndexDict)
            r.raise_for_status()
            r.encoding = code
            return r
        except:
            print('网页代码文本爬取失败')
            pass

d ={'start':'25'}
r = requests.get('https://book.douban.com/top250',params=d)
print(r.cookies) 
#<RequestsCookieJar[<Cookie bid=gHfL_2a_mWo for .douban.com/>]>
# print(r.headers)
headers = {'User-Agent':'Chrome/10'}
rr = requests.get('https://book.douban.com/top250',headers = headers)
print (rr.request.headers['User-Agent'])

# params 也是加到url后面的参数，一般当参数是键值对时使用
params={"mobile":'TestingenvironmentVIPB.mobile_online',"psw":'TestingenvironmentVIPB.password_real'}
rrr = requests.get('https://book.douban.com/top250',params = params,headers= headers)
print(rrr.url)



# 如果需要在请求中添加cookie，可以实例化一个RequestCookieJar的类，
# 然后把值set进去，最后在get,post方法里面指定cookies参数就行了，
import requests
from requests.cookies import RequestsCookieJar
 
 
url = "http://fanyi.baidu.com/v2transapi"
 
cookie_jar = RequestsCookieJar(policy=)
cookie_jar.set("BAIDUID", "B1CCDD4B4BC886BF99364C72C8AE1C01:FG=1", domain="baidu.com")
 
res = requests.get(url, cookies=cookie_jar)
print(res.status_code)


