import urllib
import urllib.parse
import urllib.request
import os


# flask ，下载文件
url = 'http://127.0.0.1:5000/download'


try:
    r = urllib.request.urlopen(url)
    # 这里read获取的是二进制的
    r = r.read()
    # 二进制解码为汉字，urf-8
    filename = r.decode()
    # filename = urllib.parse.quote('图片.jpg')
    print('start download:'+filename)
    data = urllib.request.urlopen(url+'?filename=' +urllib.parse.quote(filename))
    data = data.read()
    # print(data)
    fileobj = open('download'+filename,'wb')
    fileobj.write(data)
    fileobj.close()
    print('finish')

except Exception as err:
    print(err)