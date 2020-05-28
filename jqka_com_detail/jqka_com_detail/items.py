# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JqkaComDetailItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    listedCompany_enterpriseIntro_companyFullName = scrapy.Field()
    listedCompany_enterpriseIntro_region = scrapy.Field()
    listedCompany_enterpriseIntro_englishName = scrapy.Field()
    listedCompany_enterpriseIntro_industry = scrapy.Field()
    listedCompany_enterpriseIntro_formerlyUsedName = scrapy.Field()
    listedCompany_enterpriseIntro_websiteAddress = scrapy.Field()
    listedCompany_name = scrapy.Field()
    listedCompany_url = scrapy.Field()
    listedCompany_id = scrapy.Field()
    company_content2_1 = scrapy.Field()
    company_content2_2 = scrapy.Field()
    listedCompany_enterpriseIntro_companyProfile = scrapy.Field()

    # url = scrapy.Field()
    # title = scrapy.Field()
    # date = scrapy.Field()
    # source_name = scrapy.Field()
    # cont = scrapy.Field()

