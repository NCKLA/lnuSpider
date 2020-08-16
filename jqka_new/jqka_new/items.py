# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JqkaNewItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    listedCompany_url = scrapy.Field()
    listedCompany_id = scrapy.Field()
    listedCompany_name = scrapy.Field()
    listedCompany_fullName = scrapy.Field()
    # listedCompany_news_announceList__url = scrapy.Field()
    # listedCompany_news_announceList__url0 = scrapy.Field()

    # 公告列表
    listedCompany_news_announceList = scrapy.Field()
    # listedCompany_news_announceList_tag = scrapy.Field()
    # listedCompany_news_announceList_date = scrapy.Field()

