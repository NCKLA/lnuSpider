# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import time
import urllib3
from scrapy.exporters import JsonLinesItemExporter

class WangdaizhijiaPipeline(object):
    def __init__(self):
        ssstime = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
        self.fp = open("评论详情" + ssstime + ".json", 'wb')
        self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False)
        self.http = urllib3.PoolManager()
        pass

    def open_spider(self, spider):
        print("=====爬虫开始力=====")
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.fp.close()
        print("=====爬虫结束力=====")
    pass

