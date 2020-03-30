# -*- coding: utf-8 -*-
import random
import time

import scrapy
from jqka.items import JqkaItem
from scrapy import Request
from scrapy.http.response.html import HtmlResponse
from scrapy.selector.unified import SelectorList


class JqkaSpiderSpider(scrapy.Spider):
    name = 'jqka_spider'
    allowed_domains = ['news.10jqka.com.cn']
    start_urls = ['http://news.10jqka.com.cn/today_list/index_3.shtml']

    def start_requests(self):
        yield Request("http://news.10jqka.com.cn/today_list/index_3.shtml", headers={'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"})

    def parse(self, response):

        contents = response.xpath(".//div[@class='list-con']/ul/li")

        for content in contents:
            # item放在循环体里面
            item = JqkaItem()
            url = content.xpath(".//span/a/@href").get()
            tag = content.xpath("//div[@class='mysite']/span/a/text()").getall()
            item['tag'] = "".join(tag).strip()
            item['url'] = url
            yield scrapy.Request(item['url'], meta={'item': item}, callback=self.detail)
        # 翻页操作
        # return
        print("========准备翻页========")
        next_url = response.xpath("//span[@class='num-container']/a[last()]/@href").getall()
        next_url = "".join(next_url)
        if not next_url:
            print("===结束===")
            return
        else:
            yield scrapy.Request(next_url, callback=self.parse)
            print("=====翻页成功======")

    def detail(self, response):
        # 接收上级已爬取的数据
        print("========已经进入内页=========")
        item = response.meta['item']
        # 一级内页数据提取
        title = response.xpath("//h2[@class='main-title']/text()").getall()
        item['title'] = "".join(title).strip()

        item['source_name'] = response.xpath("//div[@class='info-fl fl']//a/text()").getall()
        item['source_name'] = "".join(item['source_name']).strip()

        item['date'] = response.xpath("//span[@id='pubtime_baidu']/text()").getall()
        item['date'] = "".join(item['date']).strip()

        item['cont'] = response.xpath("//div[@class='main-text atc-content']/p/text()").getall()
        item['cont'] = "".join(item['cont']).strip()
        yield item

        time.sleep(random.randint(1, 3))
        print("=======延时结束========")

