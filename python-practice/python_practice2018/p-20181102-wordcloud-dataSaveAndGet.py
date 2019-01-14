def a(lst):
	def b():
		def c(x,y):
			return x+y
		return map(c,lst)
	return b

# m = a([2,4,5])
# print m()
# 13
mm = a([2,4,5])
print (mm)

f = open("dataFileName.txt","w")
ls = [[],[],[]]
for item in ls:
	f.write(",".join(item)+ '/n')

f.close()

#GovRptWordCloudv1.py
import jieba
import wordcloud
f = open("新时代中国特色社会主义.txt", "r", encoding="utf-8")
 
t = f.read()
f.close()
ls = jieba.lcut(t) #分词，并形成列表
txt = " ".join(ls) #将汉语的分词用空格分开，并转化为字符串
w = wordcloud.WordCloud( \
    width = 1000, height = 700,\
    background_color = "white",
    font_path = "msyh.ttc"  #font_path为字体文件来源  
    )
w.generate(txt) #生产词云
w.to_file("grwordcloud.png") #输出保存为图片，并命名文件名称



#不规则图形词云
#GovRptWordCloudv2.py
import jieba
import wordcloud
from scipy.misc import imread
mask = imread("chinamap.jpg") #mask 用来设置词云形状，默认长方形
excludes = { }
f = open("新时代中国特色社会主义.txt", "r", encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(\
    width = 1000, height = 700,\
    background_color = "white",
    font_path = "msyh.ttc", mask = mask
    ) #还有很多参数，min_font_size, max_fond_size, fon_step字号逐渐减小的步长 
      #max_words最大呈现单词数, stop_words不显示的单词, mask调用见上面一条注释

w.generate(txt)
w.to_file("grwordcloudm.png")



