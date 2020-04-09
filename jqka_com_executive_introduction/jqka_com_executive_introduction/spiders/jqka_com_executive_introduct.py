# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import random
import re

from jqka_com_detail.jqka_com_detail.items import JqkaComDetailItem
from jqka_com_executive_introduction.items import JqkaComExecutiveIntroductionItem
from scrapy import item
from scrapy.http import Request
#获取excel需要引入的包
from openpyxl import load_workbook
from selenium import webdriver
import time
import scrapy


class JqkaComExecutiveIntroductSpider(scrapy.Spider):

    def __init__(self):
        self.driver = webdriver.PhantomJS(executable_path=r'C:\Users\10359\local\bin\phantomjs.exe')
        self.driver.set_page_load_timeout(40)

    name = 'jqka_com_executive_introduct'
    allowed_domains = ["basic.10.jqka.com"]

    def start_requests(self):
        yield Request("http://basic.10jqka.com.cn/603221/company.html", headers={
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"})

    def parse(self, response):
        book = load_workbook(filename=r"C:\python\lnuSpider\data\exel\com_list.xlsx")
        sheet = book.active
        data = []
        row_num = 1
        while row_num <= 10:
            # 将表中第一列的1-100行数据写入data数组中
            data.append(sheet.cell(row=row_num, column=3).value)
            row_num = row_num + 1
        for i in data:
            #需要改
            company_detail = JqkaComExecutiveIntroductionItem()
            #需要改
            url = 'http://basic.10jqka.com.cn/%s' % i + '/company.html'
            company_detail['url'] = url
            # print(response.text)
            yield scrapy.Request(company_detail['url'],
                                 meta={'company_detail': company_detail}, callback=self.detail_ni, dont_filter=True)
        return

    def detail_ni(self, response):
        print("=====准备高管介绍中的信息====")
        company_detail = response.meta['company_detail']
        root = response.xpath("//div[@class='content page_event_content']")[0]

        company_name = root.xpath("//div[@stat][@id='detail']//table[@class='m_table']//tr[1]""//td[2]//spa"
                                  "n/text()")[0].extract()
        company_detail['company_name'] = company_name
        print("=====高管信息准备完毕，休息一下嘻嘻====")
        time.sleep(random.randint(2, 5))
        yield company_detail

