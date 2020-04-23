# -*- coding: utf-8 -*-
import scrapy
import random
import re

from jqka_com_overview.items import JqkaComOverviewItem
from scrapy import item
from scrapy.http import Request
# 获取excel需要引入的包
from openpyxl import load_workbook
from selenium import webdriver
import time
import scrapy


class JqkaCoSpider(scrapy.Spider):
    def __init__(self):
        self.driver = webdriver.PhantomJS(executable_path=r'C:\Users\10359\local\bin\phantomjs.exe')
        self.driver.set_page_load_timeout(40)

    name = 'jqka_co'
    allowed_domains = ["basic.10.jqka.com"]

    def start_requests(self):
        yield Request("http://basic.10jqka.com.cn/603221/index.html", headers={
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"})

    def parse(self, response):
        # 读取excel表格
        book = load_workbook(filename=r"C:\python\lnuSpider\data\exel\com_list.xlsx")
        sheet = book.active
        data = []
        row_num = 1
        while row_num <= 1:
            # 将表中第一列的1-100行数据写入data数组中
            data.append(sheet.cell(row=row_num, column=3).value)
            row_num = row_num + 1
        for i in data:
            company_co = JqkaComOverviewItem()
            url = 'http://basic.10jqka.com.cn/%s' % i + '/index.html'
            company_co['url'] = url
            # print(response.text)
            yield scrapy.Request(company_co['url'],
                                 meta={'company_co': company_co}, callback=self.detail_ni, dont_filter=True)
        return

    def detail_ni(self, response):
        company_co = response.meta['company_co']

        content1 = response.xpath("//div[@class='m_box event new_msg z102']"
                                  "[@id='profile']//table"
                                  "[@class='m_table m_table_db']/tbody/tr[1]")

        content11 = content1.xpath("./td[1]/span/a/text()").getall()
        print(content11)
        content12 = content1.xpath("./td[2]/span[2]/text()").getall()
        print(content12)

        content2 = response.xpath("//div[@class='m_box event new_msg z102']"
                                  "[@id='profile']//table"
                                  "[@class='m_table m_table_db mt10']/tbody/tr[1]")
        content21 = content2.xpath("./td[1]/span/text()").getall()
        content21 = "".join(content21).strip()
        print(content21)
        content22 = content2.xpath("./td[2]/span/text()").getall()
        content22 = "".join(content22).strip()
        print(content22)
        content23 = content2.xpath("./td[3]/span/text()").getall()
        content23 = "".join(content23).strip()
        print(content23)
        content24 = content2.xpath("./td[4]/span[2]/text()").getall()
        content24 = "".join(content24).strip().replace(' ', '')
        print(content24)

        content2 = response.xpath("//div[@class='m_box event new_msg z102']"
                                  "[@id='profile']//table"
                                  "[@class='m_table m_table_db mt10']/tbody/tr[2]/td")
        for content_2 in content2:
            content_22 = content_2.xpath("./span/text()").getall()
            content_22 = "".join(content_22).strip().replace(' ', '')
            print(content_22)

        content3 = response.xpath("//div[@class='m_box event new_msg z102']"
                                  "[@id='profile']//table"
                                  "[@class='m_table m_table_db mt10']/tbody/tr[3]/td")
        for content_3 in content3:
            content_33 = content_3.xpath("./span/text()").getall()
            content_33 = "".join(content_33).strip().replace(' ', '')
            print(content_33)





        time.sleep(random.randint(1, 4))
        yield company_co
