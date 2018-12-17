import requests
import re 
from bs4 import BeautifulSoup

# 为什么单独运行，可以打印出xsrf，但是放入p-20181216-爬虫知乎登陆.py 报错
# 错误为KeyError  没有key xsrf


# 利用session保持链接
session = requests.session()

agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
header = {
    # "HOST": "www.zhihu.com",
    # "Referer": "https://www.zhihu.com",
    "User-Agent": agent,
    'Connection': 'keep-alive'
}

response = session.get("https://www.zhihu.com/signup", headers=header)
m_dict =  response.cookies.get_dict()
print(m_dict['_xsrf'])
mm_dict =  requests.utils.dict_from_cookiejar(response.cookies)
print(mm_dict['_xsrf'])
