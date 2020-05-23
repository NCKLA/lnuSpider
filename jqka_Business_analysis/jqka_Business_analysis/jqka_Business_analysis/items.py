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
    listedCompany_mainBusiness = scrapy.Field()
    listedCompany_mainBusinessCompositionAnalysis_1 = scrapy.Field()
    listedCompany_mainBusinessCompositionAnalysis_2 = scrapy.Field()
    listedCompany_mainBusinessCompositionAnalysis_3 = scrapy.Field()
