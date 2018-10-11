import requests as r
import os
path = "/Users/luxixi/luxixi2018/"
url = "http://img3.a0bi.com/upload/ttq/20150217/1424148773551.jpg"
savePath = path + url.split("/")[-1]
try:
    if not os.path.exists(path):
        os.mkdir(path)
    if not os.path.exists(savePath):
        a = r.get(url)
        a.raise_for_status()
        with open(savePath,"wb") as pic:
            pic.write(a.content)
            pic.close
            print("爬取成功，并已保存图片")
    else:
        print("保存失败")
except:
    print('爬取失败')