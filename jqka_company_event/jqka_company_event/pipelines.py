# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import time
from scrapy.exporters import JsonLinesItemExporter

class JqkaCompanyEventPipeline:
    def __init__(self):
        now_time = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
        self.fp = open(r"C:\python\lnuSpider\data\json\同花顺上市公司公司大事" + now_time + ".json", 'wb')
        self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False)
        # self.http = urllib3.PoolManager()

    def open_spider(self, spider):
        print("=====爬虫开始了=====")

    def process_item(self, company_ce, spider):
        self.exporter.export_item(company_ce)
        return company_ce

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.fp.close()
        print("=====爬虫结束了=====")