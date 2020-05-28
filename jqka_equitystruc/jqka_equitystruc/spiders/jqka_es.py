# -*- coding: utf-8 -*-
import requests
import scrapy
from jqka_equitystruc.items import JqkaEquitystrucItem
from lxml import etree
from scrapy import item
from scrapy.http import Request
# 获取excel需要引入的包
from openpyxl import load_workbook
from selenium import webdriver
import time
import scrapy
import pandas as pd


class JqkaEsSpider(scrapy.Spider):
    name = 'jqka_es'
    allowed_domains = ['http://basic.10jqka.com.cn/603221/holder.html']
    start_urls = ['http://http://basic.10jqka.com.cn/603221/holder.html/']

    # start_urls = ['http://basic.10jqka.com.cn/603221/operate.html/']

    def start_requests(self):
        yield Request("http://basic.10jqka.com.cn/603221/holder.html", headers={
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"})

    def parse(self, response):
        book = load_workbook(filename=r"C:\python\lnuSpider\data\exel\com_list.xlsx")
        sheet = book.active
        data = []
        data1 = []
        data2 = []
        data3 = []
        row_num = 1
        while row_num <= 1:
            # 将表中第一列的1-100行数据写入data数组中
            data.append(sheet.cell(row=row_num, column=3).value)
            data1.append(sheet.cell(row=row_num, column=1).value)
            data3.append(sheet.cell(row=row_num, column=2).value)
            data2.append(row_num)
            row_num = row_num + 1
        for i in data2:
            # url = 'http://basic.10jqka.com.cn/'+data[i]+'/company.html'
            # print(data[i-1])
            listedCompany_url = 'http://basic.10jqka.com.cn/' + data[i - 1] + '/holder.html'
            company_es= JqkaEquitystrucItem()
            company_es['listedCompany_url'] = listedCompany_url
            listedCompany_id = data1[i - 1]
            company_es['listedCompany_id'] = listedCompany_id
            listedCompany_name = data3[i - 1]
            company_es['listedCompany_name'] = listedCompany_name
            # print(listedCompany_id)
            # pandas读取表格
            # res_elements = etree.HTML(response.text)
            # table = res_elements.xpath("//table[@class='tbody']")
            # table = etree.tostring(table[0], encoding='utf-8').decode()
            # df = pd.read_html(table, encoding='utf-8', header=0)
            # results = list(df.T.to_dict().values())  # 转换成列表嵌套字典的格式
            # print(results)
            yield scrapy.Request(company_es['listedCompany_url'],
                                 meta={'company_es': company_es}, callback=self.detail_ni, dont_filter=True)
        return

    def detail_ni(self, response):
        company_es = response.meta['company_es']
        root = response.xpath(".//div[@id='gdrsTable'][@class='holernumcomp gdrs_table']//div[@class='table_data']")
        root = response.xpath("//div[@class='content page_event_content']//div[@id='gdrsTable'][@class='holernumcomp gdrs_table']")
        print(root)
        root1 = root.xpath("./div[@class='scroll_container']/div[@class='table_data']/div[@class='data_tbody']")
        time1 = root1.xpath("./table[@class='top_thead']/tr[1]/th[1]/div/text()").getall()
        print(time1)
        time12 = root1.xpath("./table[@class='tbody']/tr[1]/td[1]/div/text()").getall()
        print(time12)
        time123 = root1.xpath("./table[@class='tbody']/tr[2]/td[1]/span/text()").getall()
        print(time123)
        time124 = root1.xpath("./table[@class='tbody']/tr[3]/td[1]/text()").getall()
        print(time124)
        time125 = root1.xpath("./table[@class='tbody']/tr[4]/td[1]/span/text()").getall()
        print(time125)
        time121 = root1.xpath("./table[@class='tbody']/tr[5]/td[1]//text()").getall()
        print(time121)

        # pandas读取表格
        res_elements = etree.HTML(response.text)
        table = res_elements.xpath("//table[@class='m_table m_hl ggintro']")
        table = etree.tostring(table[2], encoding='utf-8').decode()
        df = pd.read_html(table, encoding='utf-8', header=0)[0]
        results = list(df.T.to_dict().values())  # 转换成列表嵌套字典的格式
        print(results)

        yield company_es