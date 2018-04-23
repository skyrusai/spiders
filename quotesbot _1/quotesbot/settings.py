# -*- coding: utf-8 -*-

# Scrapy settings for quotesbot project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

IPPOOL=[  
    {"ipaddr":"61.129.70.131:8080"},  
    {"ipaddr":"61.152.81.193:9100"},  
    {"ipaddr":"120.204.85.29:3128"},  
    {"ipaddr":"219.228.126.86:8123"},  
    {"ipaddr":"61.152.81.193:9100"},  
    {"ipaddr":"218.82.33.225:53853"},  
    {"ipaddr":"223.167.190.17:42789"} ,
    {"ipaddr":"64.62.220.40:80"},  
    {"ipaddr":"35.196.89.215:80"},  
    {"ipaddr":"66.82.123.234:8080"},  
    {"ipaddr":"34.202.223.70:80"},  
    {"ipaddr":"38.96.9.236:8008"},  
    {"ipaddr":"64.52.84.2:3128"},  
    {"ipaddr":"140.82.47.174:8080"}  	
]
# # 64.62.220.40:80
# # 35.196.89.215:80
# # 66.82.123.234:8080
# # 34.202.223.70:80
# # 38.96.9.236:8008
# # 64.52.84.2:3128
# # 140.82.47.174:8080
# 34.213.199.191:80
# 35.194.84.220:80
# 35.196.143.234:8080
# 45.55.220.79:80
# 168.235.93.162:8080
# 54.153.86.193:8080
# 143.104.238.70:80


BOT_NAME = 'quotesbot'

SPIDER_MODULES = ['quotesbot.spiders']
NEWSPIDER_MODULE = 'quotesbot.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'quotesbot (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True
# 设置用户代理池
#UPPOOL = [
#　　"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0", 
#]
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'quotesbot.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
   # 'quotesbot.middlewares.MyCustomDownloaderMiddleware': 543,
# }

#Enable or disable downloader middlewares
#See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
#   'quotesbot.middlewares.MyCustomDownloaderMiddleware': 543,
   'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware':123,
   'quotesbot.middlewares.MyproxiesSpiderMiddleware' : 125    
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'quotesbot.pipelines.SomePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'