# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JqkaFundRaisingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    listedCompany_url = scrapy.Field()
    listedCompany_id = scrapy.Field()
    listedCompany_name = scrapy.Field()
    fund_raising = scrapy.Field()
