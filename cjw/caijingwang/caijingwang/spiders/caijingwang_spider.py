# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.http.response.html import HtmlResponse
from scrapy.selector.unified import SelectorList
from caijingwang.items import CaijingwangItem


class CaijingwangSpiderSpider(scrapy.Spider):
    name = 'caijingwang_spider'
    # allowed_domains = ['caijing.com']
    # start_urls = ['http://finance.caijing.com.cn/bank/1.shtml']

    def start_requests(self):
        start_urls = ['http://finance.caijing.com.cn/bank/1.shtml',#爬取不同模块（银行、保险、基金、互联网金融、支付、信托、债券、期货、综合）
                      'http://finance.caijing.com.cn/insurance/1.shtml',
                      'http://finance.caijing.com.cn/fund/1.shtml',
                      'http://finance.caijing.com.cn/market/1.shtml',
                      'http://finance.caijing.com.cn/zhifu/1.shtml',
                      # 'http://finance.caijing.com.cn/trust/1.shtml',
                      'http://finance.caijing.com.cn/bondfutures/1.shtml',
                      'http://finance.caijing.com.cn/newfutures/1.shtml',
                      'http://finance.caijing.com.cn/localfinance/1.shtml', ]
        for url in start_urls:
            yield Request(url, headers={
                'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"})
    def parse(self, response):
        infos = response.xpath("//div[@class='main_lt']/ul[@class='list']//li")
        for info in infos:
            item = CaijingwangItem()
            url = info.xpath(".//div/a/@href").get()
            item['url'] = url
            yield scrapy.Request(url, meta={'item': item}, callback=self.detail_parse)
        next_url = response.xpath("//div[@class='main_lt']/div[@class='thepg']//li[last()]/a/@href").getall()
        next_url = "".join(next_url)
        if not next_url:
            return
        else:
            yield scrapy.Request(next_url, callback=self.parse)

    def detail_parse(self, response):
        item = response.meta['item']

        title = response.xpath("//div[@id='article']/h2//text()").get()
        item['title'] = title

        source = response.xpath("//span[@id='source_baidu']//text()").get()
        item['source'] = source

        date = response.xpath("//span[@id='pubtime_baidu']//text()").get()
        item['date'] = date

        article = response.xpath("//div[@id='the_content']/p//text()").getall()
        item['article'] = article

        editor = response.xpath("//div[@class='ar_writer']/span//text()").getall()
        item['editor'] = editor

        yield item
