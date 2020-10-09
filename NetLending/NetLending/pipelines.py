# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import  re
from scrapy.exporters import JsonLinesItemExporter
class NetlendingPipeline:
    def __init__(self):
        #wb以二进制方式打开
        self.fp=open("comments.json",'wb')
        self.exporter=JsonLinesItemExporter(self.fp,ensure_ascii=False,encoding='utf-8')
    def open_spider(self,spider):
        print("爬虫开始了...")
    def process_item(self,item,spider):
        self.exporter.export_item(item)
        return item
    def process_info(self,info):
        info=[re.sub(r"\t|\n|\s","",i) for i in info]
        info=[i for i in info if len(i)>0]
        return info
    def close_spider(self,spider):
        self.fp.close()
        print("爬虫结束了...")
