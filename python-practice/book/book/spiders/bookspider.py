# -*- coding: utf-8 -*-
import scrapy
from book.items import BookItem

# 创建project  scrapy startproject spidername
# cd切换目录到爬虫目录，编写items.py， 设置数据表中需要有哪些指标，如：name=spider.Field()
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
            item['name'] = name,
            item['price'] = price
            yield item
        


        # 提取下一页链接
        next_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        # next_url = response.css('ul.pager li.next a::attr(href)').extract_first()
        if next_url:
            # 构造下一页链接
            next_url = response.urljoin(next_url)
            # 构造新的Request对象
            yield scrapy.Request(next_url, callback=self.parse)
