from scrapy import cmdline
cmdline.execute("scrapy crawl sohucaijing_Spider".split())

# cmdline.execute("scrapy crawl wzhhexun".split())


# cmdline.execute("scrapy crawl wzhtonghuashun".split())

# import urllib3
#
# http = urllib3.PoolManager()
#
# r = http.request('GET', "http://5b0988e595225.cdn.sohucs.com/images/20200328/4eca574a6f90"
#                                        "4cefafbb5c9fa97994bc.png")
# with open("wzhProject/data/image/sohucaijing/ceshi_image.png", 'wb') as file_writer:
#     file_writer.write(r.data)
# file_writer.close()
