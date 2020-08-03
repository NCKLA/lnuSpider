# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JqkaSvzlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    listedCompany_name = scrapy.Field()
    listedCompany_url = scrapy.Field()
    listedCompany_id = scrapy.Field()

    listedCompany_svzl_institutionholdSummary = scrapy.Field()  # 上市公司_主力持仓_机构持股汇总 模块
    # listedCompany_svzl_institutionholdSummary_reportingPeriod = scrapy.Field()               # 上市公司_主力持仓_机构持股汇总_主力进出\报告期
    # listedCompany_svzl_institutionholdSummary_organizationNumber = scrapy.Field()            # 上市公司_主力持仓_机构持股汇总_机构数量
    # listedCompany_svzl_institutionholdSummary_accumulatedHoldingQuantity = scrapy.Field()    # 上市公司_主力持仓_机构持股汇总_累计持有数量
    # listedCompany_svzl_institutionholdSummary_totalMarketValue = scrapy.Field()              # 上市公司_主力持仓_机构持股汇总_累计市值
    # listedCompany_svzl_institutionholdSummary_positionRatio = scrapy.Field()                 # 上市公司_主力持仓_机构持股汇总_持仓比例
    # listedCompany_svzl_institutionholdSummary_comparedPreviousPeriodChange = scrapy.Field()  # 上市公司_主力持仓_机构持股汇总_较长期变化

    listedCompany_svzl_institutionholdDetail = scrapy.Field()  # 上市公司_主力持仓_机构持股明细 模块
    # listedCompany_svzl_institutionholdDetail_organizationOrFundName = scrapy.Field()       # 上市公司_主力持仓_机构持股明细_机构或基金名称
    # listedCompany_svzl_institutionholdDetail_organizationType = scrapy.Field()             # 上市公司_主力持仓_机构持股明细_机构类型
    # listedCompany_svzl_institutionholdDetail_quantityHeld = scrapy.Field()                 # 上市公司_主力持仓_机构持股明细_持有数量
    # listedCompany_svzl_institutionholdDetail_marketValue = scrapy.Field()                  # 上市公司_主力持仓_机构持股明细_持有市值
    # listedCompany_svzl_institutionholdDetail_circulationSharesProportion = scrapy.Field()  # 上市公司_主力持仓_机构持股明细_占流通股比例
    # listedCompany_svzl_institutionholdDetail_increaseOrDecrease = scrapy.Field()           # 上市公司_主力持仓_机构持股明细_增减情况
    # listedCompany_svzl_institutionholdDetail_fundIncomeRanking = scrapy.Field()            # 上市公司_主力持仓_机构持股明细_基金收益情况
    # listedCompany_svzl_institutionholdDetail_date = scrapy.Field()                         # 上市公司_主力持仓_机构持股明细_日期

    listedCompany_svzl_ipoInstitution = scrapy.Field()         # 上市公司_主力持仓_IPO获配机构 模块
    # listedCompany_svzl_ipoInstitution_organizationName = scrapy.Field()            # 上市公司_主力持仓_IPO获配机构_机构名称
    # listedCompany_svzl_ipoInstitution_allottedQuantity = scrapy.Field()            # 上市公司_主力持仓_IPO获配机构_获配数量
    # listedCompany_svzl_ipoInstitution_applyPurchasingQuantity = scrapy.Field()     # 上市公司_主力持仓_IPO获配机构_申购数量
    # listedCompany_svzl_ipoInstitution_lockupPeriod = scrapy.Field()                # 上市公司_主力持仓_IPO获配机构_锁定期
    # listedCompany_svzl_ipoInstitution_organizationType = scrapy.Field()            # 上市公司_主力持仓_IPO获配机构_机构类型


