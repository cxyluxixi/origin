# -*- coding: utf-8 -*-

# Scrapy settings for music163 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'music163'

SPIDER_MODULES = ['music163.spiders']
NEWSPIDER_MODULE = 'music163.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'music163 (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 2

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Host': 'music.163.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'DNT': '1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'https://music.163.com/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': '__f_=1543496405268; _ntes_nnid=2b2587bd1eda1d5e4943db6c9a8b2aaf,1543496405430; _ntes_nuid=2b2587bd1eda1d5e4943db6c9a8b2aaf; UM_distinctid=16789819c901449-0779e7d3953477-1e396652-13c680-16789819c91633; vjuids=17ff6bfe3.16789819ebd.0.72c901b276548; s_n_f_l_n3=034639a63cfedfcb1544200232652; _antanalysis_s_id=1544200232939; NTES_CMT_USER_INFO=47256352%7Clumengxi9404%7Chttp%3A%2F%2Fmimg.126.net%2Fp%2Fbutter%2F1008031648%2Fimg%2Fface_big.gif%7Cfalse%7CbHVtZW5neGk5NDA0QDEyNi5jb20%3D; vjlast=1544200233.1545124484.11; ne_analysis_trace_id=1545124484472; vinfo_n_f_l_n3=034639a63cfedfcb.1.0.1544200232651.0.1545124515730; _ga=GA1.2.209431621.1545204584; _iuqxldmzr_=32; playliststatus=visible; WM_TID=eaOFWnTLFg9FRUFBRVY5O6HWlE2l0cZ9; hb_MA-BFF5-63705950A31C_u=%7B%22utm_source%22%3A%20%22cp-1018878377%22%2C%22utm_medium%22%3A%20%22share%22%2C%22utm_campaign%22%3A%20%22commission%22%2C%22utm_content%22%3A%20%22%22%2C%22utm_term%22%3A%20%22%22%2C%22promotional_id%22%3A%20%22%22%7D; starttime=; NNSSPID=07604b0be2af448c84eced6c86492ae1; MUSIC_EMAIL_U=7b70706cbb75bc30468d7d1126bb7c99ed19902973ea9ffd0aded41878c115e952db2b0fa53a0445d3644bf36d601cf61e28fa1146adac0d7955a739ab43dce1; NTES_SESS=.VxAE2uBDP5kZVwHMU2TpDdZ1b78wUVpWNFIrEWPNz9KkrW0kCD17o_SvTEihn_B8OWspKXNvymaeroCakgrct89EwLrxNZ7IVxg18zaJWMf1gejH3L5tsgvvb.xxsgxVNAEhe7Wmi0xlxJCcT6URbZQczWFV1rybGIN7USgBO78mmRgaQoG65kS6pPNo_gy762l12JpvO3ltc24M8u8RbIbt; S_INFO=1548581548|0|#1&5#|lumengxi9404@126.com#chidianhaodeluxixi; P_INFO=lumengxi9404@126.com|1548581548|0|rms|00&99|bej&1548574622&urs#bej&null#10#0#0|&0|urs|lumengxi9404@126.com; mail_psc_fingerprint=06a8416db9268c64d86b51e5cd3d2705; mp_MA-9ADA-91BF1A6C9E06_hubble=%7B%22sessionReferrer%22%3A%20%22https%3A%2F%2Fcampus.163.com%2F%23%2Fhome%22%2C%22updatedTime%22%3A%201548581716771%2C%22sessionStartTime%22%3A%201548581716766%2C%22sendNumClass%22%3A%20%7B%22allNum%22%3A%202%2C%22errSendNum%22%3A%200%7D%2C%22deviceUdid%22%3A%20%22cc7ecf92-52a7-4abb-99d4-aa1e6ed1f364%22%2C%22persistedTime%22%3A%201543677010031%2C%22LASTEVENT%22%3A%20%7B%22eventId%22%3A%20%22da_screen%22%2C%22time%22%3A%201548581716772%7D%2C%22sessionUuid%22%3A%20%220b25294c-da41-4287-9f39-4a3e74fd8342%22%7D; WM_NI=j48wSZMJ8tuOwkkEfY7W7E8Vq%2FQR7W7sCCRj9n%2FM5YmGB%2BITyl%2Fbe0Dw9phhBVeE0m8CFvUoB%2Bfy8bPVKc47PVxMut9Mrvb%2FQJxXkoK3NeUgpf5eB7OcDVP0z6ru46qCNlA%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeccdb3a938db7acc13be9eb8fb6d14b839a9a85f3689b959ba3d55bbca9e58fb62af0fea7c3b92aaaecf898d2528f96f895f845b5b5a5a6e553f589f9a6bb5eb3f19fb3b65df5ad8da4d162fbb2e1aeb853af998ecccc60bbb4e183e83c88a9f791eb64828aaba6b367fc9d8a97d86582f5aa9abb6a948a8584b73d948ab8aef880fb93be97e1259396b8b9ea6589ed8286d86db4bafb86c13d8dbd8cb7d33cbaeabe96b73eb39d828dc437e2a3; JSESSIONID-WYYY=oQnirfdnJlR9myn4uPFbYh0flfMJVgA4ey8hjCJmIfruqp4ZoW3VSuf9FgWlYYC7oNrTwmZwfUIjWRR0Q9xQ0UzV1CryCU1hJH%5CTWbkI2%5CVJ0R%2FswDk0sl0EmBbEv%2Frjnjna3Ss4R%2BvuvQ9%5CPFElFzjlgQN%5C%2FySohaeh%2F5tm1vh74mcF%3A1548743707386',

}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'music163.middlewares.Music163SpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'music163.middlewares.Music163DownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
#    'music163.pipelines.Music163Pipeline': 300,
    'music163.pipelines.Music163MongoPipeline':345,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
