# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CaijingwangItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    source = scrapy.Field()
    date = scrapy.Field()
    article = scrapy.Field()
    editor = scrapy.Field()