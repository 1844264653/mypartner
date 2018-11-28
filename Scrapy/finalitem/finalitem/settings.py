# -*- coding: utf-8 -*-

# Scrapy settings for finalitem project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'finalitem'

SPIDER_MODULES = ['finalitem.spiders']
NEWSPIDER_MODULE = 'finalitem.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'finalitem (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    'finalitem.middlewares.FinalitemSpiderMiddleware': 543,
}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'finalitem.middlewares.FinalitemDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'finalitem.pipelines.FinalitemPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


IPS = [
    'http://119.183.121.126:8118', 'http://219.238.186.188:8118', 'http://124.235.135.87:80',
    'http://180.168.13.26:8000', 'https://58.62.238.150:32431', 'https://210.22.160.34:48513',
    'https://118.181.226.22:37346', 'https://124.89.33.59:53281', 'https://221.1.200.242:38652',
    'https://101.236.57.214:8866', 'https://101.94.6.110:8123', 'https://221.6.32.206:50925',
    'https://121.228.49.232:3128', 'https://27.24.215.49:57248', 'https://115.231.5.230:44524',
    'https://183.15.122.42:3128', 'https://117.21.191.154:32431', 'https://119.254.94.95:43150',
    'https://222.94.147.198:808', 'http://118.178.227.171:80', 'https://221.234.250.30:8010',
    'https://183.45.88.109:61710', 'https://36.110.14.66:50519', 'https://106.3.79.57:31662',
    'https://182.88.15.114:8123', 'https://180.121.129.224:3128', 'https://113.200.27.10:53281',
    'https://115.223.85.244:8010', 'https://111.72.154.38:53128',
    'https://61.170.179.89:50799',
    'https://180.110.5.254:3128',
    'https://171.37.159.233:8123',
    'https://182.88.134.204:8123',
    'https://123.185.5.9:8118',
    'https://218.24.16.198:43620',
    'https://106.86.208.98:41683',
    'https://183.15.122.107:3128',
    'https://221.229.18.91:3128',
    'https://36.110.14.66:50519',
    'http://101.236.57.99:8866',
    'http://61.135.217.7:80',
    'http://182.88.163.65:8123',
    'http://121.31.195.239:8123',
    'http://119.250.252.59:8118',
    'http://117.91.253.119:8118',
    'http://120.26.127.90:8118',
]

USER_AGENT = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
    'Opera/8.0 (Windows NT 5.1; U; en)',
    'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
    'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
    'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
    'Chrome/17.0.963.56 Safari/535.11',
]

HTTPERROR_ALLOWED_CODES = [302]
