import requests as r 
from bs4 import BeautifulSoup
kv = {"user-agent":"Chrome/44.0"}
demo = r.get("http://www.baidu.com/",hearder=kv)

soup = BeautifulSoup(demo,"html.parser")
soup.a.name
soup.a.attrs
soup.a.attrs[""]
soup.a.parent.name
soup.a.next_sibling
soup.a.string
type(soup.a.string)
soup.a.contents #a节点的所有子节点的全部内容以列表方式返回
soup.body.children #for child in soup.body.children
soup.body.descentants #全部的后代
soup.a.parents
soup.a.parent
soup.a.next_siblings
soup.a.next_sibling
soup.a.previous_siblings
soup.a.previous_sibling

for link in soup.find_all('a'): 
    # 用find_all找到全部a标签，然后
    print(link.get('href'))

soup.find_all(["a","b"]) #找出两个及以上的参数，要用列表形式

# import re
# for tag in soup.find_all(re.compile('b'))
# find_all(tagname,attr,recursive,string,**kwargs)
# soup.find_all('p',id='link1','course') # 'course'为string参数，表示包含course字符串的p
# recursive 表示是否怼子孙全部检索，默认为True
# 简写soup()==soup.find_all(),tag()=tag.fing_all()

