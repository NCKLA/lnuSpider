# -*- coding: utf-8 -*-
import random

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
        while row_num <= 3815:
            # 将表中第一列的1-100行数据写入data数组中
            data.append(sheet.cell(row=row_num, column=3).value)
            data1.append(sheet.cell(row=row_num, column=1).value)
            data3.append(sheet.cell(row=row_num, column=2).value)
            data2.append(row_num)
            row_num = row_num + 1
        for i in data2:
            # url = 'http://basic.10jqka.com.cn/'+data[i]+'/company.html'
            # print(data[i-1])
            a = str(data[i - 1])
            listedCompany_url = 'http://basic.10jqka.com.cn/' + a + '/holder.html'
            company_es = JqkaEquitystrucItem()
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
            yield scrapy.Request(company_es['listedCompany_url'],meta={'company_es': company_es}, callback=self.detail_ni, dont_filter=True)

    def detail_ni(self, response):
        company_es = response.meta['company_es']
        # root = response.xpath(".//div[@id='gdrsTable'][@class='holernumcomp gdrs_table']//div[@class='table_data']")
        item = response.xpath("//div[@id='bd_0']/div[1]/ul/li")
        # print(item)
        listedCompany_shareholderResearch_topTenShareholders = list()
        list1 = list()
        # print(len(itm))
        for x in range(len(item)):
            list0 = list()
            x = x + 1
            print(x)
            root2 = response.xpath("//div[@id='bd_0']/div[{}]/table".format(x+1))
            root3 = root2.xpath("./tbody/tr")
            for rot3 in root3:
                single=dict()

                listedCompany_shareholderResearch_topTenShareholders_shareholderName = rot3.xpath("./th/a/text()").getall()
                listedCompany_shareholderResearch_topTenShareholders_shareholderName = ''.join(listedCompany_shareholderResearch_topTenShareholders_shareholderName).strip()
                single['listedCompany_shareholderResearch_topTenShareholders_shareholderName'] = listedCompany_shareholderResearch_topTenShareholders_shareholderName

                listedCompany_shareholderResearch_topTenShareholders_shareType = rot3.xpath("./td[5]/text()").getall()
                listedCompany_shareholderResearch_topTenShareholders_shareType = ''.join(
                    listedCompany_shareholderResearch_topTenShareholders_shareType).strip()
                single['listedCompany_shareholderResearch_topTenShareholders_shareType'] = listedCompany_shareholderResearch_topTenShareholders_shareType

                listedCompany_shareholderResearch_topTenShareholders_sharesHoldNumber = rot3.xpath("./td[1]/text()").getall()
                listedCompany_shareholderResearch_topTenShareholders_sharesHoldNumber = ''.join(
                    listedCompany_shareholderResearch_topTenShareholders_sharesHoldNumber).strip()
                single['listedCompany_shareholderResearch_topTenShareholders_sharesHoldNumber'] = listedCompany_shareholderResearch_topTenShareholders_sharesHoldNumber

                listedCompany_shareholderResearch_topTenShareholders_shareHoldingChange = rot3.xpath("./td[2]/text()").getall()
                listedCompany_shareholderResearch_topTenShareholders_shareHoldingChange = ''.join(
                    listedCompany_shareholderResearch_topTenShareholders_shareHoldingChange).strip()
                single['listedCompany_shareholderResearch_topTenShareholders_shareHoldingChange'] = listedCompany_shareholderResearch_topTenShareholders_shareHoldingChange

                listedCompany_shareholderResearch_topTenShareholders_totalEquityProportion = rot3.xpath("./td[3]/text()").getall()
                listedCompany_shareholderResearch_topTenShareholders_totalEquityProportion = ''.join(
                    listedCompany_shareholderResearch_topTenShareholders_totalEquityProportion).strip()
                single['listedCompany_shareholderResearch_topTenShareholders_totalEquityProportion'] = listedCompany_shareholderResearch_topTenShareholders_totalEquityProportion

                listedCompany_shareholderResearch_topTenShareholders_increaseOrDecrease = rot3.xpath("./td[4]/text()").getall()
                listedCompany_shareholderResearch_topTenShareholders_increaseOrDecrease = ''.join(
                    listedCompany_shareholderResearch_topTenShareholders_increaseOrDecrease).strip()
                single['listedCompany_shareholderResearch_topTenShareholders_increaseOrDecrease'] = listedCompany_shareholderResearch_topTenShareholders_increaseOrDecrease
                list0.append(single)
            list1.append(list0)
        listedCompany_shareholderResearch_topTenShareholders.append(list1)
        company_es['listedCompany_shareholderResearch_topTenShareholders'] = listedCompany_shareholderResearch_topTenShareholders



        # 股东人数 模块(按列存储)
        company_es['listedCompany_shareholderResearch_shareholderNum'] = list()
        # 日期列表，日期列表长度==列数
        date_list = response.xpath("//table[@class='top_thead']//div/text()").getall()
        base_table = response.xpath("//div[@class='data_tbody']/table[@class='tbody']")
        for i in range(0, len(date_list)):
            # 按td(列)拼凑字典对象
            td_dict = dict()
            # 日期直接通过日期列表取
            td_dict['listedCompany_shareholderResearch_shareholderNum_time'] = date_list[i].strip()
            # 其余字段需要再通过xpath取值
            # 股东总人数 字段需要判断
            if base_table.xpath(".//tr[1]/td[{}]/div".format(i+1)):
                td_dict['listedCompany_shareholderResearch_shareholderNum_totalShareholdersNumber'] = base_table.xpath(".//tr[1]/td[{}]/div/text()".format(i+1)).get().strip()
            else:
                td_dict['listedCompany_shareholderResearch_shareholderNum_totalShareholdersNumber'] = base_table.xpath(".//tr[1]/td[{}]/text()".format(i+1)).get().strip()
            # 较上期变化 字段需要判断
            if base_table.xpath(".//tr[2]/td[{}]/span".format(i+1)):
                td_dict['listedCompany_shareholderResearch_shareholderNum_comparedPreviousPeriodChange'] = base_table.xpath(".//tr[2]/td[{}]/span/text()".format(i+1)).get().strip()
            else:
                td_dict['listedCompany_shareholderResearch_shareholderNum_comparedPreviousPeriodChange'] = base_table.xpath(".//tr[2]/td[{}]/text()".format(i+1)).get().strip()
            # 行业平均 字段
            td_dict['listedCompany_shareholderResearch_shareholderNum_industryAverage'] = base_table.xpath(".//tr[3]/td[{}]/text()".format(i+1)).get().strip()
            # 人均流通股 字段
            td_dict['listedCompany_shareholderResearch_shareholderNum_perCapitaCirculatingShares'] = base_table.xpath(".//tr[4]/td[{}]/text()".format(i+1)).get().strip()
            # 人均流通变化 字段需要判断
            if base_table.xpath(".//tr[5]/td[{}]/span".format(i+1)):
                td_dict['listedCompany_shareholderResearch_shareholderNum_perCapitaCirculationChanges'] = base_table.xpath(".//tr[5]/td[{}]/span/text()".format(i+1)).get().strip()
            else:
                td_dict['listedCompany_shareholderResearch_shareholderNum_perCapitaCirculationChanges'] = base_table.xpath(".//tr[5]/td[{}]/text()".format(i+1)).get().strip()
            # 将字典对象加入列表
            company_es['listedCompany_shareholderResearch_shareholderNum'].append(td_dict)


        root_1 = response.xpath(
            "//div[@class='content page_event_content']//div[@id='flowholder'][@class='m_box hold_detail z100 gssj_scroll gssj_scroll1']")
        root_11 = root_1.xpath("//div[@id='bd_1']/div[@class='m_tab mt15']/ul/li")
        listedCompany_shareholderResearch_topTenCurrentShareholders_time = list()
        for root_111 in root_11:
            listedCompany_shareholderResearch_topTenCurrentShareholders_tim = root_111.xpath("./a/text()").getall()
            listedCompany_shareholderResearch_topTenCurrentShareholders_tim = ''.join(listedCompany_shareholderResearch_topTenCurrentShareholders_tim).strip()
            listedCompany_shareholderResearch_topTenCurrentShareholders_time.append(listedCompany_shareholderResearch_topTenCurrentShareholders_tim)
        company_es['listedCompany_shareholderResearch_topTenCurrentShareholders_time'] = listedCompany_shareholderResearch_topTenCurrentShareholders_time

        listedCompany_shareholderResearch_topTenCurrentShareholders = list()
        root_12 = root_1.xpath("//div[@id='bd_1']/div[@class='m_tab_content2 clearfix']/table/tbody[1]/tr")
        for root_121 in root_12:
            single5 = dict()
            content_5 = root_121.xpath("./th/a/text()").getall()
            single5['listedCompany_shareholderResearch_topTenCurrentShareholders_shareholderName'] = "".join(content_5).strip()
            content_6 = root_121.xpath("./td[1]/text()").getall()
            single5['listedCompany_shareholderResearch_topTenCurrentShareholders_sharesHoldNumber'] = "".join(content_6).strip()
            content_7 = root_121.xpath("./td[2]/span/text()").getall()
            single5['listedCompany_shareholderResearch_topTenCurrentShareholders_shareHoldChange'] = "".join(content_7).strip()
            content_8 = root_121.xpath("./td[3]/text()").getall()
            single5['listedCompany_shareholderResearch_topTenCurrentShareholders_totalEquityProportion'] = "".join(content_8).strip()
            content_9 = root_121.xpath("./td[5]/text()").getall()
            single5['listedCompany_shareholderResearch_topTenCurrentShareholders_shareType'] = "".join(content_9).strip()
            listedCompany_shareholderResearch_topTenCurrentShareholders.append(single5)
        company_es['listedCompany_shareholderResearch_topTenCurrentShareholders'] = listedCompany_shareholderResearch_topTenCurrentShareholders

        listedCompany_shareholderResearch_topTenCurrentShareholders_increaseOrDecrease = root_1.xpath(
            "//div[@id='bd_1']/div[@class='m_tab_content2 clearfix']/table/caption//text()").getall()
        listedCompany_shareholderResearch_topTenCurrentShareholders_increaseOrDecrease = "".join(
            listedCompany_shareholderResearch_topTenCurrentShareholders_increaseOrDecrease).strip().replace('\t', '')
        company_es[
            'listedCompany_shareholderResearch_topTenCurrentShareholders_increaseOrDecrease'] = listedCompany_shareholderResearch_topTenCurrentShareholders_increaseOrDecrease

        # # pandas读取表格
        # res_elements = etree.HTML(response.text)
        # table = res_elements.xpath("//table[@class='m_table m_hl ggintro']")
        # table = etree.tostring(table[2], encoding='utf-8').decode()
        # df = pd.read_html(table, encoding='utf-8', header=0)[0]
        # results = list(df.T.to_dict().values())  # 转换成列表嵌套字典的格式
        # print(results)
        time.sleep(random.randint(3, 6))
        yield company_es
