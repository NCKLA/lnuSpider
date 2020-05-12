# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import JsonLinesItemExporter
import time
import json
import settings_wzh
import urllib3


class LnuspiderPipeline(object):

    def __init__(self):
        ssstime = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
        self.fp = open("wzhProject/data/json/搜狐号_搜狐财经_"+ssstime+".json", 'wb')
        self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False)

        self.http = urllib3.PoolManager()

    def open_spider(self, spider):
        print("=====爬虫开始力=====")

    def process_item(self, item, spider):
        # dir_path = '%s/%s' % (settings_wzh.IMAGES_STORE, "sohucaijing")
        # # 下载图片
        #
        # for src in item['images_src'][0]:
        #     file_path = '%s/%s' % (dir_path, src.split('/')[-1])
        #     r = self.http.request('GET', src)
        #     with open(file_path, 'wb') as f:
        #         f.write(r.data)
        #     f.close()
        #
        # self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.fp.close()
        print("=====爬虫结束力=====")


class WzhTongHuaShunPipeline(object):
    # def __init__(self):
    #     ssstime = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
    #     self.fp = open("wzhProject/data/json/搜狐号_搜狐财经_"+ssstime+".json", 'wb')
    #     self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False)
    #     self.http = urllib3.PoolManager()

    def open_spider(self, spider):
        print("=====同花顺爬虫开始力=====")

    def process_item(self, item, spider):

        return item

    def close_spider(self, spider):
        # self.exporter.finish_exporting()
        # self.fp.close()

        print("=====同花顺爬虫结束力=====")


class WzhHexunPipeline(object):
    # def __init__(self):
    #     ssstime = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
    #     self.fp = open("wzhProject/data/json/搜狐号_搜狐财经_"+ssstime+".json", 'wb')
    #     self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False)
    #     self.http = urllib3.PoolManager()

    def open_spider(self, spider):
        print("=====和讯爬虫开始力=====")

    def process_item(self, item, spider):
        return item

    def close_spider(self, spider):
        # self.exporter.finish_exporting()
        # self.fp.close()

        # 记得关闭用的端口
        spider.ip_proxy.spider_api_close_port(spider.ip_proxy.port)

        print("=====和讯爬虫结束力=====")


class SohucaijingPipeline(object):
    def __init__(self):
        ssstime = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
        self.fp = open("wzhSpider/data/json/搜狐号_搜狐财经_"+ssstime+".json", 'wb')
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

# class SeleniumSpiderMiddleware(object):
#     def __init__(self):
#         self.options = Options()
#         self.options.add_argument('-headless')  # 无头参数
#         self.driver = None
#
#     def process_request(self, request, spider):
#         if spider.name == 'sohucaijing_Spider':
#
#             self.driver = Firefox(executable_path='geckodriver', firefox_options=self.options)
#             # 配了环境变量第一个参数就可以省了，不然传绝对路径
#             wait = WebDriverWait(self.driver, timeout=10)
#
#             # 当引擎从调度器中取出request进行请求发送下载器之前
#             # 会先执行当前的爬虫中间件 ，在中间件里面使用selenium
#             # 请求这个request ，拿到动态网站的数据 然后将请求
#             # 返回给spider爬虫对象
#             # 使用爬虫文件的url地址
#
#             self.driver.get(request)
#             # wait.until(expected.visibility_of_element_located((By.NAME, 'q'))).send_keys(
#             #     'headless firefox' + Keys.ENTER)
#             # wait.until(expected.visibility_of_element_located((By.CSS_SELECTOR, '#ires a'))).click()
#             # print(self.driver.page_source)
#
#             for x in range(1, 12, 2):
#                 i = float(x) / 11
#                 # scrollTop 从上往下的滑动距离
#                 js = 'document.body.scrollTop=document.body.scrollHeight * %f' % i
#                 self.driver.execute_script(js)
#             response = HtmlResponse(url=request.url,
#                                     body=spider.driver.page_source,
#                                     encoding='utf-8',
#                                     request=request)
#             # 这个地方只能返回response对象，当返回了response对象，那么可以直接跳过下载中间件，将response的值传递给引擎，
#             # 引擎又传递给 spider进行解析
#             self.driver.close()
#             self.driver.quit()
#             return response


# class SohuImagePipeline(ImagesPipeline):
#     def open_spider(self, spider):
#         ssstime = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
#         self.fp = open("wzhProject/data/json/搜狐号_搜狐财经_"+ssstime+".json", 'wb')
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
        ssstime = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
        self.fp = open("jqka"+ssstime+".json", 'w', encoding='utf-8')

    def open_spider(self, spider):
        print('爬虫开始了')

    def process_item(self, item, spider):
        # item变成字典类型dict()
        item_json = json.dumps(dict(item), ensure_ascii=False)
        self.fp.write(item_json+'\n')
        return item

    def close_spider(self, spider):
        self.fp.close()
        print('爬虫结束了')