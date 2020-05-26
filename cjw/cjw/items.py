# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CjwItem(scrapy.Item):
    title = scrapy.Field()
    source = scrapy.Field()
    date = scrapy.Field()
    article = scrapy.Field()
    url = scrapy.Field()
