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

def get_servertime():
    url = 'https://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=MTM4NzExMzQyMDk%3D&rsakt=mod&checkpin=1&client=ssologin.js(v1.4.19)&_=1547170677962'
    data = urllib.request.urlopen(url).read()
    p = re.compile(r'\((.*)\)')
    try:
        json_data = p.search(data).group(1)
        data = json.loads(json_data)
        servertime = str(data['servertime'])
        nonce = data['nonce']
        return servertime, nonce
    except:
        print ('Get severtime error!')
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


def login():
    username = '你的登录邮箱'
    pwd = '你的密码'
    url = 'http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.3.18)'
    try:
        servertime, nonce = get_servertime()
    except:
        return ''
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
    postdata['servertime'] = servertime
    postdata['nonce'] = nonce
    postdata['su'] = get_user(username)
    postdata['sp'] = get_pwd(pwd, servertime, nonce)
    postdata = parse.urlencode(postdata)
    headers = {'User-Agent':'Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0'}
    req  = urllib.request.Request(
        url = url,
        data = postdata,
        headers = headers
    )
    result = urllib.request.urlopen(req)
    text = result.read()
    p = re.compile(r'location\.replace\(\'(.*?)\'\)')
    try:
        login_url = p.search(text).group(1)
        #print login_url
        urllib.request.urlopen(login_url)
        print ("登录成功!")
    except:
        print ('Login error!')

login()