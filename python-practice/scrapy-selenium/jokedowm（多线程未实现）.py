import requests
from lxml import etree
import threading
from threading import Thread
from queue import Queue


# 本代码学习教程，多线程  https://zhuanlan.zhihu.com/p/38540042

class Crawl(Thread):
    def __init__(self,crawl_id,page_queue):
        Thread.__init__(self)
        self.thread_id = crawl_id
        self.page_queue = page_queue

    def run(self):
        print('start crawl:' + self.thread_id)
        self.parse_Page(self.get_Page())
        print('end crawl:' + self.thread_id)


    def get_Page(self):
        # 构建请求头
        page = self.page_queue.get()
        url = 'http://www.qiushibaike.com/8hr/page/' + str(page) + '/'
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'}
        response = requests.get(url,headers=headers,timeout=10)
        if response.status_code == 200:
            # 从网站分析出响应内容的编码
            # print(response.encoding)
            response.encoding = 'UTF-8'
            # print(response.text)
            return response.text
        else:
            print("请求网页失败")

class parser(threading.Thread):
    def __init__(self,parser_id,data_queue,lock):
        threading.Thread.__init__(self)
        self.parser_id = parser_id
        self.data_queue = data_queue
        self.lock = lock

    def run(self):
        print()

    def parse_Page(self,html):
        html_lxml = etree.HTML(html)
        # 获取到每一块的所有内容
        datas = html_lxml.xpath('//div[contains(@id,"qiushi_tag")]')
        # print(datas)
        item = {}
        for data in datas:
            # print(data.attrib)    
            # 用户名称
            username = data.xpath('.//h2')[0].text.strip()
            # 糗事内容
            content = data.xpath('.//div[@class="content"]/span')[0].text.strip()
            # 评论数
            comments = data.xpath('.//span[@class="stats-comments"]/a/i')[0].text
            # 好笑数
            vote = data.xpath('.//span[@class="stats-vote"]/i')[0].text
            # 图片
            image = data.xpath('.//div[@class="thumb"]/a/@img')

            item = {
            'username':username,
            'content':content,
            'vote':vote,
            'comments':comments,
            'image':image
            }
            print(item)





if __name__ == '__main__':
    # 将html文本存入队列
    data_queue = Queue()
    # 设置结束线程变量
    Flag = False
    # 设置指令锁
    lock = threading.Lock()

    page_queue = Queue(20)
    for page in range(1,4):
        page_queue.put(page)

    # 初始化采集线程
    crawl_thread = []
    crawl_list = ['crawl-1','crawl-2','crawl-3']
    for crawl_id in crawl_list:
        crawl = Crawl(crawl_id,page_queue)
        crawl.start()
        crawl_thread.append(crawl)


