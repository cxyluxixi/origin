import urllib.parse
import urllib.request
import requests


# flask，上传文件
url = 'http://127.0.0.1:5000/upload'
filename = '图片.jpg'
try:
    fobj = open('/Users/luxixi/luxixi2018/startgit/'+filename,'rb')
    data = fobj.read()
    fobj.close()
    print(data)

    headers = {'content-type': 'application/octet-stream'}
    url = url+'?filename='+urllib.parse.quote(filename)
    r = urllib.request.Request(url,data,headers)
    msg = urllib.request.urlopen(r)
    msg = msg.read().decode()
    # r = requests.post(url,headers=headers,data=data)
    # msg = r.content
    print(msg)
except Exception as err:
    print(err)