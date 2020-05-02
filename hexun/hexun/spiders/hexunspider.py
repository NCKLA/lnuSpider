# -*- coding: utf-8 -*-
import scrapy
from hexun.items import HexunItem
import time
import json

class HexunspiderSpider(scrapy.Spider):
    name = 'hexunspider'
    allowed_domains = ['hexun.com']
    start_urls=["http://open.tool.hexun.com/MongodbNewsService/data/getOriginalNewsList.jsp?id=187804274&s=30&cp=1&priority=0&callback=hx_json11587781686930"]

    #需要获取文章标题、文章内容、文章作者、文章发表时间(必须要有)
    def parse(self, response):
        #循环一百次，这100页的js源码
        for i in range(1,101):
            #拼接好了所有的url，每一个url里面有20个文章的标题，以及20具体文章的链接
            url = "http://open.tool.hexun.com/MongodbNewsService/data/getOriginalNewsList.jsp?id=187804274&s=30&cp=%d" %i+"&priority=0&callback=hx_json11587781686930"
            print(url)
            time.sleep(1)
            yield scrapy.Request(url=url,callback=self.detail_parse,dont_filter=True)


    # 此处处理返回来的文本信息.
    def detail_parse(self,response):
        item = HexunItem()
        articlestr = response.text
        #截取之后的
        articles = articlestr[23:-4]
        # print(articles)
        json_obj = json.loads((articles))
        urls = []
        for i in range(0,len(json_obj['result'])):
            print(str(json_obj['result'][i]))
            urls.append(str(json_obj['result'][i]['entityurl']))

        item['url'] = urls
        yield item


        #     json_obj = json.loads((sss[23:-2]))
        #     print(type(json_obj))
        #     print(json_obj)
        #     for i in range(0, len(json_obj['result']) - 1):
        #         print(str(json_obj['result'][i]))
        #         print(str(json_obj['result'][i]['entitytime']))
        #     # s1 = "hx_json11587781686930( "
        #     # print(len(s1))

        # with open("test.txt", "r") as f:
        #     for res in json_obj['result']:
        #         f.writelines(str(res['entityurl']))
        #         # print(str(res['entityurl']))
        #     f.close()
        pass

    # def parse_url(self,response):
    #     #读取excel表格中的网址
    #     # 读取excel表格
    #     print(response.text)
    #     book = load_workbook(filename="com_list.xlsx")
    #     sheet = book.active
    #     # 字典，存取从excel表格中读取出来的网址
    #     articleurls = []
    #     # data.append(sheet.cell(row=row_num, column=3).value)
    #     row_num = 1
    #     while row_num <= 20:
    #         articleurl = sheet.cell(row=row_num,column=1).value
    #         print(articleurl)
    #         break







