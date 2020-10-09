# -*- coding: utf-8 -*-

# Scrapy settings for NetLending project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'NetLending'

SPIDER_MODULES = ['NetLending.spiders']
NEWSPIDER_MODULE = 'NetLending.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'NetLending (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
LOG_LEVEL="WARNING"

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
# 'Accept-Encoding': 'gzip, deflate, br',
# 'Accept-Language': 'zh-CN,zh;q=0.9,en-GB;q=0.8,en-XA;q=0.7,en;q=0.6',
# 'Connection': 'keep-alive',
# 'Content-Length': '64',
# 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
# 'Cookie': '__jsluid_s=aca8e48eaa7f8a46ce1060077b1001a0; _ga=GA1.2.1130660300.1601685935; _gid=GA1.2.1073006868.1601685935; gr_user_id=05c39165-24aa-4493-931b-61aa576fde81; __jsluid_h=0afbbede0da8a03fe1bd018c7b93a6f5; wdzj_session_source=https%253A%252F%252Fwww.wdzj.com%252Fdangan%252Fdianping%252F%2523nogo; WDZJptlbs=1; Hm_lvt_9e837711961994d9830dcd3f4b45f0b3=1601685935,1601769221,1601856023,1601865394; Hm_lpvt_9e837711961994d9830dcd3f4b45f0b3=1601865394; gr_session_id_1931ea22324b4036a653ff1d3a0b4693=b351183d-5bd4-4b72-9f98-d1ff4f3552dd; _gat=1; gr_session_id_1931ea22324b4036a653ff1d3a0b4693_b351183d-5bd4-4b72-9f98-d1ff4f3552dd=true',
# 'Host': 'www.wdzj.com',
# 'Origin': 'https://www.wdzj.com',
# 'Referer': 'https://www.wdzj.com/dangan/dianping/',
# 'Sec-Fetch-Dest': 'empty',
# 'Sec-Fetch-Mode': 'cors',
# 'Sec-Fetch-Site': 'same-origin',
#
# 'X-Requested-With': 'XMLHttpRequest'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
   'NetLending.middlewares.NetlendingSpiderMiddleware': 543,
}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'NetLending.middlewares.NetlendingDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'NetLending.pipelines.NetlendingPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
