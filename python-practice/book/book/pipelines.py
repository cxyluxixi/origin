# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import scrapy
from book.items import BookItem


# 验证数值
class BookPipeline(object):
    def process_item(self, item, spider):
        if(item['name']):
            item['price'] = 'price'+ item['price']
            return item
        else:
            raise ('missing price in %s' % item)

# 验证重复id
class DuplicatesPipeline(object):

    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        if item['id'] in self.ids_seen:
            raise ("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(item['id'])
            return item

# 写入json文件
class JsonWritePipeline(object):
    def __init__(self):
        self.file = open('items.json','wb')
        
    def process_item(self,item,spider):
        line = json.dumps(dict(item)) + '\n'
        self.file.write(line)
        return item

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
        即meta={'item':item}，这个meta参数会被放在Request对象里一起发送给parse2()函数。
        '''
    def parse_page2(self,response):
        item = response.meta['item']
        for product in response.css('......').extract():
            item['image'] = product.scc('......').extract_first()
        return item
'''这个response已含有上述meta字典，此句将这个字典赋值给item，完成信息传递。
这个item已经和parse中的item一样了
之后我们就可以做图片url提取的工作了，
数据提取完成后return item ，这样就完成了数据抓取的任务了。'''


# Scrapy内置的request子类，FormRequest这个专门为form表单设计，模拟表单提交的示例
class LoginSpider(scrapy.Spider):
    name = 'example.com'
    start_urls = ['http://www.example.com/users/login.php']

    def parse(self, response):
        return scrapy.FormRequest.from_response(response,
            formdata={'username': 'john', 'password': 'secret'},
            callback=self.after_login
        )
'''     return [FormRequest(url="http://www.example.com/post/action",
                formdata={'name': 'John Doe', 'age': '27'}, 
                callback=self.after_post)]
'''

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
