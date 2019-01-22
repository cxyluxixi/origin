# -*- coding: utf-8 -*-
import scrapy
from book.items import BookItem



# scrapy 教程 https://www.xncoding.com/tags/scrapy/ 
# 创建project  scrapy startproject spidername
# cd切换目录到爬虫目录，编写items.py， 设置数据表中需要有哪些指标，如：name=spider.Field()
# scrapy genspider spidername url domain 
# 开始编写spider文件，parse()写解析式，提取上一步需要的那些items，相当于requests中bs4的find，find_all表达式
# 写中间件，爬虫伪装，设置代理ip，my_proxy 服务器等
# 写pipielines.py,一般是关于数据储存，判断清洗等爬下来之后的处理。
# 设置settings.py， 一般是关于连接服务器和爬虫伪装的一些设置：开启管道,  user_agent,  headers,
#DOWNLOADER_MIDDLEWARES = {
#    'book.middlewares.BookDownloaderMiddleware': 543,
#    'book.middlewares.my_proxy':数字越小，优先级越高,
#}

class BookspiderSpider(scrapy.Spider):
    name = 'bookspider'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):

        # 提取数据
        # 书的信息在<article class="product_pod">中
        books = response.css('article.product_pod')
        item = BookItem()
        for book in books:
            # 书籍名称
            # name = book.css('h3 a::text').extract_first()
            name = book.xpath('./h3/a/@title').extract_first()
            
            # 书籍价格
            #price = book.css('p.price_color::text').extract_first()
            price = book.xpath('./div[@class="product_price"]/p/text()').extract_first()

            # 书籍图片地址
            imgUrl = book.xpath('./div[@class="image_container"]/a/img/@src').extract_first()
            item['name'] = name,
            item['price'] = price
            item['imgUrl'] = 'http://books.toscrape.com/'+ imgUrl
            yield item
        


        # 提取下一页链接
        next_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        # next_url = response.css('ul.pager li.next a::attr(href)').extract_first()
        if next_url:
            # 构造下一页链接
            next_url = response.urljoin(next_url)
            # 构造新的Request对象
            yield scrapy.Request(next_url, callback=self.parse)



# Scrapy内置的request子类，FormRequest这个专门为form表单设计，模拟表单提交的示例
class LoginSpider(scrapy.Spider):
    name = 'example.com'
    start_urls = ['http://www.example.com/users/login.php']

    def parse(self, response):
        return scrapy.FormRequest.from_response(response,
            formdata={'username': 'john', 'password': 'secret'},
            callback=self.after_login
        )
# return [FormRequest(url="http://www.example.com/post/action",
# formdata={'name': 'John Doe', 'age': '27'}, 
#          callback=self.after_post)]

    def after_login(self, response):
        # check login succeed before going on
        if "authentication failed" in response.body:
            self.logger.error("Login failed")
            return 

        # continue scraping with authenticated session...
        
# reponse子类       
'''TextResponse 在基本Response类基础之上增加了编码功能，专门用于二进制数据比如图片、声音或其他媒体文件
HtmlResponse 此类是TextResponse的子类，通过查询HTML的meta http-equiv属性实现了编码自动发现
XmlResponse 此类是TextResponse的子类，通过查询XML声明实现编码自动发现
'''

class xxxspider(scrapy.Spider):
    name = 'example.com'
    start_urls = ['http://www.example.com/users/login.php']

    # 给回调函数传递额外的参数
    # 如果想在上一个函数的return 返回对象中给下一个函数中传入参数
    # 可以指定Request.meta,只接受字典类型数据，
    # 将想要传输的数据，赋值给 request.meta['xxx'] = 'value' 
    # 在接受的函数中，再把值传给变量，'value' = response.meta['xxx']
    def parse_page1(self,response):
        '''
        需要知道的是item是一个字典
        '''
        item = BookItem()
        request = scrapy.Request("http://www.example.com/some_page.html",
                             callback=self.parse_page2)
        request.meta['item'] = item
        return request
        '''比如我们要爬取淘宝上的商品，我们在第一层爬取时候获得了标题(title)和价格(price)，
        但是还想获得商品的图片，就是那些点进去的大图片，假设点进去的链接是上述代码的url，
        利用scrpy.Request请求url后生成一个Request对象，通过meta参数，把item这个字典赋值给meta字典的'item'键，
        即meta={'item':item}，这个meta参数会被放在Request对象里一起发送给parse2()函数。'''
    def parse_page2(self,response):
        item = response.meta['item']
        for product in response.css('......').extract():
            item['image'] = product.scc('......').extract_first()
        return item
'''这个response已含有上述meta字典，此句将这个字典赋值给item，完成信息传递。
这个item已经和parse中的item一样了
之后我们就可以做图片url提取的工作了，
数据提取完成后return item ，这样就完成了数据抓取的任务了。'''
