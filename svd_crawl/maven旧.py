import time

import scrapy
from mavenLib.request import SeleniumRequest
from scrapy.linkextractors import LinkExtractor
class MavenlibSpider(scrapy.Spider):
    # 爬虫名  运行
    name = 'mavenlib'
    # 允许访问的域名
    allowed_domains = ['mvnrepository.com']
    # 起始的url
    start_urls = ['https://mvnrepository.com/'] # 后缀为HTMl结尾 不需要加/
    def start_requests(self):  # 控制爬虫发出的第一个请求
        # 登陆流程
        # yield scrapy.Request(
        #     url=self.start_urls[0],
        #     method='post',
        #     callback=self.parse
        # )
        yield SeleniumRequest(
            url=self.start_urls[0],
            callback=self.parse_home
            # callback=self.parse_version
        )
        # 之后进行parse解析即可

    # 对主页处理 获取每个分类的url并发送请求
    def parse_home(self, response):
        le = LinkExtractor(restrict_xpaths='/html/body/div/div/div[2]/div/ul/li/div/div[2]/a')
        links = le.extract_links(response)
        for link in links:
            print("home:"+link.url)
            # time.sleep(10)
            yield SeleniumRequest(
                url=link.url,
                callback=self.parse_categories
            )
            break

    def parse_categories(self, response):
        le = LinkExtractor(restrict_xpaths='/html/body/div/main/div[1]/div/div[1]/h2/a[1]')
        links = le.extract_links(response)
        for link in links:
            print("cate:"+link.url)
            # time.sleep(10)
            yield SeleniumRequest(
                url=link.url,
                # callback=self.parse_component1
                callback=self.parse_component
            )

        le2 = LinkExtractor(restrict_xpaths='/html/body/div/main/div[1]/ul/li/a')
        links2 = le2.extract_links(response)
        for link in links2:
            print("page:"+link.url)
            yield SeleniumRequest(
                url=link.url,
                callback=self.parse_categories
            )

    # test
    def parse_component(self, response):
        print("进来了" + response.url)

    # 标签
    def parse_component1(self, response):
        le = LinkExtractor(restrict_xpaths='//*[@id="snippets"]/ul/li/a')
        links = le.extract_links(response)
        i = 0
        for link in links:
            i = i+1
            if response.url == link.url:
                print("tags:" + link.url)
                # self.parse_component2(response)
                le1 = LinkExtractor(restrict_xpaths='//*[@id="snippets"]/div/div/div/table/tbody/tr/td[2]/a')
                links1 = le1.extract_links(response)
                for link1 in links1:
                    print("version:" + link1.url)
                    time.sleep(2)
                    yield SeleniumRequest(
                        url=link1.url,
                        callback=self.parse_version
                    )
            else:
                print("tags:"+link.url)
                yield SeleniumRequest(
                    url=link.url,
                    callback=self.parse_component2
                )
            if i == 2:
                break

    # 有问题的版本
    def parse_component2(self, response):
        le = LinkExtractor(restrict_xpaths='//*[@id="snippets"]/div/div/div/table/tbody/tr/td[2]/a')
        links = le.extract_links(response)
        for link in links:
            print("version:"+link.url)
            yield SeleniumRequest(
                url=link.url,
                callback=self.parse_version
            )


    # 版本详情页
    def parse_version(self, response):
        print("parse_version")
        le = LinkExtractor(restrict_xpaths='/html/body/div/main/div[1]/table/tbody/tr[11]/td/span/a')
        links = le.extract_links(response)
        for link in links:
            print("cveId:"+link.url)
            # todo: 将坐标与cve编号存于数据库中


    # cve详情页
    # todo：爬取详情页   问题 多个库怎么合一块？ 或者不在中间件中调用，而是在这直接调用

    def parse(self, response):
        # content = response.text # 获取内容
        print("漏洞库爬取开始")
        print(response.text)
        print(response.xpath('/html/body/div/div/div[2]/div/ul/li[1]/div/div[2]/a/text()').get())
        # print("=====================")
        # print(content)
"""
nvd 获取链接
response.xpath('//*[@id="body-section"]/div[2]/span/ul/li/a/@href').getall()
nvd.nist.gov/ + vuln/full-listing/年/月


maven   403
其他数据库 不知道怎么看是不是Java组件
1. https://mvnrepository.com/        403   
2. 国家信息安全漏洞库   cnnvd 中文信息  补丁   URL找不到
3. 美国国家信息安全漏洞库  nvd 英文  找不到解决方案  不确定是哪个组件
4. 全球信息安全漏洞指纹库与文件检测服务
5. 中国国家工控系统行业漏洞库
6. 中国国家信息安全漏洞共享平台  cnvd  有些查询不到
7. Freebuf

"""