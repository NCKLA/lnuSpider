# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JqkaBonusItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    listedCompany_name = scrapy.Field()
    listedCompany_url = scrapy.Field()
    listedCompany_id = scrapy.Field()
    listedCompany_fullName = scrapy.Field()

    # 1.分红情况 模块
    listedCompany_dividendFinancing_dividendMatter = scrapy.Field()
    # 2.配股情况 模块
    listedCompany_dividendFinancing_allotmentCondition = scrapy.Field()
    # 3.机构获配明细 模块
    listedCompany_dividendFinancing_organizationAllocation = scrapy.Field()
    # 4.增发情况 模块
    listedCompany_dividendFinancing_additionalIssue = scrapy.Field()

