# _*_ coding: utf-8 _*_
# @Time : 2023/2/27 17:39
# @Author ： primary-color
# @File : test
# @Project : svd_crawl
import scrapy


class IcanhazipSpider(scrapy.Spider):
    # class MavenSpider(scrapy.Spider):
    # 爬虫名 运行
    name = "mavenlib"
    # 允许访问的域名
    allowed_domains = ['mvnrepository.com']
    # 起始的url
    start_urls = ['https://mvnrepository.com/open-source']
    # name = 'icanhazip'
    # start_urls = ["https://myip.ipip.net"]

    def parse(self, response, **kwargs):
        print("???????????", response.text)
