# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JqkaBusinessAnalysisItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    listedCompany_name = scrapy.Field()
    listedCompany_url = scrapy.Field()
    listedCompany_id = scrapy.Field()
    # 主营介绍
    listedCompany_businessAnalysis_mainBusiness = scrapy.Field()
    # 主营构成分析
    listedCompany_businessAnalysis_mainBusinessCompositionAnalysis = scrapy.Field()
    # 董事会经营评述
    listedCompany_businessAnalysis_reviewOfBoardOperation = scrapy.Field()