# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import JsonLinesItemExporter
import time


class LnuspiderPipeline(object):

    def __init__(self):
        ssstime = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
        self.fp = open("lnuSpider/data/json/搜狐号_搜狐财经_"+ssstime+".json", 'wb')
        self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False)

    def open_spider(self, spider):
        print("=====爬虫开始力=====")

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.fp.close()
        print("=====爬虫结束力=====")

