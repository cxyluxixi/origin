# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import json

class WeatherPipeline(object):
    def process_item(self, item, spider):
        base_dir = os.getcwd()
        filename = base_dir +'/weather.json'
        with open (filename,'a') as f:
            f.write(json.dumps(dict(item), ensure_ascii=False) + '\n')
        return item
