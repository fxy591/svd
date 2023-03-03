# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import time
from random import choice
from selenium.webdriver import Chrome
from scrapy import signals
from selenium.webdriver.common.by import By
from mavenLib.settings import USER_AGENT_LIST
from mavenLib.request import SeleniumRequest
from scrapy.http.response.html import HtmlResponse
from selenium.webdriver.chrome.options import Options
# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class MavenlibSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

class MavenlibDownloaderMiddleware1:

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        ua = choice(USER_AGENT_LIST)  # choice 一个 sample 一些
        request.headers['User-Agent'] = ua
        return None
        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        # return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.
        if response.status != 200:
            print("errorrr======="+str(response.status))
        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.
        print("process_exception", "ware1")
        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    # spider启动的时候
    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
        # print("process_exception", "ware1")

class MavenlibDownloaderMiddleware:
    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        # 钩子函数
        s = cls()
        # 注册，                    执行什么功能            在什么时间
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(s.spider_closed, signal=signals.spider_closed)
        return s

    def process_request(self, request, spider):
        # 所有请求都会到这
        # 每个spiders可以有多个spider
        # 需要进行判断是否需要用selenium处理请求
        # 自己定义请求 request.py
        # 修改spider的start_request
        # 开始selenium的操作 返回页面源代码组装的response
        # isinstance 判断xxxx 是不是xxx类型
        if isinstance(request, SeleniumRequest):
            # selenium处理请求
            opt = Options()
            # ua = choice(USER_AGENT_LIST)
            # opt.add_argument(
            #     'user-agent='+ua
            # )
            # opt.add_argument("--headless")
            # opt.add_argument('--disable-gpu')
            opt.add_experimental_option('excludeSwitches', ['enable-automation'])
            opt.add_experimental_option('useAutomationExtension', False)
            web = Chrome(options=opt)
            # self.web = Chrome(options=opt)
            web.get(request.url)
            # self.web.get(request.url)
            time.sleep(2)
            # button = self.web.find_element(By.XPATH, '//*[@id="challenge-stage"]/div/input')
            # if button:
            #     button.click()
            #     time.sleep(2)
            page_source = web.page_source
            # page_source = self.web.page_source
            # 封装一个响应对象
            web.close()
            return HtmlResponse(url=request.url, status=200, body=page_source, request=request, encoding="utf-8")
        else:
            return None

    # spider启动的时候
    def spider_opened(self, spider):
        # self.web = Chrome()
        # 无头浏览器
        opt = Options()
        # ua = choice(USER_AGENT_LIST)
        # opt.add_argument(
        #     'user-agent='+ua
        # )
        # opt.add_argument("--headless")
        # opt.add_argument('--disable-gpu')
        opt.add_experimental_option('excludeSwitches', ['enable-automation'])
        opt.add_experimental_option('useAutomationExtension', False)
        self.web = Chrome(options=opt)
        # self.web = Chrome()


    def spider_closed(self, spider):
        self.web.close()
        # pass



class TestProxyMiddleware(object):
    _proxy = ('j199.kdltps.com', '15818')

    def process_request(self, request, spider):
        # 用户名密码认证
        # username = "t17682229290916"
        # password = "yyxgyl90"
        # request.meta['proxy'] = "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password,
        #                                                                 "proxy": ':'.join(
        #                                                                     TestProxyMiddleware._proxy)}

        # 白名单认证
        # request.meta['proxy'] = "http://%(proxy)s/" % {"proxy": ':'.join(
        #                                                                     TestProxyMiddleware._proxy)}
        # proxy = "http://92.207.253.226:38157"
        # 账密
        entry = 'http://{}:{}@proxy.ipidea.io:2336'.format("f13593235847-zone-custom", "ffxy1119")
        proxy = {
            'http': entry,
            'https': entry,
        }

        request.headers["Connection"] = "close"
        # request.meta["proxy"] = entry
        print(f"TestProxyMiddleware --> ")
        return None