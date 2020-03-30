# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LnuspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    comments = scrapy.Field()
    tags = scrapy.Field()
    date = scrapy.Field()
    url = scrapy.Field()
    path = scrapy.Field()
    pass


class ImageItem(scrapy.Item):
    src = scrapy.Field()
    path = scrapy.Field()
    pass
