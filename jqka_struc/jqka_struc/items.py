# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JqkaStrucItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    listedCompany_name = scrapy.Field()
    listedCompany_url = scrapy.Field()
    listedCompany_id = scrapy.Field()
    listedCompany_fullName = scrapy.Field()

    # 1.解禁时间表 模块
    listedCompany_equityStruc_liftBanTimeTable = scrapy.Field()
    # 2.总股本结构 模块
    listedCompany_equityStruc_shareStructure = scrapy.Field()
    # 3.股本变动
    ListedCompany_equityStruc_equityChanges = scrapy.Field()
