# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import requests
import scrapy
from scrapy.http import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline

class KrystalPipeline(ImagesPipeline):
    # 继承ImagesPipeline, 最重要的是
    # 重写get_media_requests(self, item, info)
    # 和item_completed(self, results, item, info)

    # 这两个函数不能改名字
    def get_media_requests(self,item,info):
        for image_url in item['image_urls']:
            yield Request(image_url)
        # self.file = open('/Users/luxixi/luxixi2018/startgit/gitpractice/{}/{}.jpg'.format(item['file_name'],item['image_name']),'wb')

    def item_completed(self,results, item,info):
        image_path = [x['path'] for ok, x in results if ok]
        if not image_path:
            raise DropItem("Item contains no images")
        item['image_path'] = image_path
        return item
    
    # 如果想改文件名字
    # def file_path(self,request,response=None,info=None):
    #    filename = request.meta['image_name']
    #    return filename

    # # 将图片转移至以 post_id 为名的子目录中
    # for (dest, src) in image_paths.items():
        # dir = settings.IMAGES_STORE
        # newdir = dir + os.path.dirname(src) + '/' + item['post_id'] + '/'
        # if not os.path.exists(newdir):
            # os.makedirs(newdir)
        # os.rename(dir + src, newdir + dest)
    # 将保存路径保存于 item 中（image_paths 需要在 items.py 中定义）
    # item['image_paths'] = image_paths
    # return item