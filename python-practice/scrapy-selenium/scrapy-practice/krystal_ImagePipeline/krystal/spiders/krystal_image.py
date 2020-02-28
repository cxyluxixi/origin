# -*- coding: utf-8 -*-
import scrapy
from krystal.items import KrystalItem
from selenium import webdriver 
from scrapy.spiders import CrawlSpider
import time
from selenium.webdriver.common.keys  import Keys




class KrystalImageSpider(scrapy.Spider):
    name = 'krystal_image'
    allowed_domains = ['image.baidu.com']
    start_urls = ['http://image.baidu.com/']

    key = '郑秀晶'
    base_url = 'http://image.baidu.com/'
    
    def parse(self,respone):

        # 打开搜索页面
        page_search = webdriver.Chrome()
        page_search.get(self.base_url)
        time.sleep(1)

        # 输入要搜索的关键词
        key_word = page_search.find_element_by_xpath('//*[@id="kw"]')
        key_word.send_keys(self.key)
        key_word.send_keys(Keys.ENTER)
        time.sleep(3)

        # 滚动条，找到全部图片的url
        scroll_js = 'var q = document.documentElement.scrollTop={}'
        for i in range(1,100000,10000):
            page_search.execute_script(scroll_js.format(i))
            time.sleep(3)
        image_urls = page_search.find_elements_by_xpath('//*[@id="imgid"]/div/ul/li/div[1]/a/img')

        # 获取每个图片的url
        image_u =[]
        image_k = KrystalItem()
        for item in image_urls:
            url_pic = item.get_attribute("data-imgurl")
            image_u.append(url_pic)
            
        image_k['image_urls'] = image_u
        yield image_k
        
        # 返回image_urls， 使用ImagePipeline
        # yield{
        #     'image_urls':image_u
        # }

