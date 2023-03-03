import scrapy
from scrapy.linkextractors import LinkExtractor
from svd.items import CweItem
class CweSpider(scrapy.Spider):
    name = "cwe"
    allowed_domains = ["www.cvedetails.com"]
    start_urls = ["http://www.cvedetails.com/cwe-definitions/1/cwelist.html?order=2&trc=668&sha=0427874cc45423ccb6974ee25935fbfceac76fcb"]

    def parse(self, response):
        # print(response.text)
        # le = LinkExtractor(restrict_xpaths='//*[@id="searchresults"]/table/tr')

        trs = response.xpath('//*[@id="searchresults"]/table/tr')
            # le.extract_links(response)
        # print(trs)
        i = 0
        cwe = CweItem()
        for tr in trs:
            if i == 0 :
                i =1
                continue
            cwe_id = "CWE-" + tr.xpath('./td[1]/a/text()').get()
            cwe_name = tr.xpath('./td[2]/text()').get()
            cwe['cwe_id'] = cwe_id.strip()
            cwe['cwe_name'] = cwe_name.strip()
            yield cwe
        le = LinkExtractor(restrict_xpaths='//*[@id="pagingb"]/a')
        links = le.extract_links(response)
        for link in links:
            # print("page:" + link.url)
            yield scrapy.Request(
                url=link.url,
                # dont_filter=False,
                callback=self.parse
            )

        # pass
