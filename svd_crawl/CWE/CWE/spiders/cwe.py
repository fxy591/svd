import scrapy
from scrapy.linkextractors import LinkExtractor

class CweSpider(scrapy.Spider):
    name = "cwe"
    allowed_domains = ["www.cvedetails.com"]
    start_urls = ["http://www.cvedetails.com/cwe-definitions/1/cwelist.html?order=2&trc=668&sha=0427874cc45423ccb6974ee25935fbfceac76fcb"]

    def parse(self, response):
        le = LinkExtractor(restrict_xpaths='//*[@id="searchresults"]/table/tbody/tr')
        trs = le.extract_links(response)
        i = 0
        for tr in trs:
            if i == 0:
                continue
            cwe_id = "CWE-" + tr.xpath('./td[1]/text()').get()
            cwe_name = tr.xpath('./td[2]/text()').get()
            print(cwe_id + ':' + cwe_name)

        # pass
