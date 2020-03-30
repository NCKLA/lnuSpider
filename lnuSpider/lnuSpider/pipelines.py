# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import JsonLinesItemExporter
import time
import json
from lnuSpider import settings_wzh
import urllib3


class LnuspiderPipeline(object):
    def __init__(self):
        ssstime = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
        self.fp = open("lnuSpider/data/json/搜狐号_搜狐财经_"+ssstime+".json", 'wb')
        self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False)
        self.http = urllib3.PoolManager()

    def open_spider(self, spider):
        print("=====爬虫开始力=====")

    def process_item(self, item, spider):
        dir_path = '%s/%s' % (settings_wzh.IMAGES_STORE, "sohucaijing")
        # 下载图片
        for src in item['images_src'][0]:
            file_path = '%s/%s' % (dir_path, src.split('/')[-1])
            r = self.http.request('GET', src)
            with open(file_path, 'wb') as f:
                f.write(r.data)
            f.close()

        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.fp.close()
        print("=====爬虫结束力=====")


# class SohuImagePipeline(ImagesPipeline):
#     def open_spider(self, spider):
#         ssstime = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
#         self.fp = open("lnuSpider/data/json/搜狐号_搜狐财经_"+ssstime+".json", 'wb')
#         self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False)
#         print("=====爬虫开始力=====")
#
#     def process_item(self, item, spider):
#         self.exporter.export_item(item)
#         return item
#
#     def close_spider(self, spider):
#         self.exporter.finish_exporting()
#         self.fp.close()
#         print("=====爬虫结束力=====")
#
#     def get_media_requests(self, item, info):
#         for src in item['images_src'][0]:
#             print("准备yield图片：".join(src))
#             yield scrapy.Request(url=src, meta={'src': src, 'title': item['title']})
#
#     def file_path(self, request, response=None, info=None):
#         src = request.meta['src']
#         title = request.meta['title']
#         # 设置图片的路径为  类型名称/url地址
#         # 这是一个图片的url: http://pics.sc.chinaz.com/Files/pic/icons128/7065/z1.png
#         # 这句代码的意思是先取出图片的url，[0]表示从列表转成字符串
#         # split分割再取最后一个值，这样写是让图片名字看起来更好看一点
#         image_name = src.split('/')[-1]
#         path = '%s/%s' % (title, image_name)
#         print("path===".join(path))
#         return path


class JqkaPipeline(object):
    def __init__(self):
        self.fp = open("jqka.json", 'w', encoding='utf-8')

    def open_spider(self, spider):
        print ('爬虫开始了')

    def process_item(self, item, spider):
        #item变成字典类型dict()
        item_json = json.dumps(dict(item), ensure_ascii=False)
        self.fp.write(item_json+'\n')
        return item

    def close_spider(self, spider):
        self.fp.close()
        print ('爬虫结束了')