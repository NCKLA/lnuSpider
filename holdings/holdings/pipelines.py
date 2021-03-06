# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import JsonLinesItemExporter


class HoldingsPipeline(object):

    def __init__(self):
        # now_time = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
        self.fp = open("1.json", 'wb')
        self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False)
        # self.http = urllib3.PoolManager()

    def open_spider(self, spider):
        print("=====爬虫开始力=====")

    def process_item(self, company_share, spider):
        # dir_path = '%s/%s' % (settings_wzh.IMAGES_STORE, "sohucaijing")
        # # 下载图片
        # for src in item['images_src'][0]:
        #     file_path = '%s/%s' % (dir_path, src.split('/')[-1])
        #     r = self.http.request('GET', src)
        #     with open(file_path, 'wb') as f:
        #          f.write(r.data)
        #     f.close()
        self.exporter.export_item(company_share)
        return company_share

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.fp.close()
        print("=====爬虫结束力=====")