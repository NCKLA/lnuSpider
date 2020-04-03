# -*- coding: utf-8 -*-
import scrapy


class JqkaComDetailSpiderSpider(scrapy.Spider):
    name = 'jqka_com_detail_spider'
    allowed_domains = ['basic.10.jqka.com']
    start_urls = ['http://basic.10.jqka.com/']

    def parse(self, response):
        root = response.xpath("//div[@class='content page_event_content/*']").extract()
        print(root)
        root1 = response.xpath("//div[@class='content page_event_content/*']")
        print(type(root1))

