# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from cjw.items import CjwItem

class CjwSpiderSpider(CrawlSpider):
    name = 'cjw_spider'
    allowed_domains = ['caijing.com.cn']
    start_urls = ['http://finance.caijing.com.cn/']

    rules = (
        Rule(LinkExtractor(allow=r'http://finance.caijing.com.cn/.+'), follow=True),
        Rule(LinkExtractor(allow=r".+2.+\.shtml"), callback="parse_item", follow=False)
    )

    def parse_item(self, response):
        print(response.text)
        title = response.xpath("//div[@id='article']/h2[@id='cont_title']/text()").get()
        source = response.xpath("//div[@class='ar_source']//a[@href='http://www.caijing.com.cn']/text()").get()
        date = response.xpath("//div[@class='ar_source']//span[@id='pubtime_baidu']/text()").get()
        article = response.xpath("//div[@id='the_content']/p//text()").getall()
        # title = "".join(title)
        # source = "".join(source)
        # date = "".join(date)
        article = "".join(article).strip()
        print('='*30)
        print(title)
        print(source)
        print(date)
        print(article)
        print('='*30)
        item = CjwItem(title=title, source=source, date=date, article=article)
        yield item