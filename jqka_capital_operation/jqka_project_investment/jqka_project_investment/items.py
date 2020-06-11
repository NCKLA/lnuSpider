# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JqkaProjectInvestmentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    listedCompany_url = scrapy.Field()
    listedCompany_id = scrapy.Field()
    listedCompany_name = scrapy.Field()
    project_investment = scrapy.Field()

