# -*- coding: utf-8 -*-
import scrapy

from lnuSpider.items import LnuspiderItem


class SohucaijingSpiderSpider(scrapy.Spider):
    name = 'sohucaijing_Spider'
    allowed_domains = ['mp.sohu.com/profile?xpt=c29odWNqeWMyMDE3QHNvaHUuY29t&_'
                       'f=index_pagemp_1&spm=smpc.ch15.top-subnav.8.1585379351817DgmoPb1',
                       'www.sohu.com/a/']
    start_urls = ['http://mp.sohu.com/profile?xpt=c29odWNqeWMyMDE3QHNvaHUuY29t&_'
                  'f=index_pagemp_1&spm=smpc.ch15.top-subnav.8.1585379351817DgmoPb1/']

    # 需求内容： 标题 正文  日期  原链接  标签  类别暂时没有  评论
    def parse(self, response):
        infos = response.xpath("//ul[@class='feed-list-area feed-normal-list-area']/li")
        for info in infos:
            item = LnuspiderItem()
            # title = info.xpath(".//h4[@class='feed-title']/a//text()").get().strip()

            url = info.xpath(".//h4/a/@href").get()
            # 获取到的是'//www.sohu.com/a/383791237_100001551'  但是getall获取的是个list

            # jianjie = info.xpath(".//p//text()").get().strip()

            tags = info.xpath(".//article/div/div/span/a//text()").getall()

            item['url'] = "http:"+url
            item['tags'] = tags
            print("=====准备进入子页面=====")
            yield scrapy.Request(item['url'], meta={'item': item}, callback=self.detail_parse)
        return

    def detail_parse(self, response):
        print("=====进入子页面成功=====")
        item = response.meta['item']
        item['title'] = response.xpath("//div[@class='text-title']/h1//text()").get().strip()
        item['date'] = response.xpath("//span[@id='news-time']//text()").get().strip()
        # 按照要求给strong的标签文字末尾加个句号  以后还会加图片路径
        tag_ps = response.xpath("//article[@id='mp-editor']/p")
        # 先获取所有p标签
        contents = []
        for tag_p in tag_ps:
            # 先直接获取所有文本

            # contents.append(tag_p.xpath(".//text()").get().strip())

            text = tag_p.xpath(".//text()").get()
            if text is not None:
                contents.append(text.strip())
            else:
                src = tag_p.xpath("./img/@src").get()

            # 如果有strong子标签则在末尾加一个句号。
            if tag_p.xpath("./strong//text()").get() is not None:
                contents.append("。")
        # 数据特点是开头可能会有个“原标题：xxxxx”   末尾可能会有个 ”责任编辑“  还都不显示  但是爬出来了  得去掉
        if "原标题" in contents[0]:
            contents.pop(0)
        if "责任编辑" in contents[len(contents)-1]:
            contents.pop(len(contents)-1)
        item['content'] = "".join(contents).strip()
        # 评论先等等

        print("=====子页面爬取完毕 准备yield=====")
        yield item



