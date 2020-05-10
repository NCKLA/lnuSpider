# -*- coding: utf-8 -*-
import random
import re

from jqka_com_detail.items import JqkaComDetailItem
from scrapy import item
from scrapy.http import Request
# 获取excel需要引入的包
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
        yield Request("http://basic.10jqka.com.cn/603221/company.html", headers={
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"})

    def parse(self, response):
        # 读取excel表格
        book = load_workbook(filename=r"C:\python\lnuSpider\data\exel\com_list.xlsx")
        sheet = book.active
        data = []
        data1 = []
        data2 = []
        row_num = 1
        while row_num <= 3:
            # 将表中第一列的1-100行数据写入data数组中
            data.append(sheet.cell(row=row_num, column=3).value)
            data1.append(sheet.cell(row=row_num, column=1).value)
            data2.append(row_num)
            row_num = row_num + 1
        for i in data2:
            # url = 'http://basic.10jqka.com.cn/'+data[i]+'/company.html'
            # print(data[i-1])
            listedCompany_url = 'http://basic.10jqka.com.cn/' + data[i - 1] + '/company.html'
            company_detail = JqkaComDetailItem()
            company_detail['listedCompany_url'] = listedCompany_url
            listedCompany_id = data1[i - 1]
            company_detail['listedCompany_id'] = listedCompany_id
            # print(listedCompany_id)
            yield scrapy.Request(company_detail['listedCompany_url'],
                                 meta={'company_detail': company_detail}, callback=self.detail_ni, dont_filter=True)
        return

    def detail_ni(self, response):
        print("=====准备详细情况中的第一部分信息====")
        company_detail = response.meta['company_detail']
        root = response.xpath("//div[@class='content page_event_content']")[0]
        # print(root)
        company_detail['listedCompany_enterpriseIntro_companyFullName'] = root.xpath("//div[@stat][@id='detail']//table[@class='m_table']//tr[1]//td[2]//span/text()")[0].extract()

        listedCompany_enterpriseIntro_region = root.xpath("//div[@stat][@id='detail']//table[@class='m_table']//tr[1]//td[3]//span/text()")[0].extract()
        company_detail['listedCompany_enterpriseIntro_region'] = listedCompany_enterpriseIntro_region

        listedCompany_enterpriseIntro_englishName = root.xpath("//div[@stat][@id='detail']//table[@class='m_table']//tr[2]""//td[1]//span/text()")[0].extract()

        company_detail['listedCompany_enterpriseIntro_englishName'] = "".join(
            listedCompany_enterpriseIntro_englishName).strip().replace(' ', '')

        listedCompany_enterpriseIntro_industry = root.xpath("//div[@stat][@id='detail']//table[@class='m_table']//tr[2]//td[2]//span/text()")[0].extract()

        company_detail['listedCompany_enterpriseIntro_industry'] = listedCompany_enterpriseIntro_industry

        listedCompany_enterpriseIntro_formerlyUsedName = root.xpath("//div[@stat][@id='detail']//table[@class='m_table']//tr[3]//td[1]//span/text()")[0].extract()

        company_detail['listedCompany_enterpriseIntro_formerlyUsedName'] = listedCompany_enterpriseIntro_formerlyUsedName

        listedCompany_enterpriseIntro_websiteAddress = root.xpath("//div[@stat][@id='detail']//table[@class='m_table']//tr[3]//td[2]//span/a/text()")[0].extract()

        company_detail['listedCompany_enterpriseIntro_websiteAddress'] = listedCompany_enterpriseIntro_websiteAddress

        print("=====准备详细情况中的第二部分信息中的第一部分====")
        company_content2_1 = list()
        company_comments = response.xpath("//div[@stat][@id='detail']//div[@class='m_tab_content2']")[0]
        # print(response.text)
        # print(company_comments)
        single = dict()
        # 主营业务
        listedCompany_enterpriseIntro_mainBusiness = company_comments.xpath("//tr[1]/td[1]//span/text()").get()
        # print(company_main_business)
        single['listedCompany_enterpriseIntro_mainBusiness'] \
            = listedCompany_enterpriseIntro_mainBusiness.strip()
        # 产品名称
        listedCompany_enterpriseIntro_productName = company_comments.xpath("//tr[@class='product_name']//span/span/text()")[0].extract()

        listedCompany_enterpriseIntro_productName = "". \
            join(listedCompany_enterpriseIntro_productName).strip().replace(' ', '')
        # 去除字符串中存在的所有空格，调用re包

        listedCompany_enterpriseIntro_productName = \
            re.sub('\s+', '', listedCompany_enterpriseIntro_productName).strip()
        # print(company_product_name)
        single['listedCompany_enterpriseIntro_productName'] = listedCompany_enterpriseIntro_productName.strip()

        # 控股股东
        listedCompany_enterpriseIntro_controllingShareholders = company_comments.xpath("//div[@class='tipbox_wrap mr10']//span/text()")[0].extract()

        single['listedCompany_enterpriseIntro_controllingShareholders'] = \
            "".join(listedCompany_enterpriseIntro_controllingShareholders).strip()
        # 实际控制人
        listedCompany_enterpriseIntro_actualController = company_comments.xpath("//tr[3]//span/text()")[3].getall()
        single['listedCompany_enterpriseIntro_actualController'] = \
            "".join(listedCompany_enterpriseIntro_actualController).strip()

        # 最终控制人
        listedCompany_enterpriseIntro_ultimateController = company_comments.xpath("//tr[4]//span/text()")[0].extract()
        single['listedCompany_enterpriseIntro_ultimateController'] = \
            "".join(listedCompany_enterpriseIntro_ultimateController).strip()

        company_content2_1.append(single)

        # print("子页面，打印这个字典=="+str(single))
        company_detail['company_content2_1'] = company_content2_1

        print("=====准备打印详细情况中的第二部分信息中的第二部分====")
        company_content2_2 = list()
        single1 = dict()

        listedCompany_enterpriseIntro_chairman = company_comments.xpath("//tr[5]//table[@class='m_table ggintro']//h3/text()")[0].extract()

        single1['listedCompany_enterpriseIntro_chairman'] = "".join(listedCompany_enterpriseIntro_chairman).strip()

        listedCompany_enterpriseIntro_chairmanSecretary = company_comments.xpath("//tr[5]//table[@class='m_table ggintro']//h3/text()")[1].extract()
        single1['listedCompany_enterpriseIntro_chairmanSecretary'] = "".join(listedCompany_enterpriseIntro_chairmanSecretary).strip()
        listedCompany_enterpriseIntro_legalRepresentative = company_comments.xpath("//tr[5]//table[@class='m_table ggintro']//h3/text()")[
            2].extract()
        single1['listedCompany_enterpriseIntro_legalRepresentative'] = "".join(listedCompany_enterpriseIntro_legalRepresentative).strip()

        listedCompany_enterpriseIntro_generalManager = company_comments.xpath("//tr[6]//table[@class='m_table ggintro']//h3/text()").getall()
        single1['listedCompany_enterpriseIntro_generalManager'] = "".join(listedCompany_enterpriseIntro_generalManager).strip()

        listedCompany_enterpriseIntro_registeredCapital = company_comments.xpath("//tr[6]/td/span/text()")[3].getall()
        single1['listedCompany_enterpriseIntro_registeredCapital'] = "".join(listedCompany_enterpriseIntro_registeredCapital).strip()

        listedCompany_enterpriseIntro_staffNumbers = company_comments.xpath("//tr[6]/td/span/text()")[4].getall()
        single1['listedCompany_enterpriseIntro_staffNumbers'] = "".join(listedCompany_enterpriseIntro_staffNumbers).strip()

        listedCompany_enterpriseIntro_tel = company_comments.xpath("//tr[7]/td/span/text()")[0].getall()
        single1['listedCompany_enterpriseIntro_tel'] = "".join(listedCompany_enterpriseIntro_tel).strip()

        listedCompany_enterpriseIntro_fax = company_comments.xpath("//tr[7]/td/span/text()")[1].getall()
        single1['listedCompany_enterpriseIntro_fax'] = "".join(listedCompany_enterpriseIntro_fax).strip()

        listedCompany_enterpriseIntro_postalCode = company_comments.xpath("//tr[7]/td/span/text()")[2].getall()
        single1['listedCompany_enterpriseIntro_postalCode'] = "".join(listedCompany_enterpriseIntro_postalCode).strip()

        listedCompany_enterpriseIntro_businessAddress = company_comments.xpath("//tr[8]/td/span/text()").getall()
        single1['listedCompany_enterpriseIntro_businessAddress'] = "".join(listedCompany_enterpriseIntro_businessAddress).strip()
        company_content2_2.append(single1)
        company_detail['company_content2_2'] = company_content2_2

        print("=====准备详细情况中的第三部分信息====")
        listedCompany_enterpriseIntro_companyProfile = company_comments.xpath("//tr[9]//p[@class='tip lh24']/text()").getall()
        listedCompany_enterpriseIntro_companyProfile = "".join(listedCompany_enterpriseIntro_companyProfile).strip()
        company_detail['listedCompany_enterpriseIntro_companyProfile'] = listedCompany_enterpriseIntro_companyProfile

        print("=====详细情况准备完毕，休息一下嘻嘻====")
        time.sleep(random.randint(1, 3))
        yield company_detail
