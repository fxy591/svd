# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import time
from random import choice
from selenium.webdriver import Chrome
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from svd.request import SeleniumRequest
from scrapy.http.response.html import HtmlResponse
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.options import Options
# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
# import undetected_chromedriver.v2 as uc
from twisted.internet import defer
from twisted.internet.error import TimeoutError, DNSLookupError, \
    ConnectionRefusedError, ConnectionDone, ConnectError, \
    ConnectionLost, TCPTimedOutError
from scrapy.http import HtmlResponse
from twisted.web.client import ResponseFailed
from scrapy.core.downloader.handlers.http11 import TunnelError

class SvdSpiderMiddleware:
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
        # that it doesn???t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class SvdDownloaderMiddleware:
    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        # ????????????
        s = cls()
        # ?????????                    ??????????????????            ???????????????
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(s.spider_closed, signal=signals.spider_closed)
        return s

    def process_request(self, request, spider):
        # ????????????????????????
        # ??????spiders???????????????spider
        # ?????????????????????????????????selenium????????????
        # ?????????????????? request.py
        # ??????spider???start_request
        # ??????selenium????????? ??????????????????????????????response
        # isinstance ??????xxxx ?????????xxx??????
        if isinstance(request, SeleniumRequest):
            # selenium????????????
            # opt = Options()

            # options = ChromeOptions()
            # options.add_experimental_option('excludeSwitches', ['enable-automation'])
            #
            # # web = Chrome(options=options)
            chrome_options = uc.ChromeOptions()
            chrome_options.add_argument("--disable-extensions")
            chrome_options.add_argument("--disable-popup-blocking")
            chrome_options.add_argument("--profile-directory=Default")
            chrome_options.add_argument("--ignore-certificate-errors")
            chrome_options.add_argument("--disable-plugins-discovery")
            chrome_options.add_argument("--incognito")
            chrome_options.add_argument('--no-first-run')
            chrome_options.add_argument('--no-service-autorun')
            chrome_options.add_argument('--no-default-browser-check')
            chrome_options.add_argument('--password-store=basic')
            chrome_options.add_argument('--no-sandbox')

            web = uc.Chrome(options=chrome_options)
            # web = Chrome()
            # web = uc.Chrome()
            web.get(request.url)
            time.sleep(5)

            page_source = web.page_source
            time.sleep(5)
            # page_source = self.web.page_source
            # ????????????????????????
            # web.close()
            return HtmlResponse(url=request.url, status=200, body=page_source, request=request, encoding="utf-8")
        else:
            return None

    # spider???????????????
    def spider_opened(self, spider):
        # opt = Options()
        # opt.add_argument('-ignore-certificate-errors')
        # opt.add_argument('-ignore -ssl-errors')
        # opt.add_argument('--disable-blink-features=AutomationControlled')
        # opt.add_experimental_option('excludeSwitches', ['enable-automation'])
        # opt.add_experimental_option('useAutomationExtension', False)
        # self.web = Chrome(options=opt)
        # self.web = uc.Chrome()

        pass

    def spider_closed(self, spider):
        # self.web.close()
        pass


class TestProxyMiddleware(object):
    _proxy = ('n419.kdltps.com', '15818')

    def process_request(self, request, spider):
        # ?????????????????????
        username = "t17781792274249"
        password = "nmudozhr"
        request.meta['proxy'] = "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password,
                                                                        "proxy": ':'.join(
                                                                            TestProxyMiddleware._proxy)}

        # ???????????????
        # request.meta['proxy'] = "http://%(proxy)s/" % {"proxy": ':'.join(
        #                                                                     TestProxyMiddleware._proxy)}
        # proxy = "http://92.207.253.226:38157"
        # ??????
        # entry = 'http://{}:{}@proxy.ipidea.io:2336'.format("f13593235847-zone-custom", "ffxy1119")
        # proxy = {
        #     'http': entry,
        #     'https': entry,
        # }

        request.headers["Connection"] = "close"
        # request.meta["proxy"] = entry
        # print(f"TestProxyMiddleware --> {request.meta['proxy']}")
        return None

class ProcessAllExceptionMiddleware(object):
    ALL_EXCEPTIONS = (defer.TimeoutError, TimeoutError, DNSLookupError,
                      ConnectionRefusedError, ConnectionDone, ConnectError,
                      ConnectionLost, TCPTimedOutError, ResponseFailed,
                      IOError, TunnelError)

    def process_response(self, request, response, spider):
        # ??????????????????40x/50x???response
        if str(response.status).startswith('4') or str(response.status).startswith('5'):
            # ??????????????????
            return request
        # ????????????????????????
        return response

    def process_exception(self, request, exception, spider):
        # ???????????????????????????
        if isinstance(exception, self.ALL_EXCEPTIONS):
            # ??????????????????????????????
            print('Got exception: %s' % (exception))
            # ??????????????????
            return request
        # ??????????????????????????????
        print('not contained exception: %s' % exception)