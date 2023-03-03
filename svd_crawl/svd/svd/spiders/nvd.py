import scrapy
from svd.items import NvdItem, DetailItem


class NvdSpider(scrapy.Spider):
    name = "nvd"
    allowed_domains = ["nvd.nist.gov"]
    start_urls = ["http://nvd.nist.gov/vuln/full-listing/"]

    def parse(self, response):
        li_list = response.xpath('//*[@id="body-section"]/div/span/ul/li')
        for li in li_list:
            href = li.xpath('./a/@href').get()
            # print(response.urljoin(href)) # 自动拼接URL
            # cve_date = href.split('/')[-2:-1]
            # cve_date = href.split('/')[-2] + "__" + href.split('/')[-1]

            # 处理href为请求 交给引擎
            yield scrapy.Request(
                url=response.urljoin(href),  # 自动拼接URL
                method='get',
                callback=self.parse_riqi  # 返回数据的解析函数  回调函数
            )
            # break

    def parse_riqi(self, response):
        cve_date = response.url.split('/')[-2] + '_' + response.url.split('/')[-1]
        span_list = response.xpath('//*[@id="body-section"]/div[2]/div[2]/span')
        # i = 0
        for span in span_list[:3]:
            # i = i + 1
            # cve_id = span.xpath('./a/text()').get()
            cve_url = "http://nvd.nist.gov" + span.xpath('./a/@href').get()
            # print(cve_id + "==" + cve_url)

            #  # 传递给管道
            # cve = NvdItem()  # 相当于字典 key钉死
            # cve['cve_name'] = cve_id
            # cve['cve_url'] = cve_url
            # cve['cve_date'] = cve_date
            # yield cve

            yield scrapy.Request(
                url=cve_url,
                callback=self.parse_detail
            )
            # if i == 5:
            #     break

    def parse_detail(self, response):
        # CVE
        cve_name = response.url.split('/')[-1]
        # 描述
        cve_desc = response.xpath('//*[@id="vulnDetailTableView"]/tr/td/div/div[1]/p/text()').get()
        # 分数
        cve_nist_score = response.xpath('//*[@id="Cvss3NistCalculatorAnchor"]/text()').get()
        cve_cna_score = response.xpath('//*[@id="Cvss3CnaCalculatorAnchor"]/text()').get()
        # 相关链接
        cve_referer_trs = response.xpath('//*[@id="vulnHyperlinksPanel"]/table/tbody/tr')
        cve_referer = ""
        for tr in cve_referer_trs:
            cve_referer = tr.xpath('./td[1]/a/text()').get() + "; " + cve_referer
        # 漏洞类型
        cve_type = response.xpath('//*[@id="vulnTechnicalDetailsDiv"]/table/tbody/tr/td[1]/a/text()').getall()

        # 发布时间
        cve_public = response.xpath('//*[@id="vulnDetailTableView"]/tr/td/div/div[2]/div/span[1]/text()').get()
        # 最后一次修改时间
        cve_last_modified = response.xpath('//*[@id="vulnDetailTableView"]/tr/td/div/div[2]/div/span[2]/text()').get()

        cve = DetailItem()
        cve['cve_name'] = cve_name
        cve['cve_url'] = response.url
        cve['cve_desc'] = cve_desc
        cve['cve_nist_score'] = cve_nist_score
        cve['cve_cna_score'] = cve_cna_score
        cve['cve_referer'] = cve_referer
        cve['cve_type_id'] = str(cve_type)
        cve['cve_public'] = cve_public
        cve['cve_last_modified'] = cve_last_modified

        yield cve
