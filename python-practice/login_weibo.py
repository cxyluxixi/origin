import requests
import base64
import re
import hashlib
import urllib
import json
import urllib
import urllib.request
import http.cookiejar
from urllib import parse
import base64
import re
import json
import hashlib

cj = http.cookiejar.LWPCookieJar()
cookie_support = urllib.request.HTTPCookieProcessor(cj)
opener = urllib.request.build_opener(cookie_support, urllib.request.HTTPHandler)
urllib.request.install_opener(opener)
postdata = {
    'entry': 'weibo',
    'gateway': '1',
    'from': '',
    'savestate': '7',
    'userticket': '1',
    'ssosimplelogin': '1',
    'vsnf': '1',
    'vsnval': '',
    'su': '',
    'service': 'miniblog',
    'servertime': '',
    'nonce': '',
    'pwencode': 'wsse',
    'sp': '',
    'encoding': 'UTF-8',
    'url': 'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
    'returntype': 'META'
}

headers = '''
POST /sso/login.php?client=ssologin.js(v1.4.19) HTTP/1.1
Host: login.sina.com.cn
Connection: keep-alive
Content-Length: 624
Cache-Control: max-age=0
Origin: https://weibo.com
Upgrade-Insecure-Requests: 1
Content-Type:application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Referer: https://weibo.com/
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9

'''
def str2obj(s,s1='\n',s2=': '):
   li = s.split(s1)
   res = {}
   for kv in li:
      li2 = kv.split(s2)
      if len(li2) > 1:
         res[li2[0]] = li2[1]
   return res


def get_servertime():
   urltime = 'https://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=MTM4NzExMzQyMDk%3D&rsakt=mod&checkpin=1&client=ssologin.js(v1.4.19)&_=1547170677962'
   # 返回出来的是一个Response对象，无法直接获取，text后，可以通过正则匹配到
   # 大概长这样子的：sinaSSOController.preloginCallBack({"retcode":0,"servertime":1545606770, ...})
   data = requests.request('GET', urltime).text
   p = re.compile('((.*))')
   try:
       json_data = p.search(data).group(1)
       data = json.loads(json_data)
       servertime = str(data['servertime'])
       nonce = data['nonce']
       return servertime, nonce
   except:
       print('获取 severtime 失败!')
       return None


def get_pwd(pwd, servertime, nonce):
   # 第一次计算，注意Python3 的加密需要encode，使用bytes
   pwd1 = hashlib.sha1(pwd.encode()).hexdigest()
   # 使用pwd1的结果在计算第二次
   pwd2 = hashlib.sha1(pwd1.encode()).hexdigest()
   # 使用第二次的结果再加上之前计算好的servertime和nonce值，hash一次
   pwd3_ = pwd2 + servertime + nonce
   pwd3 = hashlib.sha1(pwd3_.encode()).hexdigest()
   return pwd3


def get_user(username):
   # 将@符号转换成url中能够识别的字符
   _username = urllib.request.quote(username)
   # Python3中的base64计算也是要字节
   # base64出来后，最后有一个换行符，所以用了切片去了最后一个字符
   username = base64.encodebytes(_username.encode())[:-1]
   return username

username = input('username')
pwd=input('password')
stime,nonce = get_servertime()
pword = get_pwd(pwd,stime,nonce)


headers = str2obj(headers)
postdata['servertime'] = stime
postdata['nonce']=nonce
postdata['sp']= pword
postdata['su']= str(get_user(username))


url = 'https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.19)'
loginData = requests.post(url,params=postdata,headers=headers)
ret = loginData.text
p = re.compile(r'location\.replace\(\"(.*?)\"\)')
try:
   login_url = p.search(ret).group(1)
   r = requests.request('GET',login_url)
   r.raise_for_status()
   print("success")
except:
   print('failure')