# -*- coding: utf-8 -*-
import scrapy


class SuizhouweatherSpider(scrapy.Spider):
    name = 'suizhouweather'

    allowed_domains = ['tianqi.com/suizhou']
    start_urls = ['http://tianqi.com/suizhou/15/']
    
    # citylist = ['suizhou','wuhan','shenzhen']
    # for city in citylist:
    #     start_urls.append('http://tianqi.com/'+ city +'/15/')

    def parse(self, response):
        items = []
        weatherday = response.xpath('//div[@class= "table_day"]')
        
        pass
