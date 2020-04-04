# -*- coding: utf-8 -*-
import random
from jqka_com_detail.items import JqkaComDetailItem
from scrapy import item
from scrapy.http import Request
#获取excel需要引入的包
from openpyxl import load_workbook
from selenium import webdriver
import time
import scrapy


class JqkaComDetailSpiderSpider(scrapy.Spider):

    def __init__(self):
        self.driver = webdriver.PhantomJS(executable_path=r'C:\Users\10359\local\bin\phantomjs.exe')
        self.driver.set_page_load_timeout(40)

    name = 'jqka_com_detail_spider'
    allowed_domains = ["basic.10.jqka.com"]

    def start_requests(self):
         yield Request("http://basic.10jqka.com.cn/603221/company.html", headers={'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"})

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
            company_detail = JqkaComDetailItem()
            url = 'http://basic.10jqka.com.cn/'+i+'/company.html'
            url = "".join(url)
            company_detail['url'] = url
            # print(url)
            # print(response.text)
            yield scrapy.Request(company_detail['url'],
                                 meta={'company_detail': company_detail}, callback=self.detail_ni, dont_filter=True)
        return

    def detail_ni(self, response):
        company_detail = response.meta['company_detail']
        root = response.xpath("//div[@class='content page_event_content']")[0]
        print(root)
        company_name = root.xpath("//div[@stat][@id='detail']//table[@class='m_table']//tr[1]""//td[2]//spa"
                                  "n/text()")[0].extract()
        company_detail['company_name'] = company_name

        company_location = root.xpath("//div[@stat][@id='detail']//table[@class='m_table']//tr[1]""//td[3]//spa"
                                      "n/text()")[0].extract()
        company_detail['company_location'] = company_location

        company_english_name = root.xpath("//div[@stat][@id='detail']//table[@class='m_table']//tr[2]""//td[1]//spa"
                                          "n/text()")[0].extract()
        company_detail['company_english_name'] = company_english_name

        company_industry = root.xpath("//div[@stat][@id='detail']//table[@class='m_table']//tr[2]""//td[2]//s"
                                      "pan/text()")[0].extract()
        company_detail['company_industry'] = company_industry

        company_before_name= root.xpath("//div[@stat][@id='detail']//table[@class='m_table']//tr[3]""//td[1]//s"
                                        "pan/text()")[0].extract()
        company_detail['company_before_name'] = company_before_name

        company_url = root.xpath("//div[@stat][@id='detail']//table[@class='m_table']//tr[3]""//td[2]//s"
                                 "pan/a/text()")[0].extract()
        company_detail['company_url'] = company_url

        # company_start_time = root.xpath("//div[@stat][@id='publish']//table[@class='m_table']""//tr[1]//td["
        #                                 "1]//span/text()")[0].extract()
        # company_detail['company_start_time'] = company_start_time
        #
        # company_market_time = root.xpath("//div[@stat][@id='publish']//table[@class='m_table']//tr[2]"
        #                                  "//td[1]//span/text()")[0].extract()
        #
        # company_detail['company_market_time'] = company_market_time
        time.sleep(random.randint(2, 5))
        yield company_detail





