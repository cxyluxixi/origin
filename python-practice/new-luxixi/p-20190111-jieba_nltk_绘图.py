# --coding uft-8--
import jieba 
import json
import matplotlib
import os

text = '''
给大家分享一个关于爬虫与反爬虫的故事，可能有部分人已经看过了，看过的话就直接跳过吧，嘿嘿。
Day 1

小莫想要某站上所有的电影，写了标准的爬虫(基于HttpClient库)，不断地遍历某站的电影列表页面，根据 Html 分析电影名字存进自己的数据库。
这个站点的运维小黎发现某个时间段请求量陡增，分析日志发现都是 IP(http://xxx.xxx.xxx.xxx)这个用户，并且 user-agent 还是 Python-urllib/3.6 ，基于这两点判断非人类后直接在服务器上封杀。

Day 2

小莫电影只爬了一半，于是也针对性的变换了下策略：1. user-agent 模仿百度("Baiduspider...")，2. IP每爬半个小时就换一个IP代理。
小黎也发现了对应的变化，于是在服务器上设置了一个频率限制，每分钟超过120次请求的再屏蔽IP。 同时考虑到百度家的爬虫有可能会被误伤，想想市场部门每月几十万的投放，于是写了个脚本，通过 hostname 检查下这个 ip 是不是真的百度家的，对这些 ip 设置一个白名单。

Day 3

小莫发现了新的限制后，想着我也不急着要这些数据，留给服务器慢慢爬吧，于是修改了代码，随机1-3秒爬一次，爬10次休息10秒，每天只在8-12，18-20点爬，隔几天还休息一下。
小黎看着新的日志头都大了，再设定规则不小心会误伤真实用户，于是准备换了一个思路，当3个小时的总请求超过50次的时候弹出一个验证码弹框，没有准确正确输入的话就把 IP 记录进黑名单

Day 4

小莫看到验证码有些傻脸了，不过也不是没有办法，先去学习了图像识别（关键词 PIL，tesseract），再对验证码进行了二值化，分词，模式训练之后，总之最后识别了小黎的验证码（关于验证码，验证码的识别，验证码的反识别也是一个恢弘壮丽的斗争史...），之后爬虫又跑了起来。
小黎是个不折不挠的好同学，看到验证码被攻破后，和开发同学商量了变化下开发模式，数据并不再直接渲染，而是由前端同学异步获取，并且通过 JavaScript 的加密库生成动态的 token，同时加密库再进行混淆（比较重要的步骤的确有网站这样做，参见淘宝和微博的登陆流程）。

Day 5

混淆过的加密库就没有办法了么？当然不是，可以慢慢调试，找到加密原理，不过小莫不准备用这么耗时耗力的方法，他放弃了基于 HttpClient的爬虫，选择了内置浏览器引擎的爬虫(关键词：PhantomJS，Selenium)，在浏览器引擎运行页面，直接获取了正确的结果，又一次拿到了对方的数据。
小黎：.....

这就是爬虫、反爬虫以及反反爬虫之间的一部斗争史，在之前的文章中，我们以及了解了降低访问频率、改变请求头、Ajax分析、代理ip的使用以及验证码识别等反反爬虫措施，用以应对网站针对爬虫的各种反爬措施。那么在面对加密算法的时候，在不具备分析加密能力的情况下，我们可以选择使用Selenium+PhantomJS的方法直接使用浏览器运行网页，获取相应信息。

首先简单介绍一下Selenium这个Web的自动化测试工具，它可以根据我们的指令，让浏览器自动加载页面，获取需要的数据，甚至页面截屏，或者判断网站上某些动作是否发生。但Selenium 自己不带浏览器，不支持浏览器的功能，它需要与第三方浏览器结合在一起才能使用。但是我们有时候需要让它内嵌在代码中运行，所以我们可以用一个叫 PhantomJS 的工具代替真实的浏览器。

PhantomJS这里也简单介绍一下，PhantomJS 是一个基于Webkit的“无界面”(headless)浏览器，它会把网站加载到内存并执行页面上的 JavaScript，因为不会展示图形界面，所以运行起来比完整的浏览器要高效 PhantomJS 是一个功能完善(虽然无界面)的浏览器，可以通过Selenium调用PhantomJS来直接使用。。需要注意的是PhantomJS 只能从它的官方网站http://phantomjs.org/download.html) 下载。

如果我们把 Selenium 和 PhantomJS 结合在一起，就可以运行一个非常强大的网络爬虫了，这个爬虫可以处理 JavaScrip、Cookie、headers，以及任何我们真实用户需要做的事情。不过使用最新的Selenium过程中发现，PhantomJS目前已经不维护了，所以新版的Selenium在使用时会给出警示：
UserWarning: Selenium support for PhantomJS has been deprecated, please use headless versions of Chrome or Firefox instead 
warnings.warn('Selenium support for PhantomJS has been deprecated, please use headless 
这里推荐我们使用谷歌或者火狐的浏览器，所以我们在后面将以谷歌浏览器结合Selenium来示例。
最后就是一个我们使用浏览器经常会使用的一个动作了，拖动滚动条。具体操作见下面这个示例。
'''



# 分词 
textlist = jieba.lcut(text)

# 定制图片造型
import numpy as np
from PIL import Image
# 图片根据颜色，转化为颜色点阵多维数组，
# 后续词云会根据这个矩阵数组的不同颜色覆盖，
pic = np.array(Image.open('view.jpeg'))

# 使用图片造型的颜色来表示单词
from wordcloud import ImageColorGenerator
# ImageColorGenerator 里面传入一个多维数组，表示对应的颜色
# 然后后面词云中，设置color_func= genclr
genclr=ImageColorGenerator(pic)


# 将词汇列表转化为空格分隔的字符串
wordstr = ' '.join(textlist[:100])
from wordcloud import WordCloud
fontpath = '/Users/luxixi/luxixi2018/githubpractice/simhei/chinese.simhei.ttf'

# 定义要生成的图片的参数
wcloud = WordCloud(font_path=fontpath, 
                    background_color='black',
                    max_font_size=500,
                    min_font_size=20,
                    max_words=50,
                    random_state=42,
                    mask=pic,
                    color_func=genclr,
                    collocations=False,
                    width=1000,height=800,margin=10,)
# 将词汇字符串传到图片中，生成词云图
wcloud.generate(wordstr)
wcloud.to_file("grwordcloud.png") 

#cell-3
import jieba.analyse

# jieba.analyse.extract_tags(text, 这里的text是个str
# for word, weight in jieba.analyse.extract_tags(text, topK=10, withWeight=True):
#     print('%s %s' % (word, weight))



# 使用nitk，统计词频
text1 = 'asdfnhojcbjb;oaiusyfigqegvdhfaosjhbxkhbhuwrolihdkjbf'
from nltk.probability import FreqDist

fdist = FreqDist(wordstr)
tops = fdist.most_common(10)
print(tops)
# 打印发现很多标点符号，和“的”，“了”，等等无实际意义的字

# 去除冗余单字
dellist = []
for key in fdist:
    if len(key)<2:
        dellist.append(key)
for key in dellist:
    del fdist[key]
tops = fdist.most_common(10)
print(tops)



# 将词频字典作图
import plotly
import plotly.graph_objs as go

plotly.offline.init_notebook_mode(connected=False)

keywords=[item[0] for item in tops]
weights=[item[1] for item in tops]
# 如果词频列表中，有近似或同义词，那么合并它们，并删除单个
def mergeItem(wd1,wd2):
    newkey = wd1 +'+'+ wd2 
    n1 = keywords.index(wd1)
    keywords[n1]=newkey
    n2 = keywords.index(wd2)
    weights[n1]= weights[n1]+weights[n2] 
    del weights[n2]
    del keywords[n2]
    return newkey
# 合并两个数组 
comb = zip(keywords,weights)
def comp(item):
    return item[1]
# 排序
# sorted 中key要用生成式，每次传入comb的item
comb = sorted(comb,reversed=True,key=comp)
# 生成新数组
keywords=[v for v,_ in comb]
weights=[v for _,v in comb]
# 生成统计图
plotly.offline.iplot({
    "data": [go.Scatter(x=keywords, y=weights)], # scatter是画折线图
    "layout": go.Layout(title="拉勾网人工智能职业关键词分布")
})
