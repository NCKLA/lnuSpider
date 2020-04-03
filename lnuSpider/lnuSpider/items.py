# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LnuspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # title = scrapy.Field()
    # content = scrapy.Field()
    # comments = scrapy.Field()
    # tags = scrapy.Field()
    # date = scrapy.Field()
    url = scrapy.Field()
    # images_src = scrapy.Field()
    pass


class JqkaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    tag = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    date = scrapy.Field()
    source_name = scrapy.Field()
    cont = scrapy.Field()