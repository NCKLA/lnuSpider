# -*- coding: utf-8 -*-
import scrapy


class WzhtonghuashunSpider(scrapy.Spider):
    name = 'wzhtonghuashun'
    allowed_domains = ['basic.10jqka.com.cn/603221/news.html']
    start_urls = ['http://basic.10jqka.com.cn/603221/news.html']

    def parse(self, response):
        print(response.text)
