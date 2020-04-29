# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JqkaComDetailItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    corporationBackground_industryCommerceImformation_name = scrapy.Field()
    # company_start_time = scrapy.Field()
    # company_market_time = scrapy.Field()
    corporationBackground_industryCommerceImformation_registeredAddress = scrapy.Field()
    corporationBackground_industryCommerceImformation_englishName = scrapy.Field()
    corporationBackground_industryCommerceImformation_industry = scrapy.Field()
    corporationBackground_industryCommerceImformation_nameOnceUsed = scrapy.Field()
    corporationBackground_industryCommerceImformation_officialWebsite = scrapy.Field()
    company_content2_1 = scrapy.Field()
    company_content2_2 = scrapy.Field()
    company_introduction = scrapy.Field()
    url = scrapy.Field()
    # url = scrapy.Field()
    # title = scrapy.Field()
    # date = scrapy.Field()
    # source_name = scrapy.Field()
    # cont = scrapy.Field()

