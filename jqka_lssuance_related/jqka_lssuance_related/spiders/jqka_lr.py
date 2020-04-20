# -*- coding: utf-8 -*-
import scrapy
import random
import re
from jqka_lssuance_related.items import JqkaLssuanceRelatedItem
from scrapy import item
from scrapy.http import Request
# 获取excel需要引入的包
from openpyxl import load_workbook
from selenium import webdriver
import time
import scrapy


class JqkaLrSpider(scrapy.Spider):
    name = 'jqka_lr'

    # allowed_domains = ['http://basic.10jqka.com.cn/603221/company.html']
    # start_urls = ['http://http://basic.10jqka.com.cn/603221/company.html/']
    def __init__(self):
        self.driver = webdriver.PhantomJS(executable_path=r'C:\Users\10359\local\bin\phantomjs.exe')
        self.driver.set_page_load_timeout(40)

    allowed_domains = ["basic.10.jqka.com"]

    def start_requests(self):
        yield Request("http://basic.10jqka.com.cn/603221/company.html", headers={
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"})

    def parse(self, response):
        # 读取excel表格
        book = load_workbook(filename=r"C:\python\lnuSpider\data\exel\com_list.xlsx")
        sheet = book.active
        data = []
        row_num = 1
        while row_num <= 500:
            # 将表中第一列的1-100行数据写入data数组中
            data.append(sheet.cell(row=row_num, column=3).value)
            row_num = row_num + 1
        for i in data:
            company_detail = JqkaLssuanceRelatedItem()
            url = 'http://basic.10jqka.com.cn/%s' % i + '/company.html'
            company_detail['url'] = url
            # print(response.text)
            yield scrapy.Request(company_detail['url'],
                                 meta={'company_detail': company_detail}, callback=self.detail_ni, dont_filter=True)
        return

    def detail_ni(self, response):
        print("=====准备详细情况中的第一部分信息====")
        company_detail = response.meta['company_detail']
        root = response.xpath("//div[@class='content page_event_content']")[0]
        # print(root)
        company_detail['name'] = root.xpath("//div[@stat][@id='detail']//table[@class='m_table']//tr[1]""//td[2]//spa"
                                            "n/text()")[0].extract()
        time.sleep(random.randint(2, 5))
        yield company_detail
