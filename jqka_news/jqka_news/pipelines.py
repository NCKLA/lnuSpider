# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import random
import time
import os.path
from os.path import join, basename, dirname
from urllib.parse import urlparse
from scrapy.pipelines.files import FilesPipeline
import scrapy
from scrapy.exporters import JsonLinesItemExporter


class JqkaNewsPipeline(FilesPipeline):
    def get_media_requests(self, company_news, info):
        yield scrapy.Request(company_news['news_url'], meta={'title': company_news['news_tag']})

    def file_path(self, request, response=None, info=None):
        url = urlparse(request.url).path
        name = request.meta.get('title')
        return join(basename(dirname(url)), basename(name))

    time.sleep(random.randint(3, 5))

    # def __init__(self):
    #     now_time = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
    #     self.fp = open(r"C:\python\lnuSpider\data\json\同花顺上市公司新闻公告" + now_time + ".json", 'wb')
    #     self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False)
    #     # self.http = urllib3.PoolManager()
    #
    # def open_spider(self, spider):
    #     print("=====爬虫开始了=====")
    #
    # def process_item(self, company_news, spider):
    #     # dir_path = '%s/%s' % (settings_wzh.IMAGES_STORE, "sohucaijing")
    #     # # 下载图片
    #     # for src in item['images_src'][0]:
    #     #     file_path = '%s/%s' % (dir_path, src.split('/')[-1])
    #     #     r = self.http.request('GET', src)
    #     #     with open(file_path, 'wb') as f:
    #     #         f.write(r.data)
    #     #     f.close()
    #     self.exporter.export_item(company_news)
    #     return company_news
    #
    # def close_spider(self, spider):
    #     self.exporter.finish_exporting()
    #     self.fp.close()
    #     print("=====爬虫结束了=====")