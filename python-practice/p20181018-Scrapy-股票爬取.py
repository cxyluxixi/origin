# spider文件配置

# -*- coding: utf-8 -*-
# (HTML信息提取）使用css selector 来获取和解析页面
import scrapy
import re

class StockSpider(scrapy.Spider):
    name = "stocks"
    start_urls = ["https://quote.eastmoney.com/stocklist.html"]

    def start_requests(self,response):
        for href in response.css('a::attr(href)').extract():
            try:
                stock = []
                stock.append(re.findall(r"[s][hz]\d{6}", href)[0])
                url = 'https://gupiao.baidu.com/stock/' + stock + '.html'
                yield scrapy.Request(url,callback=self.parse_stock)
            except:
                continue
    
    def parse_stock(self,response):
        infoStock = {}
        stockInfo = response.css('.stock-bets')
        name = stockInfo.css('.bets-name').extract()
        keyList = stockInfo.css('.dt').extract()
        valueList = stockInfo.css('.dd').extract()
        for i in range(len(keyList)):
            key = re.findall(r'>.*</dt>',keyList[i])[0][1:-5]
            try:
                val = re.findall(r'\d+\.?.*</dd>',valueList[i])[0][0:-5]
            except:
                val = '--'
                infoStock[key] = val 
        infoStock.update({
            '股票名称': re.findall(r'\s.*\(',name)[0].split()[0] + \
            re.findall(r'\>.*\<',name )[0][1:-1]
        })

        yield infoStock



# pipelines 文件配置

# -*- coding: utf-8 -*-
class BaidustocksPipeline(object):
    def process_item(self,item,spider):
        return item

# 定义对爬取项的处理类
class BaidustockInfoPipeline(object):
    # 打开文件
    def open_spider(self,spider):
        self.f = open('BaidustockInfo.txt','w')
    
    # 写入文件
    def close_spider(self,spider):
        self.f.close()

    # 这个函数对每个item进行处理
    def process_item(self,item,spider):
        try:
            line = str(dict(item)) + '\n'
            self.f.write(line)
        except:
            pass 
        return item


# 配置settings.py文件的ITEM_PIPELINES选项
# 将自己定义在52行的BaidustockInfoPipeline，添加到字典中
ITEM_PIPELINES = {
    'BaiduStocks.pipelines.BaidustocksInfoPipeline': 300,
}