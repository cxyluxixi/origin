# first
urlIndex = pow(2, 38)


# second
def changeLetters(strSrc):
    result = ''
    for i in strSrc:
        if i.islower():
            result += chr((ord(i) - ord('a') + 2) % 26 + ord('a'))
        else:
            result += i
    return result


if __name__ == "__main__":
    a = 'http://www.pythonchallenge.com/pc/def/map.html'
    p = changeLetters(a)
    print(p)


# third
import urllib.request
import re 
s = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/equality.html').read().decode()
comments = re.findall("<!--(.*?)-->", s,re.DOTALL)
counts ={}
comment = comments[-1]
for c in comment:
    counts[c] = counts.get(c,0) +1 
n = re.findall('[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+',comment)
print(''.join(n))



# fourth
import urllib.request
import re 
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
num = '8022'
# num = '16044/2'
pattern = re.compile(r'and the next nothing is (\d+)')
while True:
    content = urllib.request.urlopen(url + num).read().decode()
    print(content)
    newNum = re.search(pattern,content)
    if newNum == None:
        print('mistake')
        break
    num = newNum.group(1)


# fifth
# peak.html  -->  <peak hell source = 'banner.p' 
# change url to banner.p
sixUrl = 'http://www.pythonchallenge.com/pc/def/banner.p'
sixContent = urllib.request.urlopen(sixUrl)
import pickle
sixData = pickle.load(sixContent)
for line in sixData:
    l = ''
    # print(line)
    for k,v in line:
        l = l +(k*v)
    print(''.join(l))


# sixth
# channel html<!--  zip  download it
import zipfile,re
f = zipfile.ZipFile("../channel.zip")
print(f.read('readme.txt'))
num = '90052'
comments = []
while True:
    content = f.read(num+'.txt').decode('utf-8')
    comments.append(f.getinfo(num+'.txt')).comment.decode('uft-8')
    print(content)
    newSix = re.search(r'Next nothing is (\d+)',content)
    if newSix == None:
        print('mistake')
        break
    num = newSix.group(1)

print(''.join(comments))



# seventh 
# it's in the air. look at the letters. --> oxygen
# http://www.pythonchallenge.com/pc/def/oxygen.png
from PIL import Image
from io import BytesIO
import requests
import re
img = Image.open(BytesIO(requests.get('http://www.pythonchallenge.com/pc/def/oxygen.png').content))
w = int(img.width)
h = int((img.height)/2)
newSeven = [img.getpixel((i,h))for i in range(w)] #获取每个坐标点的像素 
newSeven = newSeven[::7]#通过观察数组，发现间隔规律，然后用步长去重
ords1 = [r for r,g,b,a in newSeven if r==g==b]
print(ords1)
strSeven = ''.join(map(chr,ords1))
ords2 = re.findall(r"\d+",strSeven)
strSeven2 = ''.join(map(chr,map(int,ords2)))
print(strSeven2)


# eighth 
# http://www.pythonchallenge.com/pc/def/integrity.html
'''<!--
un: 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw: 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
-->
'''
import bz2
username = bz2.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')
password = bz2.decompress(b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')
print(username,password)  #huge ,file  loading and go to the new challenge


# nineth
# http://www.pythonchallenge.com/pc/return/good.html
# len(a[30]) = ?  By clicking the image:
# a = [1, 11, 21, 1211, 111221,,,,

a = '1'
b = ''
c = [] 
for i in range(0, 30):
    j = 0 #j表示每个不同值的数字，
    k = 0 # k表示每个j指向的数字的次数，统计次数
    while j < len(a):   # j遍历每项的每个数字元素
        while k < len(a) and a[k] == a[j]: k += 1 # 如果数字相等，k加1，记录该数字有几个
        b += str(k-j) + a[j]  # k-j个a[j], 使用b加等于,即可获得下一项
        j = k
    print(b)
    a = b  # b为每次循环产生的数列新项（下一项）
    b = '' # 将b还原，重新进入循环产生下一项
    c.append(a)
print(len(a))


# eleven
# http://www.pythonchallenge.com/pc/return/5808.html
# odd even  奇偶,split the image by odd/even??

from io import BytesIO
from PIL import Image
import requests
img = Image.open('将图片下载保存，这里放入绝对路径')
(w, h) = img.size

w = img.width
h = img.height

# 生成奇偶两张画布
odd = Image.new('RGB',(w,h))
even = Image.new('RGB',(w,h))

# split the image by odd/even
for i in range(w):
    for i in range(h):
        # 获取每个坐标点的像素(r,g,b,a)
        p = img.getpixel(i,j)

        # 横纵坐标和，奇数/偶数
        if(i+j)%2 == 1:
            odd.putpixel((i,j),p)
        else:
            even.putpixel((i,j),p)

even.save('even.jpg')
odd.save('odd.jpg')


# twelve
# http://www.pythonchallenge.com/pc/return/evil.html
# dealing evil
# image = evil1.jpg
# try evil2.jpg
# try evil2.gfx
# 下载保存这个文件，evil2.gfx
data = open("/Users/luxixi/Downloads/evil2.gfx",'rb').read()
for i in range(5):
    # 将数据分成五份，保存为图片
    open('%d.jpg' % i,'wb').write(data[i::5])  
    # 五张图片显示为disproportional




# thirdteen
# http://www.pythonchallenge.com/pc/return/disproportional.html
# phone the evil
# 在上一关，evil4.jpg 里e代码显示 Bert is evil,
# 在本关，电话图片中“5”可以点击，点击之后的url为http://www.pythonchallenge.com/pc/phonebook.php
# 这个url里显示了一段代码
# 搜索了一下这段代码，需要用xmlrpc来运行获取其中的信息
import xmlrpc.client 
conn = xmlrpc.client.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
conn.system.listMethods() # ['phone', 'system.listMethods', 'system.methodHelp', 'system.methodSignature', 'system.multicall', 'system.getCapabilities']
conn.system.methodHelp('phone')
conn.system.methodSignature('phone')
print(conn.phone('Bert')) #555-ITALY




# fourteen
# http://www.pythonchallenge.com/pc/return/italy.html 
# 网页代码里有注释
# <!-- remember: 100*100 = (100+99+99+98) + (...  -->
# 括号为一组，表示四个方向的坐标。从大到小，按照大图（面包螺旋的方向）（右下左上）
# 按照括号的数组长度，一圈一圈的螺旋往中间点画
# 查看下面的小图，发现图的原始大小为 10000*1=100*100
from PIL import Image 
im = Image.open('http://www.pythonchallenge.com/pc/return/wire.jpg')
out = Image.new('RGB',[100,100])

# 画图指针，四个方向箭头，每画一个点，换下一个方向，画一个点 
delta =[(1,0),(0,1),(-1,0),(0,-1)]
x,y,p = -1,0,0

d = 200
# 后面用于获得边长，s = d//2
# 获得类似（100+99+99+98)的数组，每次整除以2，
# 得到的即为（100 99 99 98），（98 97 97 96）
# 一圈四条边，每次画一条边（100，99，99，98）
while d/2>0:
    for v in delta:
        ss = d // 2
        for s in range(ss):
            x = x+v[0]
            y = y+v[1]
            z = im.getpixel(p,0)
            out.putpixel((x,y),z)
            p+=1
        d -=1
out.save('Pchallenge14.jpg')
# cat



# fifteen
# 



