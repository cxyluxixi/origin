import requests 
from http.cookiejar import LWPCookieJar
import re 
import json
import base64
from PIL import Image
from bs4 import BeautifulSoup



url = 'http://yjs.ccnu.edu.cn/yjs/'
header ={
    'Cookie': 'JSESSIONID=51D2DD917E6553DE2BFA2C7735A97C19; UM_distinctid=16763134ecb239-08da4d516a871-1e396652-13c680-16763134ecc52a',
    'User_agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}


s = requests.session()

img = s.get('http://yjs.ccnu.edu.cn/yjs/security/initDigitPicture.do?',headers= header)
show_captcha = img.content
with open('captcha.jpg', 'wb') as f:
    f.write(show_captcha)
im = Image.open('captcha.jpg')
im.show()
captcha = input('输入验证码:')
im.close()
datas = {
    'j_username': 'XXX',
    'j_password': 'XXX',
    'j_digitPicture': captcha
}
mm = s.post('http://yjs.ccnu.edu.cn/yjs/login.do', data=datas)
print(mm.status_code)
print(mm.text)

