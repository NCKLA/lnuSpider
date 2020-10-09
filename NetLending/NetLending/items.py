# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NetlendingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name=scrapy.Field()
    time=scrapy.Field()
    website=scrapy.Field()
    recommend=scrapy.Field()
    impression=scrapy.Field()
    comment=scrapy.Field()
    useful=scrapy.Field()
    useless=scrapy.Field()
    newcomment=scrapy.Field()
    geilicomment=scrapy.Field()
