# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JqkaLssuanceRelatedItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #
    listedCompany_url = scrapy.Field()
    listedCompany_id = scrapy.Field()
    listedCompany_name = scrapy.Field()
    listedCompany_fullName = scrapy.Field()

    listedCompany_enterpriseInfor_issueRelated_establishmentDate = scrapy.Field()
    listedCompany_enterpriseInfor_issueRelated_issueNumber = scrapy.Field()
    listedCompany_enterpriseInfor_issueRelated_issuePrice = scrapy.Field()
    listedCompany_enterpriseInfor_issueRelated_listingDate = scrapy.Field()
    listedCompany_enterpriseInfor_issueRelated_issuePriceEarningsRatio = scrapy.Field()
    listedCompany_enterpriseInfor_issueRelated_expectedFundraising = scrapy.Field()
    listedCompany_enterpriseInfor_issueRelated_firstDayOpeningPrice = scrapy.Field()
    listedCompany_enterpriseInfor_issueRelated_IssuanceRate = scrapy.Field()
    listedCompany_enterpriseInfor_issueRelated_actualFundraising = scrapy.Field()
    listedCompany_enterpriseInfor_issueRelated_leadUnderwriter = scrapy.Field()
    listedCompany_enterpriseInfor_issueRelated_listingSponsor = scrapy.Field()
    listedCompany_enterpriseInfor_issueRelated_history = scrapy.Field()

