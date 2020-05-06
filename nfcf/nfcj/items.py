# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NfcjItem(scrapy.Item):
    title = scrapy.Field()
    date_source = scrapy.Field()
    article = scrapy.Field()