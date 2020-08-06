# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JqkaNewsAnnouncementItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 公司信息
    listedCompany_id = scrapy.Field()
    listedCompany_name = scrapy.Field()
    listedCompany_url = scrapy.Field()


    # 热点新闻列表 模块 listedCompany_news_hotnews
    listedCompany_news_hotnews = scrapy.Field()
    # listedCompany_news_hotnews_tag = scrapy.Field()       # 热点新闻 标签
    # listedCompany_news_hotnews_time = scrapy.Field()      # 热点新闻 发布时间
    # listedCompany_news_hotnews_title = scrapy.Field()     # 热点新闻 标题
    # listedCompany_news_hotnews_refer = scrapy.Field()     # 热点新闻 来源
    # listedCompany_news_hotnews_content = scrapy.Field()   # 热点新闻 内容

