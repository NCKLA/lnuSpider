# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from nfcj.items import NfcjItem


class NfcjSpiderSpider(CrawlSpider):
    name = 'nfcj_spider'
    allowed_domains = ['southmoney.com']
    start_urls = ['http://www.southmoney.com/caijing/caijingyaowen/list_44_825.html']

    rules = (
        Rule(LinkExtractor(allow=r'.+list_44_\d\.html'), follow=True),
        Rule(LinkExtractor(allow=r".+caijingyaowen/.+\.html"), callback="parse_item", follow=True)
    )
    def parse_item(self, response):
        title = response.xpath("//div/h1[@class='artTitle']/text()").get()
        date_source = response.xpath("//p[@class='artDate']/text()").get()
        article = response.xpath("//div[@class='articleCon']//text()").getall()
        article = "".join(article).strip()
        print(title)
        print(date_source)
        print(article)
        print('='*30)

        item = NfcjItem(title=title, date_source=date_source, article=article)
        yield item