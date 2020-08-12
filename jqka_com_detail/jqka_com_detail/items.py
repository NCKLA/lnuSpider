# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JqkaComDetailItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    listedCompany_enterpriseInfor_detailInfor_companyFullName = scrapy.Field()
    listedCompany_enterpriseInfor_detailInfor_region = scrapy.Field()
    listedCompany_enterpriseInfor_detailInfor_englishName = scrapy.Field()
    listedCompany_enterpriseInfor_detailInfor_industry = scrapy.Field()
    listedCompany_enterpriseInfor_detailInfor_formerlyUsedName = scrapy.Field()
    listedCompany_enterpriseInfor_detailInfor_websiteAddress = scrapy.Field()
    listedCompany_name = scrapy.Field()
    listedCompany_url = scrapy.Field()
    listedCompany_id = scrapy.Field()
    listedCompany_fullName = scrapy.Field()
    company_content2_1 = scrapy.Field()
    company_content2_2 = scrapy.Field()
    listedCompany_enterpriseInfor_detailInfor_companyProfile = scrapy.Field()

    # url = scrapy.Field()
    # title = scrapy.Field()
    # date = scrapy.Field()
    # source_name = scrapy.Field()
    # cont = scrapy.Field()

