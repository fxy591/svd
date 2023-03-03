# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SvdItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    group_id = scrapy.Field()
    artfact_id = scrapy.Field()
    version = scrapy.Field()
    cve_id = scrapy.Field()

class CweItem(scrapy.Item):
    cwe_id = scrapy.Field()
    cwe_name = scrapy.Field()

class NvdItem(scrapy.Item):
    cve_name = scrapy.Field()
    cve_url = scrapy.Field()
    cve_date = scrapy.Field()

class DetailItem(scrapy.Item):
    cve_desc = scrapy.Field()
    cve_nist_score = scrapy.Field()
    cve_cna_score = scrapy.Field()
    cve_referer = scrapy.Field()
    cve_type_id = scrapy.Field()
    cve_public = scrapy.Field()
    cve_last_modified = scrapy.Field()
    cve_name = scrapy.Field()
    cve_url = scrapy.Field()