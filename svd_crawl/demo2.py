import logging
import random

import scrapy

# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from scrapy_splash import SplashRequest
from scrapy.http import HtmlResponse

from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware
import json
import redis
import toml



# splash lua script
script = """
         function main(splash, args)
             --splash:clear_cookies()
             --splash:init_cookies(args.cookies)
             assert(splash:go(args.url))
             assert(splash:wait(args.wait))
             return splash:html()
         end
         """


class DemoSpider(Spider):
    name = 'demo2'
    # url = 'http://httpbin.org/ip'
    url = 'https://mvnrepository.com/open-source'
    custom_settings = {

        "SPLASH_URL": 'http://124.223.65.98:8050/',
        'LOG_LEVEL': 'INFO',
        'CONCURRENT_REQUESTS': 8,
        'AUTOTHROTTLE_ENABLED': True,
        'AUTOTHROTTLE_TARGET_CONCURRENCY': 8,

        'DOWNLOADER_MIDDLEWARES': {
            'scrapy_splash.SplashCookiesMiddleware': 723,
            'scrapy_splash.SplashMiddleware': 725,
            'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
        },
        'SPIDER_MIDDLEWARES': {
            'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
        },
        'DUPEFILTER_CLASS': 'scrapy_splash.SplashAwareDupeFilter',
        'HTTPCACHE_STORAGE': 'scrapy_splash.SplashAwareFSCacheStorage',

    }

    # start request
    def start_requests(self):
        for i in range(1000):
            self.logger.info(f'0000000000{i}')
            cookies = {'name': 'test', 'values': 'test'}
            yield SplashRequest(self.url, callback=self.parse, endpoint='execute',
                                args={'lua_source': script, 'cookies': cookies, 'wait': random.choice(range(10)), 'url': self.url},dont_filter=True)

    def parse(self, response: HtmlResponse, **kwargs):
        self.logger.info(response.status)
        self.logger.info(response.text)



if __name__ == '__main__':
    from scrapy.cmdline import execute

    execute('scrapy crawl demo2'.split())
