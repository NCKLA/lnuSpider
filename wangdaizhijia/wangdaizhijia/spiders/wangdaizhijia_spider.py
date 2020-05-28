# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from wangdaizhijia.items import WangdaizhijiaItem
import time
import json
'''
项目难点：
1.如何解决网贷之家的动态翻页问题，点评数据很多，整个页面只有两个按钮，
上一页和下一页，下一页可以一直点，直到最后一页，上一页也可以一直点
直到第一页，需要在爬虫中添加点击的动作。来完成翻页的功能,主要难点

2.是数据的提取，虽说每条评论涉及的数据都在ul标签中，但是每一个ul标签
下的结构也是过于复杂，所以如何在复杂的网页结构下，提取所需要的数据也
是一个小难点

3.数据的存储：如何存储数据呢

4.项目写好后网络原因可能会导致爬虫的断断续续。
'''
class WangdaizhijiaSpiderSpider(scrapy.Spider):

    #声明爬虫的名字
    name = 'wangdaizhijia_spider'
    #允许爬取的域名
    allowed_domains = ['wdzj.com']
    #爬虫的起始网址
    start_urls = ['https://www.wdzj.com/dangan/dianping/']
    #定义一个变量用于拼接网贷公司的网址
    url = 'https://www.wdzj.com/'

    def __init__(self):
        #获取浏览器驱动的配置信息。
        options = webdriver.FirefoxOptions()
        #修改添加驱动信息
        options.add_argument("--headless")#设置火狐为无界面模式
        options.add_argument("--disable-gpu")#设置不使用gpu
        #设置驱动的路径
        driver_path = r"D:\huohuqudong\geckodriver-v0.24.0-win64\geckodriver.exe"
        self.driver = webdriver.Firefox(executable_path=driver_path,firefox_options=options)
    def parse(self, response):
        #写一个循环需要进行循环翻页操作
        self.driver.get("https://www.wdzj.com/dangan/dianping/")
        item = WangdaizhijiaItem()
        for i in range(0,6000):
            data = self.driver.page_source
            #print(data)#这个data是两个不同网页的源代码
            #翻页是可以翻页的，但是拿到的数据都是同一页的
            comment_uls = self.driver.find_elements_by_xpath("//div[@class='bd'][@id='reviewList']//ul")
            # comment_uls.__getattribute__('innerHTML')
            # print(comment_uls.text)
            # print(type(comment_uls))
            # print(uls)
            # print(type(uls)) #可以正常获取到每个ul标签
            #遍历ul标签提取数据
            # print(len(uls))
            for comment_ul in comment_uls:
                #1.获取评论的作者
                author = comment_ul.find_element_by_xpath(".//div[@class='nameTit']/span/a").text
                #print(author)   #经测试可以获取到作者。

                #2.获取评论的时间
                comment_time = comment_ul.find_element_by_xpath(".//div[@class='nameTit']//span[@class='date']").text
                # print(comment_time)   #经测试时间可以获取

                #3。获取被点评的网贷平台
                wangdai_company = comment_ul.find_element_by_xpath(".//div[@class='nameTit']//span[@class='bold']/a").text
                #print(wangdai_company)  #经测试被点评的企业可以正常获取到

                #4.获取被点评的网贷平台的档案网址
                wangdai_company_url = comment_ul.find_element_by_xpath(".//div[@class='nameTit']//span[@class='bold']/a")
                wangdai_company_url_text = wangdai_company_url.get_attribute("href")
                #print(wangdai_company_url_text) #经测试被点评的公司的网址可以正常获取到

                #5.获取是否推荐当前网贷平台的标签
                tuijian = comment_ul.find_element_by_xpath(".//div[@class='nameTit']//span[@class='tags']").text
                #print(tuijian)  #经测试可以获取到是否推荐的标签

                #6.获取印象数据
                impressions = comment_ul.find_element_by_xpath(".//dl[@class='impression']").text
                # print(impressions) #可以获取

                #7.获取评论的内容
                comment = comment_ul.find_element_by_xpath(".//div[@class='comBg']//div[@class='commentFont']//p[@class='font']").text
                # print(content)  #可以获取

                #8.获取评论的所有回复内容
                comment_recovers = comment_ul.find_elements_by_xpath(".//div[@class='myComList']//dd[@class='font']")
                #print(content_recovers)#可以获取

                for comment_recover in comment_recovers:
                    if comment_recover:
                        comment_recover = comment_recover.text
                        #print(content_recover)  可以获取到评论的回复数据
                        item['comment_recover'] = comment_recover

                #9.获取所有的体验数据
                dds = comment_ul.find_elements_by_xpath(".//dl[@class='comment']//dd")
                feelings = []

                #创建列表存储
                for dd in dds:
                    data1 = dd.find_element_by_xpath(".//strong").text
                    #print(data1)
                    feelings.append(data1)

                    num = dd.find_element_by_xpath(".//span[@class='num']").text
                    #print(num)
                    feelings.append(num)

                    data2 = dd.find_element_by_xpath(".//span[@class='gray']").text
                    #print(data2)
                    feelings.append(data2)

                # print(feelings)

                # 写入item并返回
                item['author'] = author

                item['comment_time'] = comment_time

                item['wangdai_company'] = wangdai_company

                item['wangdai_company_url_text'] = wangdai_company_url_text

                item['tuijian'] = tuijian

                item['impressions'] = impressions

                item['feelings'] = feelings

                item['comment'] = comment
                yield item

            self.driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[2]/div/div[3]/ul/li[2]").click();
            time.sleep(5)



