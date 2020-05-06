import random


USER_AGENTS = ["Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201",
               "Mozilla/5.0 (Windows; U; Windows NT 6.1; it; rv:2.0b4) Gecko/20100818",
               "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
               "Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko",
               "Mozilla/5.0 (compatible; MSIE 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1;"
               " .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0",
               "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:77.0) Gecko/20190101 Firefox/77.0",
               "Mozilla/5.0 (X11; Linux ppc64le; rv:75.0) Gecko/20100101 Firefox/75.0",
               "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.10; rv:75.0) Gecko/20100101 Firefox/75.0",
               "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:77.0) Gecko/20100101 Firefox/77.0",
               "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; TencentTraveler 4.0; Trident/4.0;"
               " SLCC1; Media Center PC 5.0; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30618)",
               "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; QQDownload 1.7; GTB6.6; TencentTrav"
               "eler 4.0; SLCC1; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.5.30729; .NET CLR 3.0.30729)",
               "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; iCafeMedia; TencentTraveler 4.0; "
               "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; .NET CLR 1.1.4322; .NET CLR 2.0.50727;"
               " .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)",
               "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; TencentTraveler 4.0; QQDownload 667; SLCC1;"
               " .NET CLR 2.0.50727; .NET CLR 3.0.04506)",
               "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; QQPinyin 686; QQDownload 661; GTB6.6; "
               "TencentTraveler 4.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
               "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; QQDownload 1.7; GTB6.6; "
               "TencentTraveler 4.0)",
               "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.3a) Gecko/20021207 Phoenix/0.5",
               "Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.3a) Gecko/20021207 Phoenix/0.5",
               "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.4a) Gecko/20030411 Phoenix/0.5",
               "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.3a) Gecko/20021207 Phoenix/0.5",
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
               "Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582",
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
               " Chrome/70.0.3538.102 Safari/537.36 Edge/18.19577",
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
               "(KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
               "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 "
               "(KHTML, like Gecko) Chrome/55.0.2919.83 Safari/537.36",
               "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko)"
               " Chrome/54.0.2866.71 Safari/537.36",
               "Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16.2",
               "Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16",
               "Opera/9.80 (Macintosh; Intel Mac OS X 10.14.1) Presto/2.12.388 Version/12.16",
               "Mozilla/5.0 (Windows NT 6.0; rv:2.0) Gecko/20100101 Firefox/4.0 Opera 12.14",
               "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko)"
               " Version/7.0.3 Safari/7046A194A",
               "Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko)"
               " Version/6.0 Mobile/10A5355d Safari/8536.25",
               "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.13+ (KHTML, like Gecko)"
               " Version/5.1.7 Safari/534.57.2"]


# 返回一个随机请求头，str
def give_a_head():
    return random.choice(USER_AGENTS)
