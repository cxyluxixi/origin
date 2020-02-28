# gitpractice

### scrapy 如何开始新的项目，相关cmd命令
--1. scrapy 教程 https://www.xncoding.com/tags/scrapy/ 
   1.1创建project  
        scrapy startproject spidername
   1.2cd切换目录到爬虫目录，编写items.py，
        设置数据表中需要有哪些指标，如：name=spider.Field()
--2.生成爬虫文件
        scrapy genspider spidername url domain 
        开始编写spider文件，parse()写解析式，提取items.py中需求的数据，也就是那些spider.Field()需要的那些items，相当于requests中bs4的find，find_all表达式
--3. 写中间件，爬虫伪装，设置代理ip，my_proxy 服务器等
     3.1写pipielines.py,一般是关于数据储存，判断清洗等爬下来之后的处理。
     3.2 设置settings.py， 一般是关于连接服务器和爬虫伪装的一些设置：开启管道,  user_agent,  headers,DOWNLOADER_MIDDLEWARES等
     DOWNLOADER_MIDDLEWARES = {
        'book.middlewares.BookDownloaderMiddleware': 543,
        'book.middlewares.my_proxy':数字越小，优先级越高,
     }
--4. 运行scrapy
        scrapy crawl spidername
        是bookspider，那么就是 scrapy crawl bookspiders

--5. 暂停爬虫进程
        “scrapy crawl 爬虫名称 -s JOBDIR=保存进程的文件夹目录”
        比如 “scrapy crawl jobbole -s JOBDIR=job_info/001”
--6. 再次重启爬虫进程，下次需要重启的时候，上一步相同的命令
         “scrapy crawl jobbole -s JOBDIR=job_info/001”

## 目前主要是scrapy 和 selenium的练习内容

-- 1.book文件夹是scrapy简单实现爬取储存json数据文件,已移动到scrapy_demo文件中

-- 2.(selenium）zhihu_验证码  
        目前无法实现，点击图片对应位置的验证码，英文字符验证码无法清除“属性预留汉字”后输入  

-- 3.(selenium) zhilian(已实现）
        元素input send_keys和验证码输入

-- 4.flask_demo文件夹是关于flask框架的使用

-- 5.image_krystal是scrapy_demo中krystal 爬虫运行存图片的文件夹
