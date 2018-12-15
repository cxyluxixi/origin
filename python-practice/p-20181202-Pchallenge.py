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
pattern = re.compile('and the next nothing is (\d+)')
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
    newSix = re.search('Next nothing is (\d+)',content)
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
ords2 = re.findall("\d+",strSeven)
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
