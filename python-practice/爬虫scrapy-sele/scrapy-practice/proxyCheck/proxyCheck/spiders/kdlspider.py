# -*- coding: utf-8 -*-
import scrapy
from proxyCheck.items import ProxycheckItem

class KdlspiderSpider(scrapy.Spider):
    name = 'kdlspider'
    allowed_domains = ['kuaidaili.com']
    start_urls = ['http://kuaidaili.com/']
    for i in range(1,6):
        start_urls.append('http://www.kuaidaili.com/free/inha/' + str(i) + '/')


    def parse(self, response):
        item = ProxycheckItem()
        main = response.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr')

        for trtr in main:
            ip = trtr.xpath("td/text()").extract()[0]
            port = trtr.xpath("td/text()").extract()[1]
            item["addressIP"] = ip + ":" + port
            yield item
            