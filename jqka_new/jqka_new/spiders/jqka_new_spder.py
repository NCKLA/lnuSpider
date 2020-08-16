# -*- coding: utf-8 -*-
import random
import time
from jqka_new.items import JqkaNewItem
from scrapy.http import Request
# 获取excel需要引入的包
from openpyxl import load_workbook
from selenium import webdriver
import scrapy
from selenium.webdriver.chrome.options import Options

class JqkaNewSpderSpider(scrapy.Spider):
    name = 'jqka_new_spder'
    allowed_domains = ['http://basic.10jqka.com.cn/000056/news.html']
    start_urls = ['http://http://basic.10jqka.com.cn/000056/news.html/']

    def __init__(self):
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")  # 设置火狐为headless无界面模式
        options.add_argument("--disable-gpu")
        self.driver_path = r"D:\project\geckodriver.exe"
        self.driver = webdriver.Firefox(executable_path=self.driver_path, firefox_options=options)

    def start_requests(self):
        yield Request("http://basic.10jqka.com.cn/603221/news.html",
                      headers={
                          'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"})


    def parse(self, response):
        book = load_workbook(filename=r"C:\python\lnuSpider\data\exel\com_list.xlsx")
        sheet = book.active
        data = []
        data1 = []
        data2 = []
        data3 = []
        data4 = []
        row_num = 1
        while row_num <= 3815:
            # 将表中第一列的1-100行数据写入data数组中
            data.append(sheet.cell(row=row_num, column=3).value)
            data1.append(sheet.cell(row=row_num, column=1).value)
            data3.append(sheet.cell(row=row_num, column=2).value)
            data4.append(sheet.cell(row=row_num, column=4).value)
            data2.append(row_num)
            row_num = row_num + 1
        for i in data2:
            # url = 'http://basic.10jqka.com.cn/'+data[i]+'/company.html'
            # print(data[i-1])
            a = str(data[i - 1])
            listedCompany_url = 'http://basic.10jqka.com.cn/' + a + '/news.html'
            company_news = JqkaNewItem()
            company_news['listedCompany_url'] = listedCompany_url
            listedCompany_id = data1[i - 1]
            company_news['listedCompany_id'] = listedCompany_id
            listedCompany_name = data3[i - 1]
            company_news['listedCompany_name'] = listedCompany_name
            listedCompany_fullName = data4[i - 1]
            company_news['listedCompany_fullName'] = listedCompany_fullName
            # print(listedCompany_id)
            yield scrapy.Request(company_news['listedCompany_url'],meta={'company_news': company_news}, callback=self.detail_ni, dont_filter=True)


    def detail_ni(self, response):
        company_news = response.meta['company_news']

        self.driver.get(company_news['listedCompany_url'])
        time.sleep(1)

        # 公告列表模块
        company_news['listedCompany_news_announceList'] = list()
        while True:
            root1 = self.driver.find_elements_by_xpath("//div[@class='m_dlbox'][@id='pull_all']//dl")
            for root2 in root1:
                news_dict = dict()
                # 1.日期
                news_date = root2.find_element_by_xpath("./dt/span[@class='date']")
                news_date = news_date.text
                # 2.标签
                news_tag = root2.find_element_by_xpath("./dt/span[@class='title']/a/strong")
                news_tag = news_tag.text
                # 封装字典
                news_dict['listedCompany_news_announceList_tag'] = news_tag
                news_dict['listedCompany_news_announceList_date'] = news_date
                # 将字典加入列表
                company_news['listedCompany_news_announceList'].append(news_dict)

            # 下一页按钮 对象
            next_ele = self.driver.find_element_by_xpath("//div[@id='pub']//div[@class='splpager clearfix light-theme simple-pagination']//li[last()]")
            print(next_ele.get_attribute("class")+"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            # 是最后一页 则跳出循环
            if next_ele.get_attribute("class") == "disabled":
                # 该结束了
                break
            # 不是最后一页 则翻页
            else:
                print("翻页")
                next_ele.click()
                time.sleep(1)

        yield company_news