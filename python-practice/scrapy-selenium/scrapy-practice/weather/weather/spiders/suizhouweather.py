# -*- coding: utf-8 -*-
import scrapy
import re 
from weather.items import WeatherItem

class SuizhouweatherSpider(scrapy.Spider):
    name = 'suizhouweather'

    allowed_domains = ['tianqi.com/suizhou']
    start_urls = ['https://www.tianqi.com/suizhou/30/']
    
    # citylist = ['suizhou','wuhan','shenzhen']
    # for city in citylist:
    #     start_urls.append('http://tianqi.com/'+ city +'/15/')

    def parse(self, response):
        itemslist = []
        items = WeatherItem()
        weatherday = response.xpath('//div[@class= "table_day "]')
        for item in weatherday:
            items["date"] = item.xpath('./h3/b/text()').extract()
            items["weekday"] = item.xpath('./h3/text()').extract()
            weather = item.xpath('./ul/li[@class="temp"]//text()').extract()
            items["weather"] = weather
            items["tempHigh"] = item.xpath('./ul/li[@class="temp"]/b/text()').extract()
            items["wind"] = item.xpath('./ul/li[3]/text()').extract()
            yield items 
            itemslist.append(items)
        return itemslist
    