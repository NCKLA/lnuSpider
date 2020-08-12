# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JqkaEquitystrucItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    listedCompany_name = scrapy.Field()
    listedCompany_url = scrapy.Field()
    listedCompany_id = scrapy.Field()
    listedCompany_fullName = scrapy.Field()

    # 股东人数模块
    listedCompany_shareholderResearch_shareholderNum = scrapy.Field()
    # listedCompany_shareholderResearch_shareholderNum_time = scrapy.Field()
    # listedCompany_shareholderResearch_shareholderNum_totalShareholdersNumber = scrapy.Field()
    # listedCompany_shareholderResearch_shareholderNum_comparedPreviousPeriodChange = scrapy.Field()
    # listedCompany_shareholderResearch_shareholderNum_perCapitaCirculatingShares = scrapy.Field()
    # listedCompany_shareholderResearch_shareholderNum_perCapitaCirculationChanges = scrapy.Field()
    # listedCompany_shareholderResearch_shareholderNum_industryAverage = scrapy.Field()

    # 十大流通股东模块
    listedCompany_shareholderResearch_topTenCurrentShareholders_time = scrapy.Field()
    listedCompany_shareholderResearch_topTenCurrentShareholders = scrapy.Field()
    listedCompany_shareholderResearch_topTenCurrentShareholders_increaseOrDecrease = scrapy.Field()

    # 十大股东 模块
    listedCompany_shareholderResearch_topTenShareholders = scrapy.Field()


