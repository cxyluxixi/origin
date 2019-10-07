# -*- coding: utf-8 -*-

'''
1.复杂跳转，回调
2.爬取Ajax生成的数据（网易云音乐评论）
'''

import time
import scrapy
import json
import requests
from selenium import webdriver
from music163.items import Music163Item
from ..settings import DEFAULT_REQUEST_HEADERS



class MusicSpider(scrapy.Spider):
    name = 'music'
    allowed_domains = ['163.com']
    start_urls = ['http://music.163.com/']

    base_url = 'http://music.163.com/'

    # id 是歌手页面，歌手分类的url中显示的id值
    # initials 是歌手分类的歌手名字拼音首字母的url中的initial值
    ids = ['1001','1002','1003','2001','2002','2003','6001','6002','6003','7001','7002','7003','4001','4002','4003']
    initials = [65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,0]
    def start_requests(self):
        for id in self.ids:
            for initial  in self.initials:
                each_url = '{url}/#/discover/artist/cat?id={id}&initial={initial}'.format(url=self.base_url,id=id,initial=initial)

                yield scrapy.Request(each_url,callback = self.parse_artists_url)

    
    def parse_artists_url(self, response):
        artists_url = response.xpath('//*[@class="sml"]/a[1]/@href').extract()
        for artist_url in artists_url:
            # artist_url 长这样"/artist?id=961075"
            artist_url = self.base_url +'/#/artist/album?'+artist_url[8:]
            yield scrapy.Request(artist_url, callback=self.parse_artist_albums)


    def parse_artist_albums(self,response):
        
        albums_url = response.xpath('//p[@class="dec dec-1 f-thide2 f-pre"]/a/@href').extract()
        mm = Music163Item()
        for album in albums_url:
            # /album?id=71720086
            album_url = self.base_url  + '#'+ album
            driver = webdriver.Chrome()
            driver.get(album_url)
            time.sleep(1)
            driver.switch_to_frame('contentFrame')
            musics = driver.find_elements_by_xpath('//span[@class="txt"]/a')
            # for item in musics:
            #     music_url = item.get_attribute('href')
            #     music_id = music_url[-10:]
            #     yield scrapy.Request(music_url,callback=self.parse_music,meta={'id':music_id,'url':music_url})
            for item in musics:
                music_url = item.get_attribute('href')
                # music_id = music[9:]
                # music_url = base_url + music
                text_comments = []
                driver.get(music_url)
                time.sleep(1)
                driver.switch_to_frame('contentFrame')
                comments = driver.find_elements_by_xpath('//div[@class="itm"]/div[2]/div[1]/div')
                for i in range(1,len(comments)+1):

                    comment = driver.find_element_by_xpath('//div[@class="itm"][{}]/div[2]/div[1]/div'.format(i))
                    text_comment = comment.text
                    # print(text_comment)
                    text_comments.append(text_comment)



                    music = driver.find_element_by_xpath('//div[@class="tit"]/em[@class="f-ff2"]').text
                    artist = driver.find_element_by_xpath('//div[@class="cnt"]/p[1]/span/a').text
                    album = driver.find_element_by_xpath('//div[@class="cnt"]/p[2]/a').text
                    # print(music,artist,album)
                

                # 为方便写入文件，这里强制转化为str，会减少很多麻烦，比如WebElement无法写入，
                    mm['id'] = str(music_url)
                    mm['music'] = str(music)
                    mm['album'] = str(album)
                    mm['artist'] = str(artist)
                mm['comments'] = str(text_comments)

                print(driver.title)
                driver.close()
                yield mm
