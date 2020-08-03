# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JqkaCapitalOperationItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    listedCompany_name = scrapy.Field()
    listedCompany_url = scrapy.Field()
    listedCompany_id = scrapy.Field()

    listedCompany_capitalOperation_fundRaisingSource = scrapy.Field()   # 1.募集资金来源 模块

    listedCompany_capitalOperation_projectInvestment = scrapy.Field()    # 2.项目投资 模块

    listedCompany_capitalOperation_purchaseandMergers = scrapy.Field()   # 3.收购兼并 模块

    listedCompany_capitalOperation_equityInvestment = scrapy.Field()     # 4.股权投资 模块

    listedCompany_capitalOperation_equityTransfer = scrapy.Field()       # 5.股权转让 模块

    listedCompany_capitalOperation_relatedTransactions = scrapy.Field()  # 6.关联交易 模块
