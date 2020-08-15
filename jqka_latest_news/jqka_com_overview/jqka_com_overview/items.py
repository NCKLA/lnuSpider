# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JqkaComOverviewItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    listedCompany_url = scrapy.Field()
    listedCompany_id = scrapy.Field()
    listedCompany_name = scrapy.Field()
    listedCompany_latestNews_comBrief_comHighlights = scrapy.Field()
    listedCompany_latestNews_comBrief_comPopularityRanking = scrapy.Field()
    listedCompany_latestNews_comBrief_industryPopularityRanking = scrapy.Field()
    listedCompany_latestNews_comBrief_mainBusiness = scrapy.Field()
    listedCompany_latestNews_comBrief_shenwanIndustry = scrapy.Field()
    listedCompany_latestNews_comBrief_conceptFitRanking = scrapy.Field()
    listedCompany_latestNews_comBrief_domesticMarketsComparableCompanies = scrapy.Field()
    listedCompany_latestNews_comBrief_foreignMarketsComparableCompanies = scrapy.Field()
