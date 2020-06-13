# -*- coding: utf-8 -*-
import scrapy
from jqka_svzl.items import JqkaSvzlItem
from scrapy.http import Request
from openpyxl import load_workbook
import time
import random
from selenium import webdriver


class JqkaSvzlSpiderSpider(scrapy.Spider):
    name = 'jqka_svzl_spider'
    allowed_domains = ['http://basic.10jqka.com.cn/603290/position.html']

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
            listedCompany_url = 'http://basic.10jqka.com.cn/' + data[i - 1] + '/position.html'
            company_svzl= JqkaSvzlItem()
            company_svzl['listedCompany_url'] = listedCompany_url
            listedCompany_id = data1[i - 1]
            company_svzl['listedCompany_id'] = listedCompany_id
            listedCompany_name = data3[i - 1]
            company_svzl['listedCompany_name'] = listedCompany_name
            yield scrapy.Request(company_svzl['listedCompany_url'],
                                 meta={'company_svzl': company_svzl}, callback=self.detail_ni, dont_filter=True)
        return

    def detail_ni(self, response):

        company_svzl = response.meta['company_svzl']

        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")  # 设置火狐为headless无界面模式
        options.add_argument("--disable-gpu")

        driver_path = r"D:\project\geckodriver.exe"
        driver = webdriver.Firefox(executable_path=driver_path, firefox_options=options)
        driver.get(company_svzl['listedCompany_url'])


        # c = driver.find_element_by_xpath("//div[@class='m_dlbox'][@id='pull_all']")
        # print(c.get_attribute('innerHTML'))
        # root1 = driver.find_elements_by_xpath("//div[@id='ipoallot']//table/tbody/tr")
        # table = driver.find_elements_by_css_selector("[class='m_table m_hl']")[1]
        root1 = driver.find_element_by_xpath("//div[@id='ipoallot']//table[@class='m_table m_hl']/tbody")
        rows = root1.find_elements_by_tag_name("tr")
        # tr_label_s = root1.find_element_by_xpath("./tbody/tr")
        # print(tr_label_s.text)
        # print(root1.text)
        rowname = []
        i = 1
        while i<10:
            # news_date = root2.find_element_by_xpath("./th")
            # print(news_date.text)
            col = rows[i].text
            rowname.append(col)
            i = i + 1
        print(rowname)

        yield company_svzl


