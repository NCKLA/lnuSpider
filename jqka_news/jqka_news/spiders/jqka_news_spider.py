# -*- coding: utf-8 -*-
import scrapy
from jqka_news.items import JqkaNewsItem
from scrapy import item
from scrapy.http import Request
# 获取excel需要引入的包
from openpyxl import load_workbook
from selenium import webdriver
from selenium import webdriver
import scrapy
import json
import requests
import ip_proxy


class JqkaNewsSpiderSpider(scrapy.Spider):
    def __init__(self):
        # self.driver = webdriver.PhantomJS(executable_path=r'C:\Users\10359\local\bin\phantomjs.exe')
        # self.driver.set_page_load_timeout(40)
        # self.driver = webdriver.PhantomJS(executable_path=r'C:\Users\G50\local\bin\phantomjs.exe')
        # # 设置timeout 不设置大概会像我一样卡死
        # self.driver.set_page_load_timeout(40)
        super().__init__()
        # self.min_page = 1
        # self.max_page = 100
        # self.list_page = range(self.min_page, self.max_page)
        self.json_obj = None
        self.domain = None
        self.port = None
        JqkaNewsSpiderSpider.new_port(self)

    def new_port(self):
        print("准备开始获取url的try")

        try:
            open_url = ip_proxy.get_open_url()

            # 向代理服务器发起请求，去拿端口号（ip地址是固定的好像）
            r = requests.get(open_url, timeout=5)
            result = str(r.content)
            if "b\'" in result:
                result = result[2:-1]
            print("result   " + result)
            # logging.info('open_url||' + result)
            # json_obj为响应json
            self.json_obj = json.loads(result)
            code = self.json_obj['code']
            self.domain = self.json_obj['domain']
            # 获得的端口号（如果状态码为100）
            if code == 100:
                self.port = str(self.json_obj['port'][0])
            elif code == 108:
                reset_url = ip_proxy.get_reset_url()
                r = requests.get(reset_url, timeout=5)
            else:
                print("异常的状态码：" + str(code))
            # 状态码说明
            # 100 成功
            # 101 认证不通过
            # 102 请求格式不正确
            # 103 IP暂时耗尽
            # 106 账号使用时间到期
            # 118 ip使用量已用完
        except Exception as e:
            print("申请端口，try出事儿了" + repr(e))
        print("try完了")
        print("打印domain和port   " + self.domain + ":" + self.port)

    def close_port(self, port):
        print("准备开始关闭端口的try")
        try:
            print("开始try  准备close")
            close_url = ip_proxy.get_close_url(port)
            r = requests.get(close_url, timeout=5)
            print("close result: " + str(r.content))
        except Exception as e:
            print("关闭端口，try出事了: " + repr(e))

    name = 'jqka_news_spider'
    allowed_domains = ['basic.10jqka.com.cn']
    start_urls = ['http://basic.10jqka.com.cn/603221/news.html']

    def start_requests(self):
        url = JqkaNewsSpiderSpider.start_urls[0]
        print(url)
        proxy = self.domain + ":" + str(self.port)
        proxies = ""
        if url.startswith("http://"):
            proxies = "http://" + str(proxy)
        elif url.startswith("https://"):
            proxies = "https://" + str(proxy)
        # 注意这里面的meta={'proxy':proxies},一定要是proxy进行携带,其它的不行,后面的proxies一定 要是字符串,其它任何形式都不行
        yield scrapy.Request(url, callback=self.parse, meta={'proxy': proxies})

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
            company_news = JqkaNewsItem()
            com_url = 'http://basic.10jqka.com.cn/%s' % i + '/news.html'
            company_news['url'] = com_url
            # print(response.text)
            yield scrapy.Request(company_news['url'],
                                 meta={'company_news': company_news}, callback=self.detail_ni, dont_filter=True)
        return

    def detail_ni(self, response):
        company_news = response.meta['company_news']
        root = response.xpath("//div[@class='content page_event_content']"
                              "/div[@class='m_box subnews'][@id='pub'][@stat='pub_pub']"
                              "/div[@class='bd']/div[@class='m_tab_content']/*").getall()
        # print(root)
        root1 = response.xpath("//div[@class='m_dlbox'][@id='pull_all']/dl")
        # print(type(root1))
        # print(root1)
        for root2 in root1:
            news_date = root2.xpath("./dt/span[@class='date']/text()").getall()
            news_tag = root2.xpath("./dt/span[@class='title']/a/strong/text()").getall()
            news_url = root2.xpath("./dt/span[@class='title']/a/@href").getall()
            # print(news_date)
            # print(news_tag)
            # print(news_url)
            company_news['news_url'] = "".join(news_url).strip()
            yield scrapy.Request(company_news['news_url'],
                                 meta={'company_news': company_news}, callback=self.detail_ni1, dont_filter=True)
        root3 = response.xpath("//div[@class='splpager clearfix light-theme simple-pagination']/*").getall()
        # options = webdriver.FirefoxOptions()
        # options.set_headless(True)
        # options.add_argument("--headless")  # 设置火狐为headless无界面模式
        # options.add_argument("--disable-gpu")
        # driver = webdriver.Firefox(firefox_options=options)
        # driver.get('http://basic.10jqka.com.cn/603221/news.html')
        # < a href=" " class="page-link next">下一页</ a>
        # element = driver.find_element_by_css_selector("[class='page-link next']")
        # print(element.text)
        # element.click()
        # list1 = driver.find_element_by_id("pull_all").find_elements_by_class_name("client")
        # print(type(list1))
        # for one_news in list1:
        #     ss = one_news.get_attribute("href")
        #     print(ss)
        # print(news)
        # driver.close()
        # print(root3)

        # yield company_news

    def detail_ni1(self, response):
        print("======进入内页======")
        company_news = response.meta['company_news']
        yield company_news

