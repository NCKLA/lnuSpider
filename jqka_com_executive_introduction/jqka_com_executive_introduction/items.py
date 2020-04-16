# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JqkaComExecutiveIntroductionItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    company_name = scrapy.Field()
    url = scrapy.Field()
    company_content2_1 = scrapy.Field()
    company_content2_2 = scrapy.Field()
    company_content2_3 = scrapy.Field()
