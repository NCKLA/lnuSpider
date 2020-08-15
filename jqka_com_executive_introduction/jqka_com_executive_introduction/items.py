# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JqkaComExecutiveIntroductionItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    listedCompany_name = scrapy.Field()
    listedCompany_url = scrapy.Field()
    listedCompany_id = scrapy.Field()
    listedCompany_fullName = scrapy.Field()
    company_content1 = scrapy.Field()
    company_content2 = scrapy.Field()
    company_content3 = scrapy.Field()
    company_content4 = scrapy.Field()
    company_content5 = scrapy.Field()
    company_content6 = scrapy.Field()
