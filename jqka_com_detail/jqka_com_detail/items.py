# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JqkaComDetailItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    company_name = scrapy.Field()
    # company_start_time = scrapy.Field()
    # company_market_time = scrapy.Field()
    company_location = scrapy.Field()
    company_english_name = scrapy.Field()
    company_industry = scrapy.Field()
    company_before_name = scrapy.Field()
    company_url = scrapy.Field()
    company_content2_1 = scrapy.Field()
    company_content2_2 = scrapy.Field()
    company_introduction = scrapy.Field()
    url = scrapy.Field()
    # url = scrapy.Field()
    # title = scrapy.Field()
    # date = scrapy.Field()
    # source_name = scrapy.Field()
    # cont = scrapy.Field()

