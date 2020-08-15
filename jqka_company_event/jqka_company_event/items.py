# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JqkaCompanyEventItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    listedCompany_name = scrapy.Field()
    listedCompany_url = scrapy.Field()
    listedCompany_id = scrapy.Field()
    listedCompany_fullName = scrapy.Field()

    # 1.违规处理 模块
    listedCompany_companyEvent_handofViolation = scrapy.Field()
    # 2.高管持股变动 模块
    listedCompany_companyEvent_executiveShareholdingchanges = scrapy.Field()
    # 3.股东持股变动模块
    listedCompany_companyEvent_shareholderholdingchanges = scrapy.Field()
