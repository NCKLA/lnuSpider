# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class WangdaizhijiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    author = scrapy.Field()

    comment_time = scrapy.Field()

    wangdai_company = scrapy.Field()

    wangdai_company_url_text = scrapy.Field()

    tuijian = scrapy.Field()

    impressions = scrapy.Field()

    feelings = scrapy.Field()

    comment = scrapy.Field()

    comment_recover = scrapy.Field()

    # total_comment = scrapy.Field()

