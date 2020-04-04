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



        self.driver = webdriver.PhantomJS(executable_path=r'C:\Users\G50\local\bin\phantomjs.exe')

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



            # 整数 额外获取的数据包数量，一包20条新闻，只要初始的20条就改成0

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





class dongtaiMiddleware(object):

    def __init__(self):

        # 配置你的路径 max linux必须在/usr/local/bin   win必须在c盘，建议在c盘的用户文件目录下建一个/local/bin再把东西放进去

        self.driver = webdriver.PhantomJS(executable_path=r'C:\Users\G50\local\bin\phantomjs.exe')



    def process_request(self, request, spider):

        # 这里的爬虫名换成你自己的

        if spider.name == 'sohucaijing_Spider':



            url = request.url

            # 我自己用的时候出现了访问网页多出‘https:///’的情况，如果存在会把这段剪去

            if 'https://' in request.url:

                url = request.url[9:]



            # print("在中间件请求的连接：" + url)

            spider.driver.get(url)

            for x in range(1, 12, 2):

                i = float(x) / 11

                # scrollTop 从上往下的滑动距离

                js = 'document.body.scrollTop=document.body.scrollHeight * %f' % i

                time.sleep(1)

                spider.driver.execute_script(js)

                time.sleep(1)



            response = HtmlResponse(url=url,

                                    body=spider.driver.page_source,

                                    encoding='utf-8',

                                    request=request)

            # 这个地方只能返回response对象，当返回了response对象，那么可以直接跳过下载中间件，将response的值传递给引擎，引擎又传递给 spider进行解析

            return response