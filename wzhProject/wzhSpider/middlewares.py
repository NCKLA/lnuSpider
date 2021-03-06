# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
# from selenium.webdriver import Firefox
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.support import expected_conditions as expected
# from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from scrapy.http.response.html import HtmlResponse
# from scrapy.http.response import Response
import time
import json
import requests
from lnu_utils.ip_proxy import LnuIPProxy

# import os
# import sys
# # 获取 路径
# file_path = os.path.dirname(os.path.abspath(__file__))
# # 修改运行路径
# sys.path.append(file_path)
# sys.path.insert(0, os.path.dirname(file_path))  # 0 表示优先级， 数字越大级别越低 修改模块的导入

from lnu_utils import random_user_agent


class LnuspiderSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class LnuspiderDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class SeleniumSpiderMiddleware(object):
    def __init__(self):
        # self.options = Options()
        # self.options.add_argument('-headless')  # 无头参数
        # self.driver = None

        # 火狐创建
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")  # 设置火狐为headless无界面模式
        options.add_argument("--disable-gpu")
        options.add_argument("service_args = ['–ignore - ssl - errors = true', '–ssl - protocol = TLSv1']")
        self.driver = webdriver.Firefox(firefox_options=options)

        # PhantomJS创建
        # self.driver = webdriver.PhantomJS(executable_path=r'C:\Users\G50\local\bin\phantomjs.exe',
        #                                   service_args=['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1'])

        self.driver.set_page_load_timeout(20)
        # self.driver = webdriver.PhantomJS(executable_path=r'e:\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows
        # \bin\phantomjs.exe')

    def process_request(self, request, spider):
        if spider.name == 'sohucaijing_Spider':
            request.headers['User-Agent'] = random_user_agent.give_a_head()

            # self.driver = Firefox(executable_path='geckodriver', firefox_options=self.options)
            # 配了环境变量第一个参数就可以省了，不然传绝对路径
            # wait = WebDriverWait(self.driver, timeout=10)

            # 当引擎从调度器中取出request进行请求发送下载器之前
            # 会先执行当前的爬虫中间件 ，在中间件里面使用selenium
            # 请求这个request ，拿到动态网站的数据 然后将请求
            # 返回给spider爬虫对象
            # 使用爬虫文件的url地址

            # self.driver.get(request)
            # wait.until(expected.visibility_of_element_located((By.NAME, 'q'))).send_keys(
            #     'headless firefox' + Keys.ENTER)
            # wait.until(expected.visibility_of_element_located((By.CSS_SELECTOR, '#ires a'))).click()
            # print(self.driver.page_source)

            # 整数，需要爬取的新闻数量，最好定义成整20
            news_amount = 1000

            # 整数 额外获取的数据包数量，一包20条新闻，只要初始的20条就改成0  不保证因为网卡产生的数据损失
            ex_packages_amount = int(news_amount/20) - 1

            url = request.url
            if 'https://' in request.url:
                url = request.url[9:]

            print("在中间件请求的连接：" + url)
            self.driver.get(url)

            if 'mp.sohu.com/profile?xpt=c29odWNqeWMyMDE3QHNvaHUuY29t' in url:
                for temp in range(0, ex_packages_amount):
                    # for x in range(1, 12, 2):
                    #     i = (float(x) / 11)/(temp+1) + temp/(temp+1)
                    #     # scrollTop 从上往下的滑动距离
                    #     # print("中间件：准备执行这个滚动js")
                    #     js = 'document.body.scrollTop=document.body.scrollHeight * %f' % i
                    #     time.sleep(1)
                    #     self.driver.execute_script(js)
                    self.driver.execute_script("document.documentElement.scrollTop=document.body.scrollHeight")
                    time.sleep(1)
                    print("现在的feed item数量："+str(len(self.driver.find_elements_by_class_name("feed-item"))))

                    # float_list = []
                    # for _ in range(0, 3):
                    #     float_list.append(random.random())
                    # float_list.sort()
                    # print("random list:" + str(float_list))
                    # for i in float_list:
                    #     js = 'document.body.scrollTop=document.body.scrollHeight * %f' % i
                    #     time.sleep(3)
                    #     spider.driver.execute_script(js)
                    #     time.sleep(3)

            else:
                for x in range(1, 6, 2):
                    i = float(x) / 5
                    # scrollTop 从上往下的滑动距离
                    # print("中间件：准备执行这个滚动js")
                    js = 'document.body.scrollTop=document.body.scrollHeight * %f' % i
                    time.sleep(1)
                    self.driver.execute_script(js)

            response = HtmlResponse(url=url,
                                    body=self.driver.page_source,
                                    encoding='utf-8',
                                    request=request)
            # print("中间件：准备return这个response")
            # 这个地方只能返回response对象，当返回了response对象，那么可以直接跳过Internet，将response的值传递给引擎，引擎又传递给 spider进行解析
            return response


class WzhHexunDownLoaderMiddleware(object):

    def process_request(self, request, spider):
        request.headers['User-Agent'] = random_user_agent.give_a_head()

        time.sleep(5)
        url = request.url
        # 我自己用的时候出现了访问网页多出‘https:///’的情况，如果存在会把这段剪去

        print("在中间件请求的连接：" + url)
        # time.sleep(5)

        if not spider.ip_proxy.port:
            spider.ip_proxy.spider_api_new_port()

        if request.url.startswith("http://"):  # http代理
            request.meta['proxy'] = "http://" + spider.ip_proxy.domain + ":" + spider.ip_proxy.port
        elif request.url.startswith("https://"):
            request.meta['proxy'] = "https://" + spider.ip_proxy.domain + ":" + spider.ip_proxy.port

        # js = 'document.body.scrollTop=document.body.scrollHeight * %f' % random.random()
        #
        # self.driver.execute_script(js)
        #
        # time.sleep(5)

        # response = HtmlResponse(url=url,
        #                         body=self.driver.page_source,
        #                         encoding='utf-8',
        #                         request=request)

        return None
        # return response

        # self.driver.get(url)
        # for x in range(1, 12, 2):
        #     i = float(x) / 11
        #     # scrollTop 从上往下的滑动距离
        #     js = 'document.body.scrollTop=document.body.scrollHeight * %f' % i
        #     time.sleep(5)
        #     self.driver.execute_script(js)
        #     time.sleep(5)
        #
        # response = HtmlResponse(url=url,
        #                         body=self.driver.page_source,
        #                         encoding='utf-8',
        #                         request=request)
        # 这个地方只能返回response对象，当返回了response对象，那么可以直接跳过下载中间件，将response的值传递给引擎，引擎又传递给 spider进行解析
        # return response

        #
        # # 翻页数量，获取比较麻烦，想了想就手动定吧
        # amount = 10
        #
        # url = request.url
        # print("中间件的request.url"+url)
        #
        # spider.driver.get(url)
        #
        # for _ in range(1, amount):
        #
        #     time.sleep(1)
        #     self.driver.find_element_by_class_name('next').click()
        #     time.sleep(1)
        #
        #     response = HtmlResponse(url=url,
        #                             body=spider.driver.page_source,
        #                             encoding='utf-8',
        #                             request=request)
        #     return response


class TongHuaShunDownloaderMiddleware(object):
    # def __init__(self):
    #     self.ip_proxy = LnuIPProxy()
    #     self.ip_proxy.spider_api_new_port()

    def process_request(self, spider, request):
        request.headers['User-Agent'] = random_user_agent.give_a_head()

        # time.sleep(5)
        # url = request.url
        # 我自己用的时候出现了访问网页多出‘https:///’的情况，如果存在会把这段剪去

        # print("在中间件请求的连接：" + url)
        # # time.sleep(5)
        #
        # if request.url.startswith("http://"):
        #     request.meta['proxy'] = "http://" + self.ip_proxy.domain + ":" + self.ip_proxy.port  # http代理
        # elif request.url.startswith("https://"):
        #     request.meta['proxy'] = "https://" + self.ip_proxy.domain + ":" + self.ip_proxy.port
        return None


class JqkaSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.
    #jqka
    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class JqkaDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class DongtaiMiddleware(object):
    def __init__(self):
        # 配置你的路径 max linux必须在/usr/local/bin   win必须在c盘，建议在c盘的用户文件目录下建一个/local/bin再把东西放进去
        self.driver = webdriver.PhantomJS(executable_path=r'C:\Users\G50\local\bin\phantomjs.exe')
        # 设置timeout 不设置大概会像我一样卡死
        self.driver.set_page_load_timeout(40)

    def process_request(self, request, spider):
        # 这里的爬虫名换成你自己的
        if spider.name == 'sohucaijing_Spider':

            url = request.url
            # 我自己用的时候出现了访问网页多出‘https:///’的情况，如果存在会把这段剪去
            if 'https://' in request.url:
                url = request.url[9:]

            # print("在中间件请求的连接：" + url)
            self.driver.get(url)
            for x in range(1, 12, 2):
                i = float(x) / 11
                # scrollTop 从上往下的滑动距离
                js = 'document.body.scrollTop=document.body.scrollHeight * %f' % i
                time.sleep(1)
                self.driver.execute_script(js)
                time.sleep(1)

            response = HtmlResponse(url=url,
                                    body=self.driver.page_source,
                                    encoding='utf-8',
                                    request=request)
            # 这个地方只能返回response对象，当返回了response对象，那么可以直接跳过下载中间件，将response的值传递给引擎，引擎又传递给 spider进行解析
            return response
