#-*- encoding=utf-8 -*-
#@time :2020/4/12/012 10:06
#@author : hyz
#@Filr:start.py
#@Software:PyCharm

#scrapy框架下的hexunspider的启动文件
from scrapy import cmdline
cmdline.execute("scrapy crawl hexunspider".split())