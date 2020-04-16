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
        #print(response.text)
        company_detail = response.meta['company_detail']
        root = response.xpath("//div[@class='content page_event_content']")[0]

        company_name = root.xpath("//div[@stat][@id='detail']//table[@class='m_table']//tr[1]""//td[2]//spa"
                                  "n/text()")[0].extract()
        company_detail['company_name'] = company_name

        print("=====高管信息准备完毕，休息一下嘻嘻====")
        root1 = response.xpath("//div[@id='manager'][@stat='company_manag"
                               "er']//div[@id='ml_001'][@class='m_tab_content']/"
                               "table[@class='m_table managelist m_hl']/tbody/tr[1]/td[@clas"
                               "s='tc name'][1]//table[@class='m_table ggintro']/thead/tr[1]//h3/text()").getall()
        # 这里要写个嵌套循环 首先对tr循环，其次对td进行循环 获取里面和外面的信息
        contents = response.xpath("//div[@id='manager'][@stat='company_manag"
                                  "er']//div[@id='ml_001'][@class='m_tab_content']/"
                                  "table[@class='m_table managelist m_hl']/tbody/tr")
        # print(type(contents))
        company_content2_1 = list()
        for content in contents:
            single = dict()
            content_1 = content.xpath("./td[1]/a/text()").getall()
            single['content_1'] = "".join(content_1).strip()
            content_2 = content.xpath("./td[2]/text()").getall()
            single['content_2'] = "".join(content_2).strip()
            content_3 = content.xpath("./td[3]//span/text()").getall()
            single['content_3'] = "".join(content_3).strip()
            content_4 = content.xpath("./td[4]//span/text()").getall()
            single['content_4'] = "".join(content_4).strip()
            content_5 = content.xpath("./td[5]/a/text()").getall()
            single['content_5'] = "".join(content_5).strip()
            content_6 = content.xpath("./td[6]/text()").getall()
            single['content_6'] = "".join(content_6).strip()
            content_7 = content.xpath("./td[7]//span/text()").getall()
            single['content_7'] = "".join(content_7).strip()
            content_8 = content.xpath("./td[8]//span/text()").getall()
            single['content_8'] = "".join(content_8).strip()
            company_content2_1.append(single)
            company_detail['company_content2_1'] = company_content2_1

        contents1 = response.xpath("//div[@id='manager'][@stat='company_manag"
                                   "er']//div[@id='ml_002'][@class='m_tab_content']/"
                                   "table[@class='m_table managelist m_hl']/tbody/tr")
        company_content2_2 = list()
        for content in contents1:
            single1 = dict()
            content_1 = content.xpath("./td[1]/a/text()").getall()
            single1['content_1'] = "".join(content_1).strip()
            content_2 = content.xpath("./td[2]/text()").getall()
            single1['content_2'] = "".join(content_2).strip()
            content_3 = content.xpath("./td[3]//span/text()").getall()
            single1['content_3'] = "".join(content_3).strip()
            content_4 = content.xpath("./td[4]//span/text()").getall()
            single1['content_4'] = "".join(content_4).strip()
            content_5 = content.xpath("./td[5]/a/text()").getall()
            single1['content_5'] = "".join(content_5).strip()
            content_6 = content.xpath("./td[6]/text()").getall()
            single1['content_6'] = "".join(content_6).strip()
            content_7 = content.xpath("./td[7]//span/text()").getall()
            single1['content_7'] = "".join(content_7).strip()
            content_8 = content.xpath("./td[8]//span/text()").getall()
            single1['content_8'] = "".join(content_8).strip()
            company_content2_2.append(single1)
            company_detail['company_content2_2'] = company_content2_2

        contents3 = response.xpath("//div[@id='manager'][@stat='company_manag"
                                   "er']//div[@id='ml_003'][@class='m_tab_content']/"
                                   "table[@class='m_table managelist m_hl']/tbody/tr")
        company_content2_3 = list()
        for content in contents3:
            single2 = dict()
            content_1 = content.xpath("./td[1]/a/text()").getall()
            single2['content_1'] = "".join(content_1).strip()
            content_2 = content.xpath("./td[2]/text()").getall()
            single2['content_2'] = "".join(content_2).strip()
            content_3 = content.xpath("./td[3]//span/text()").getall()
            single2['content_3'] = "".join(content_3).strip()
            content_4 = content.xpath("./td[4]//span/text()").getall()
            single2['content_4'] = "".join(content_4).strip()
            content_5 = content.xpath("./td[5]/a/text()").getall()
            single2['content_5'] = "".join(content_5).strip()
            content_6 = content.xpath("./td[6]/text()").getall()
            single2['content_6'] = "".join(content_6).strip()
            content_7 = content.xpath("./td[7]//span/text()").getall()
            single2['content_7'] = "".join(content_7).strip()
            content_8 = content.xpath("./td[8]//span/text()").getall()
            single2['content_8'] = "".join(content_8).strip()
            company_content2_3.append(single2)
            company_detail['company_content2_3'] = company_content2_3
        time.sleep(random.randint(2, 5))
        yield company_detail

