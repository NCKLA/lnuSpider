# -*- coding: utf-8 -*-
import random
import re

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
        while row_num <= 500:
            # 将表中第一列的1-100行数据写入data数组中
            data.append(sheet.cell(row=row_num, column=3).value)
            row_num = row_num + 1
        for i in data:
            company_detail = JqkaComDetailItem()
            url = 'http://basic.10jqka.com.cn/%s' % i +'/company.html'
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

        company_before_name = root.xpath("//div[@stat][@id='detail']//table[@class='m_table']//tr[3]""//td[1]//s"
                                         "pan/text()")[0].extract()
        company_detail['company_before_name'] = company_before_name

        company_url = root.xpath("//div[@stat][@id='detail']//table[@class='m_table']//tr[3]""//td[2]//s"
                                 "pan/a/text()")[0].extract()
        company_detail['company_url'] = company_url






        print("=====准备详细情况中的第二部分信息中的第一部分====")
        company_content2_1 = list()
        company_comments = response.xpath("//div[@stat][@id='detail']//div[@class='m_tab_content2']")[0]
        # print(response.text)
        # print(company_comments)
        single = dict()
        company_main_business = company_comments.xpath("//tr[1]//span/text()")[0].extract()
        # print(company_main_business)
        single['company_main_business'] = company_main_business.strip()

        company_product_name = company_comments.xpath("//tr[@class='product_name']//span/span/text()")[0].extract()
        company_product_name = "".join(company_product_name).strip().replace(' ', '')
        # 去除字符串中存在的所有空格，调用re包
        company_product_name = re.sub('\s+', '', company_product_name).strip()
        # print(company_product_name)
        single['company_product_name'] = company_product_name.strip()

        company_controller_shareholder = company_comments.xpath("//div[@class='tipbox_wrap mr10']"
                                                                "//span/text()")[0].extract()
        single['company_controller_shareholder'] = "".join(company_controller_shareholder).strip()

        company_actual_shareholder = company_comments.xpath("//tr[3]//span/text()")[3].getall()
        single['company_actual_shareholder'] = "".join(company_actual_shareholder).strip()

        company_final_shareholder = company_comments.xpath("//tr[4]//span/text()")[0].extract()
        single['company_final_shareholder'] = "".join(company_final_shareholder).strip()
        company_content2_1.append(single)
        # print("子页面，打印这个字典=="+str(single))
        company_detail['company_content2_1'] = company_content2_1

        print("=====准备打印详细情况中的第二部分信息中的第二部分====")
        company_content2_2 = list()
        single1 = dict()
        company_chairman = company_comments.xpath("//tr[5]//table[@class='m_table ggintro']//h3/text()")[0].extract()
        single1['company_chairman'] = "".join(company_chairman).strip()
        company_DongMi = company_comments.xpath("//tr[5]//table[@class='m_table ggintro']//h3/text()")[1].extract()
        single1['company_DongMi'] = "".join(company_DongMi).strip()
        company_legal_person = company_comments.xpath("//tr[5]//table[@class='m_table ggintro']//h3/text()")[2].extract()
        single1['company_legal_person'] = "".join(company_legal_person).strip()

        company_general_manager = company_comments.xpath("//tr[6]//table[@class='m_table ggintro']//h3/text()").getall()
        single1['company_general_manager'] = "".join(company_general_manager).strip()
        company_registered_capital = company_comments.xpath("//tr[6]/td/span/text()")[3].getall()
        single1['company_registered_capital'] = "".join(company_registered_capital).strip()
        company_num_of_worker = company_comments.xpath("//tr[6]/td/span/text()")[4].getall()
        single1['company_num_of_worker'] = "".join(company_num_of_worker).strip()

        company_tel = company_comments.xpath("//tr[7]/td/span/text()")[0].getall()
        single1['company_tel'] = "".join(company_tel).strip()
        company_chuanzhen = company_comments.xpath("//tr[7]/td/span/text()")[1].getall()
        single1['company_chuanzhen'] = "".join(company_chuanzhen).strip()
        company_email = company_comments.xpath("//tr[7]/td/span/text()")[2].getall()
        single1['company_email'] = "".join(company_email).strip()
        company_content2_2.append(single1)
        company_detail['company_content2_2'] = company_content2_2

        print("=====准备详细情况中的第三部分信息====")
        company_introduction = company_comments.xpath("//tr[9]//p[@class='tip lh24']/text()").getall()
        company_introduction = "".join(company_introduction).strip()
        company_detail['company_introduction'] = company_introduction

        print("=====详细情况准备完毕，休息一下嘻嘻====")
        time.sleep(random.randint(2, 5))
        yield company_detail





