# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class TeachjobPipeline(object):
    def process_item(self, item, spider):
        return item

class Teachjob2020Pipeline(object):
    def __init__(self):
        # 注意这里写入文件时，不要用wb，因为item不是二进制的，是字典，字符串
        self.filename= 'jobnews.json'
        self.file = open(self.filename,'a+')

    def open_file(self,spider):
        self.file = open(self.filename,'a')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False)+','+'\n'
        # json.dump(dict(item),self.file,ensure_ascii=False)
        self.file.write(line)

        # 使用flush， 刷新文件，因为文件写入，会积攒一部分数据再写入，不会每次一点点就写
        self.file.flush()
        return item

    def close_spier(self,spider):
        self.file.close()