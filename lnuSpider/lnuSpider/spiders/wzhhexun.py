# -*- coding: utf-8 -*-
import scrapy
import json
import requests
import ip_proxy

'''
按照飞蚁代理自己的说法，最好是建立本地数据库，写个脚本进行调用。
但是问题来了，我就算有这么个数据库了，获得的链接也早就开始计费了，最贵的也就能支持半个点。
然后又看了下scrapy的代理调用，要么写在中间层要么写在spider。
然后问题又来了，如果我直接把代理写在spider，那么可能会碰到动态加载。那还是获取不到东西。
如果我写在中间件，那么spider的起始请求就可能因为我自己被ban的原因给ban了。
再者，如果两个都写，那spider获取一次代理，中间件又获取，会造成ip浪费不说，发起请求和模拟点击的ip都不一样。

思来想去决定在spider层先生成这么个代理，写在self里，中间件也是要获取spider的，就一并获取了。

但是问题还有，就是没法很好的判断这个ip是否失效了，目前知道的是可以判断“疑似恶意访问，已经拦截啥啥啥”的这个句子，
这句话如果在的话可以判断这个ip失效
但是中间件出现这个问题的话。。

我再想想
'''


class WzhhexunSpider(scrapy.Spider):
    def __init__(self):
        # self.driver = webdriver.PhantomJS(executable_path=r'C:\Users\G50\local\bin\phantomjs.exe')
        # # 设置timeout 不设置大概会像我一样卡死
        # self.driver.set_page_load_timeout(40)
        super().__init__()
        # self.min_page = 1
        # self.max_page = 100
        #
        # self.list_page = range(self.min_page, self.max_page)

        self.json_obj = None
        self.domain = None
        self.port = None

        WzhhexunSpider.new_port(self)

    def new_port(self):
        print("准备开始获取url的try")

        try:
            open_url = ip_proxy.get_open_url()

            # 向代理服务器发起请求，去拿端口号（ip地址是固定的好像）
            r = requests.get(open_url, timeout=5)
            result = str(r.content)

            if "b\'" in result:
                result = result[2:-1]
            print("result   "+result)
            # logging.info('open_url||' + result)

            # json_obj为响应json
            self.json_obj = json.loads(result)

            code = self.json_obj['code']
            self.domain = self.json_obj['domain']
            # 获得的端口号（如果状态码为100）
            if code == 100:
                self.port = str(self.json_obj['port'][0])
            elif code == 108:
                reset_url = ip_proxy.get_reset_url()
                r = requests.get(reset_url, timeout=5)
            else:
                print("异常的状态码："+str(code))
            # 状态码说明
            # 100 成功
            # 101 认证不通过
            # 102 请求格式不正确
            # 103 IP暂时耗尽
            # 106 账号使用时间到期
            # 118 ip使用量已用完
        except Exception as e:
            print("申请端口，try出事儿了" + repr(e))

        print("try完了")
        print("打印domain和port   " + self.domain + ":" + self.port)

    def close_port(self, port):
        print("准备开始关闭端口{}的try".format(port))
        try:
            print("开始try  准备close")
            close_url = ip_proxy.get_close_url(port)
            r = requests.get(close_url, timeout=5)
            print("close result: " + str(r.content))
        except Exception as e:
            print("关闭端口，try出事了: " + repr(e))

    name = 'wzhhexun'
    allowed_domains = ['open.tool.hexun.com/MongodbNewsService/data/']
    start_urls = ['http://open.tool.hexun.com/MongodbNewsService/data/'
                  'getOriginalNewsList.jsp?id=187804274&s=30&cp=6&priority=1&callback=hx_json11587634991522']
    # allowed_domains = ['ip.cn']
    # start_urls = ['https://ip.cn/']

    # copy来的一段scrapy使用代理
    def start_requests(self):
        url = WzhhexunSpider.start_urls[0]
        proxy = self.domain + ":" + str(self.port)

        proxies = ""
        if url.startswith("http://"):
            proxies = "http://"+str(proxy)
        elif url.startswith("https://"):
            proxies = "https://"+str(proxy)
        # 注意这里面的meta={'proxy':proxies},一定要是proxy进行携带,其它的不行,后面的proxies一定 要是字符串,其它任何形式都不行
        yield scrapy.Request(url, callback=self.parse, meta={'proxy': proxies})

    def parse(self, response):
        print(response.text)
