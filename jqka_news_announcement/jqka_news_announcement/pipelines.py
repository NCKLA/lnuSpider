# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import time
from scrapy.exporters import JsonLinesItemExporter

class JqkaNewsAnnouncementPipeline:
    def __init__(self):
        now_time = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
        self.fp = open(r"C:\python\lnuSpider\data\json\同花顺上市公司新闻公告" + now_time + ".json", 'wb')
        self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False)

    def open_spider(self, spider):
        print("=====爬虫开始了=====")

    def process_item(self, company_na, spider):
        self.exporter.export_item(company_na)
        return company_na

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.fp.close()
        print("=====爬虫结束了=====")
