import os
import sys 
from scrapy.cmdline import execute

sys.path.append(os.path.join(os.getcwd()))
execute('scrapy crawl book -o book.json'.split())
