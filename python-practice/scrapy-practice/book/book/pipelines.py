# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import json
import scrapy
from book.items import BookItem
import requests


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
        self.file = open('items.json','w')
        
    def process_item(self,item,spider):
        line = json.dumps(dict(item),ensure_ascii=False)+',' +'\n'
        json.dump(line,self.file)
        return item  

    
# 保存图片，写入文件，wb二进制
class ImageWritePipeline(object):
    def process_item(self,item,spider):
        base_dir = os.getcwd()
        filename = base_dir + str(item['name'])+'.jpg'
        with open(filename,'wb') as f:
            f.write(requests.get(item['imgUrl']).content)
        return item