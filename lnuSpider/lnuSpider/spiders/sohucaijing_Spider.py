# -*- coding: utf-8 -*-
import scrapy

from lnuSpider.items import LnuspiderItem
from selenium import webdriver


'''
主页面有20个新闻，每次页面拉到底会再产生20个新闻，是ajax请求。

'''


class SohucaijingSpiderSpider(scrapy.Spider):
    def __init__(self):
        self.driver = webdriver.PhantomJS(executable_path=r'C:\Users\G50\local\bin\phantomjs.exe')
        # 设置timeout 不设置大概会像我一样卡死
        self.driver.set_page_load_timeout(40)
        # self.driver = webdriver.PhantomJS(executable_path=r'e:\phantomjs-2.1.1-windows\
        # phantomjs-2.1.1-windows\bin\phantomjs.exe')

    name = 'sohucaijing_Spider'
    allowed_domains = ['mp.sohu.com/profile?xpt=c29odWNqeWMyMDE3QHNvaHUuY29t&_'
                       'f=index_pagemp_1&spm=smpc.ch15.top-subnav.8.1585379351817DgmoPb1',
                       'www.sohu.com/',
                       '5b0988e595225.cdn.sohucs.com/images']
    start_urls = ['http://mp.sohu.com/profile?xpt=c29odWNqeWMyMDE3QHNvaHUuY29t&_'
                  'f=index_pagemp_1&spm=smpc.ch15.top-subnav.8.1585379351817DgmoPb1/']

    # 需求内容： 标题 正文  日期  原链接  标签  类别暂时没有  评论 图片
    def parse(self, response):

        # infos = response.xpath("//ul[@class='feed-list-area feed-normal-list-area']/li")
        infos = response.xpath("//li[@class='feed-item']")

        for info in infos:
            item = LnuspiderItem()
            # title = info.xpath(".//h4[@class='feed-title']/a//text()").get().strip()

            url = info.xpath(".//h4/a/@href").get()
            # 获取到的是'//www.sohu.com/a/383791237_100001551'  但是getall获取的是个list

            # jianjie = info.xpath(".//p//text()").get().strip()

            tags = info.xpath(".//article/div/div/span/a//text()").getall()

            item['url'] = "https:"+url
            # item['url'] = url

            item['tags'] = tags

            # print("=====准备进入子页面=====")
            print("spider：parse方法发起的请求链接："+item['url'])
            yield scrapy.Request(item['url'], meta={'item': item}, callback=self.detail_parse, dont_filter=True)
        return

    def detail_parse(self, response):
        print("=====进入子页面成功=====")
        item = response.meta['item']
        # item['images_src'] = ""
        item['images_src'] = [response.xpath("//article[@id='mp-editor']//img/@src").getall()]

        title = "" + response.xpath("//div[@class='text-title']/h1//text()").get()
        item['title'] = title.strip()

        date = "" + response.xpath("//span[@id='news-time']//text()").get()
        item['date'] = date.strip()
        # 按照要求给strong的标签文字末尾加个句号  以后还会加图片路径
        tag_ps = response.xpath("//article[@id='mp-editor']/p")
        # 先获取所有p标签
        contents = []
        for tag_p in tag_ps:
            # 先直接获取所有文本

            # contents.append(tag_p.xpath(".//text()").get().strip())

            text = tag_p.xpath(".//text()").get()
            src = tag_p.xpath("./img/@src").get()
            if src is not None:
                contents.append("(图片:" + src.split('/')[-1] + ")")
            elif text is not None:
                contents.append(text.strip())

            # 如果有strong子标签则在末尾加一个句号。
            if tag_p.xpath("./strong//text()").get() is not None:
                contents.append("。")
        # 数据特点是开头可能会有个“原标题：xxxxx”   末尾可能会有个 ”责任编辑“  还都不显示  但是爬出来了  得去掉
        if "原标题" in contents[0]:
            contents.pop(0)
        if "责任编辑" in contents[len(contents)-1]:
            contents.pop(len(contents)-1)
        item['content'] = "".join(contents).strip()

        # 评论
        # print("=====准备打印一下评论信息====")
        comments = list()
        raw_comments = response.xpath("//div[@class='c-item-comment clear']")
        for raw_comment in raw_comments:
            single = dict()
            # /html/body/div[2]/div[2]/div[2]/div[5]/div/div/div/div[4]/div/div[2]/div[1]/div[2]/div[2]/div[2]/a[3]/i
            username = "" + "".join(raw_comment.xpath("./div[2]/div[1]/div[@class='c-username left']/text()").get())
            single['username'] = username.strip()
            single['location'] = raw_comment.xpath("./div[2]/div[1]/div[@class='c-username left']/span/text()").get()
            single['date'] = raw_comment.xpath("./div[2]/div[2]/div[2]/div[@class='c-date left']/text()").get()
            single['discuss'] = raw_comment.xpath("./div[2]/div[2]/div[@class='c-discuss']/text()").get()
            single['thumb'] = raw_comment.xpath("./div[2]/div[2]/div[2]/a[3]/text()").get()
            comments.append(single)
            # print("子页面，打印这个字典=="+str(single))
        item['comments'] = comments
        # print("=====子页面爬取完毕 准备yield=====")
        yield item



