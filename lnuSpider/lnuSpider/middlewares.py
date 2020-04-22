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
import random


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

        self.driver = webdriver.PhantomJS(executable_path=r'C:\Users\10359\local\bin\phantomjs.exe')
        self.driver.set_page_load_timeout(40)
        # self.driver = webdriver.PhantomJS(executable_path=r'e:\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows
        # \bin\phantomjs.exe')

    def process_request(self, request, spider):
        if spider.name == 'sohucaijing_Spider':

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

            # 整数 额外获取的数据包数量，一包20条新闻，只要初始的20条就改成0  不保证因为网卡产生的数据损失
            ex_packages_amount = 4

            url = request.url
            if 'https://' in request.url:
                url = request.url[9:]

            # print("在中间件请求的连接：" + url)
            spider.driver.get(url)

            if 'mp.sohu.com/profile?xpt=c29odWNqeWMyMDE3QHNvaHUuY29t' in url:
                for temp in range(0, ex_packages_amount):
                    for x in range(1, 12, 2):
                        i = (float(x) / 11)/(temp+1) + temp/(temp+1)
                        # scrollTop 从上往下的滑动距离
                        # print("中间件：准备执行这个滚动js")
                        js = 'document.body.scrollTop=document.body.scrollHeight * %f' % i
                        time.sleep(1)
                        spider.driver.execute_script(js)
                        time.sleep(1)
            else:
                for x in range(1, 12, 2):
                    i = float(x) / 11
                    # scrollTop 从上往下的滑动距离
                    # print("中间件：准备执行这个滚动js")
                    js = 'document.body.scrollTop=document.body.scrollHeight * %f' % i
                    time.sleep(1)
                    spider.driver.execute_script(js)
                    time.sleep(1)

            response = HtmlResponse(url=url,
                                    body=spider.driver.page_source,
                                    encoding='utf-8',
                                    request=request)
            # print("中间件：准备return这个response")
            # 这个地方只能返回response对象，当返回了response对象，那么可以直接跳过下载中间件，将response的值传递给引擎，引擎又传递给 spider进行解析
            return response


class WzhHexunDownLoaderMiddleware(object):
    USER_AGENTS = ["Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201",
                   "Mozilla/5.0 (Windows; U; Windows NT 6.1; it; rv:2.0b4) Gecko/20100818",
                   "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
                   "Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko",
                   "Mozilla/5.0 (compatible; MSIE 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1;"
                   " .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0",
                   "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:77.0) Gecko/20190101 Firefox/77.0",
                   "Mozilla/5.0 (X11; Linux ppc64le; rv:75.0) Gecko/20100101 Firefox/75.0",
                   "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.10; rv:75.0) Gecko/20100101 Firefox/75.0",
                   "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:77.0) Gecko/20100101 Firefox/77.0",
                   "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; TencentTraveler 4.0; Trident/4.0;"
                   " SLCC1; Media Center PC 5.0; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30618)",
                   "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; QQDownload 1.7; GTB6.6; TencentTrav"
                   "eler 4.0; SLCC1; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.5.30729; .NET CLR 3.0.30729)",
                   "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; iCafeMedia; TencentTraveler 4.0; "
                   "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; .NET CLR 1.1.4322; .NET CLR 2.0.50727;"
                   " .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)",
                   "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; TencentTraveler 4.0; QQDownload 667; SLCC1;"
                   " .NET CLR 2.0.50727; .NET CLR 3.0.04506)",
                   "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; QQPinyin 686; QQDownload 661; GTB6.6; "
                   "TencentTraveler 4.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
                   "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; QQDownload 1.7; GTB6.6; "
                   "TencentTraveler 4.0)",
                   "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.3a) Gecko/20021207 Phoenix/0.5",
                   "Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.3a) Gecko/20021207 Phoenix/0.5",
                   "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.4a) Gecko/20030411 Phoenix/0.5",
                   "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.3a) Gecko/20021207 Phoenix/0.5",
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582",
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                   " Chrome/70.0.3538.102 Safari/537.36 Edge/18.19577",
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                   "(KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
                   "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 "
                   "(KHTML, like Gecko) Chrome/55.0.2919.83 Safari/537.36",
                   "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko)"
                   " Chrome/54.0.2866.71 Safari/537.36",
                   "Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16.2",
                   "Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16",
                   "Opera/9.80 (Macintosh; Intel Mac OS X 10.14.1) Presto/2.12.388 Version/12.16",
                   "Mozilla/5.0 (Windows NT 6.0; rv:2.0) Gecko/20100101 Firefox/4.0 Opera 12.14",
                   "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko)"
                   " Version/7.0.3 Safari/7046A194A",
                   "Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko)"
                   " Version/6.0 Mobile/10A5355d Safari/8536.25",
                   "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.13+ (KHTML, like Gecko)"
                   " Version/5.1.7 Safari/534.57.2"]

    def __init__(self):

        self.driver = webdriver.PhantomJS(executable_path=r'C:\Users\G50\local\bin\phantomjs.exe')
        self.driver.set_page_load_timeout(40)

    def process_request(self, request, spider):
        request.headers['User-Agent'] = random.choice(self.USER_AGENTS)

        time.sleep(5)
        url = request.url
        # 我自己用的时候出现了访问网页多出‘https:///’的情况，如果存在会把这段剪去

        print("在中间件请求的连接：" + url)
        time.sleep(5)

        if request.url.startswith("http://"):
            request.meta['proxy'] = "http://" + spider.domain + ":" + spider.port  # http代理
        elif request.url.startswith("https://"):
            request.meta['proxy'] = "https://" + spider.domain + ":" + spider.port

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

        return None

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


class IpProxyDownloaderMiddleware(object):
    def __init__(self):
        pass

    def process_request(self):
        pass


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
