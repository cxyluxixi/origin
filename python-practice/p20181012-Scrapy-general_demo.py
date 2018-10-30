# -*- coding: utf-8 -*-
import scrapy
class DemoSpider(scrapy.Spider):
    # 爬虫初始值配置,比如url
    name = "demo"
    #allowed_domains = ["python123.io"]
    start_urls = ['https://python123.io/ws/demo.html']
    
    # 上述start_urls， 可以改写为生成器写法，节约内存空间
    # def start_requests(self):
    #     urls = ['url1','url2','url3',,,,]
    #     for url in urls:
    #         yield scrapy.Request(url = url,callback=self.parse)


    # 将获取到的每个url的html页面进行解析，储存在字典中，然后保存为文件
    def parse(self, response):
        fname = response.url.split('/')[-1]
        with open(fname, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s.' % fname)
