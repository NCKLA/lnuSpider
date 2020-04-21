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
        while row_num <= 10:
            # 将表中第一列的1-100行数据写入data数组中
            data.append(sheet.cell(row=row_num, column=3).value)
            row_num = row_num + 1
        for i in data:
            company_lr = JqkaLssuanceRelatedItem()
            url = 'http://basic.10jqka.com.cn/%s' % i + '/company.html'
            company_lr['url'] = url
            # print(response.text)
            yield scrapy.Request(company_lr['url'],
                                 meta={'company_lr': company_lr}, callback=self.detail_ni, dont_filter=True)
        return

    def detail_ni(self, response):
        print("=====准备详细情况中的第一部分信息====")
        company_lr = response.meta['company_lr']
        root = response.xpath("//div[@class='content page_event_content']")[0]
        # print(root)
        company_lr['name'] = root.xpath("//div[@stat][@id='detail']//table[@class='m_table']//tr[1]""//td[2]//spa"
                                            "n/text()")[0].extract()
        content1 = response.xpath("//div[@id='publish'][@stat='company_publish']/div[@class='bd pr']/"
                                  "table[@class='m_table']//tr[1]")

        content11 = content1.xpath("./td[1]/span/text()").getall()
        print(content11)
        content12 = content1.xpath("./td[2]/span/text()").getall()
        print(content12)
        content13 = content1.xpath("./td[3]/span/text()").getall()
        print(content13)

        content2 = response.xpath("//div[@id='publish'][@stat='company_publish']/div[@class='bd pr']/"
                                  "table[@class='m_table']//tr[2]")
        content21 = content2.xpath("./td[1]/span/text()").getall()
        print(content21)
        content22 = content2.xpath("./td[2]/span/text()").getall()
        print(content22)
        content23 = content2.xpath("./td[3]/span/text()").getall()
        print(content23)

        content3 = response.xpath("//div[@id='publish'][@stat='company_publish']/div[@class='bd pr']/"
                                  "table[@class='m_table']//tr[3]")
        content31 = content3.xpath("./td[1]/span/text()").getall()
        print(content31)
        content32 = content3.xpath("./td[2]/span/text()").getall()
        print(content32)
        content33 = content3.xpath("./td[3]/span/text()").getall()
        print(content33)

        content4 = response.xpath("//div[@id='publish'][@stat='company_publish']/div[@class='bd pr']/"
                                  "table[@class='m_table']//tr[4]")
        content41 = content4.xpath("//div[@class='main_sell'][1]/span/text()").getall()
        print(content41)
        content42 = content4.xpath("//div[@class='main_sell'][2]/span/text()").getall()
        print(content42)

        content5 = response.xpath("//div[@id='publish'][@stat='company_publish']//p[@class='tip lh24']/text()").getall()
        content5 = "".join(content5).strip()
        print(content5)

        time.sleep(random.randint(2, 5))
        yield company_lr
