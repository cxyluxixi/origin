# -*- coding: utf-8 -*-
import scrapy
from book.items import BookItem


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
