import requests
import urllib.parse
import urllib.request

url = 'http://127.0.0.1:5000'
try:
    id = urllib.parse.quote('鲁西西')
    password = urllib.parse.quote('贾俊俊')
    data = 'id='+id +'&password='+password
    # encode,转化为二进制，使用post传递数据，
    data = data.encode()
    # get, 直接拼接数据
    new_url = url+'?'+data
    # post，通过data= ，传递数据
    r = urllib.request.urlopen(url, data = data)
    # get，直接拼接url
    # r = urllib.request.urlopen(new_url)
    r = r.read()
    r = r.decode()
    # r.encoding = 'utf-8'
    print(r)
except Exception as err:
    print(err)