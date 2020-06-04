# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.http.response.html import HtmlResponse
from scrapy.selector.unified import SelectorList
from caijingwangyc.items import CaijingwangycItem


class CaijingwangycSpiderSpider(scrapy.Spider):
    name = 'caijingwangyc_spider'
    # allowed_domains = ['caijing.com']
    # start_urls = ['http://www.caijing.com.cn/original/']

    def start_requests(self):
        yield Request("http://www.caijing.com.cn/original/1.shtml", headers={
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"})

    def parse(self, response):
        infos = response.xpath("//div[@class='main_lt']/ul[@class='list']//li")
        for info in infos:
            item = CaijingwangycItem()
            url = info.xpath(".//div/a/@href").get()
            item['url'] = url
            date = response.xpath(".//div[@class='time']//text()").get()
            item['date'] = date
            yield scrapy.Request(item['url'], meta={'item': item}, callback=self.detail_parse)
        next_url = response.xpath("//div[@class='main_lt']/div[@class='thepg']//li[last()]/a/@href").getall()
        next_url = "".join(next_url)
        if not next_url:
            return
        else:
            yield scrapy.Request(next_url, callback=self.parse)

    def detail_parse(self, response):
        item = response.meta['item']

        title = response.xpath("//div[@class='article']/h2//text()").get()
        item['title'] = title

        article = response.xpath("//div[@class='article-content']/p//text()").getall()
        item['article'] = article

        print('=========================')
        print(title)
        print(article)
        print('=========================')
        yield item
