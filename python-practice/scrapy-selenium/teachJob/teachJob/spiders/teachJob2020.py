# -*- coding: utf-8 -*-
import scrapy
import requests
import json 
import re 
from teachJob.items import TeachjobItem
from ..settings import DEFAULT_REQUEST_HEADERS


class Teachjob2020Spider(scrapy.Spider):
    name = 'teachJob2020'
    allowed_domains = ['qgsydw.com']
    start_urls = ['http://www.qgsydw.com/']
    indexList = [2,3,4]
    def create_url(self):
        for page in self.indexList:
            url = 'http://www.qgsydw.com/qgsydw/recruit/insrecruit/index_{page}.html'.format(page=page)
            yield scrapy.Request(url,callback=self.parse)

    def parse(self, response):
        job_ad_list  = response.xpath("//div[@class='sydw_ny_main1_right_list_nr']/ul/li")
        data = TeachjobItem()
        for i in range(1,len(job_ad_list)+1):
            data['日期'] = response.xpath('html/body/div[4]/div[2]/div[2]/ul/li[{}]/span'.format(i)).text
            data['标题'] = response.xpath('html/body/div[4]/div[2]/div[2]/ul/li[{}]/a'.format(i)).text
            print(data['标题'])
            data['省份'] = re.findall(r'\[\w*\]',str(data['标题']))[0]
            print(data['省份'])
            data['url_address'] = response.xpath('html/body/div[4]/div[2]/div[2]/ul/li[{}]/a'.format(i)).get_attribute('href')

            yield data

        # next_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        
