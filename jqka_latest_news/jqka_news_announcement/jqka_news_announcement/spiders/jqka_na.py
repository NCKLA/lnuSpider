# -*- coding: utf-8 -*-
import scrapy


class JqkaNaSpider(scrapy.Spider):
    name = 'jqka_na'
    allowed_domains = ['http://basic.10jqka.com.cn/603221/index.html']
    start_urls = ['http://http://basic.10jqka.com.cn/603221/index.html/']

    def parse(self, response):
        pass
