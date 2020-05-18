# -*- coding: utf-8 -*-
import scrapy
from jqka_Business_analysis.items import JqkaBusinessAnalysisItem
from openpyxl import load_workbook
from scrapy import item
from scrapy.http import Request
# 获取excel需要引入的包
from openpyxl import load_workbook
from selenium import webdriver
import time
import scrapy


class JqkaBaSpider(scrapy.Spider):
    name = 'jqka_Ba'
    allowed_domains = ['basic.10jqka.com.cn/603221/operate.html']
    start_urls = ['http://basic.10jqka.com.cn/603221/operate.html/']

    def start_requests(self):
        yield Request("http://basic.10jqka.com.cn/603221/operate.html", headers={
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"})

    def parse(self, response):
        book = load_workbook(filename=r"C:\python\lnuSpider\data\exel\com_list.xlsx")
        sheet = book.active
        data = []
        data1 = []
        data2 = []
        data3 = []
        row_num = 1
        while row_num <= 3:
            # 将表中第一列的1-100行数据写入data数组中
            data.append(sheet.cell(row=row_num, column=3).value)
            data1.append(sheet.cell(row=row_num, column=1).value)
            data3.append(sheet.cell(row=row_num, column=2).value)
            data2.append(row_num)
            row_num = row_num + 1
        for i in data2:
            # url = 'http://basic.10jqka.com.cn/'+data[i]+'/company.html'
            # print(data[i-1])
            listedCompany_url = 'http://basic.10jqka.com.cn/' + data[i - 1] + '/operate.html'
            company_ba= JqkaBusinessAnalysisItem()
            company_ba['listedCompany_url'] = listedCompany_url
            listedCompany_id = data1[i - 1]
            company_ba['listedCompany_id'] = listedCompany_id
            listedCompany_name = data3[i - 1]
            company_ba['listedCompany_name'] = listedCompany_name
            # print(listedCompany_id)
            yield scrapy.Request(company_ba['listedCompany_url'],
                                 meta={'company_ba': company_ba}, callback=self.detail_ni, dont_filter=True)
        return

    def detail_ni(self, response):
        company_ba = response.meta['company_ba']
        yield company_ba