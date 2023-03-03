import scrapy
from nvd.items import NvdItem # 先导入包
import pymysql
from nvd.settings import MYSQL
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# from scrapy.linkextractors import LinkExtractor
#
class NvdlibSpider(scrapy.Spider):
    name = 'nvdlib'
    allowed_domains = ['nvd.nist.gov']
    start_urls = ['http://nvd.nist.gov/vuln/full-listing/']

    def parse(self, response):
        # 从数据库中获取数据
        # conn = pymysql.connect(
        #     host=MYSQL['host'],
        #     port=MYSQL['port'],
        #     user=MYSQL['user'],
        #     password=MYSQL['password'],
        #     database=MYSQL['database']  # 链接的数据库
        # )
        # cursor = conn.cursor()  # 创建游标
        # sql = "select cve_name from cve"
        # cursor.execute(sql)
        # cve_name_list = cursor.fetchall()
        # print(cve_name_list[-1][0])

        # 整体提取
        # 获取每个月的链接 http://nvd.nist.gov/vuln/full-listing/year/month
        # urls = response.xpath('//*[@id="body-section"]/div/span/ul/li/a/@href').getall()
        # # 拼接为整链接
        # for i in range(len(urls)):
        #     urls[i] = 'http://nvd.nist.gov/' + urls[i]
        #
        # print(urls)

        # 详细页面链接  http://nvd.nist.gov/vuln/detail/CVE-2022-39187   cve链接
        # cves_urls = response.xpath('//*[@id="body-section"]/div[2]/div[2]/span/a/@href')
        # cve编号 获取标签中的文本/text()
        # cves = response.xpath('//*[@id="body-section"]/div[2]/div[2]/span/a/text()').getall()


        # 分块提取 每月日期
        li_list = response.xpath('//*[@id="body-section"]/div/span/ul/li')
        for li in li_list:
            href = li.xpath('./a/@href').get()
            # print(response.urljoin(href)) # 自动拼接URL
            # cve_date = href.split('/')[-2:-1]
            # cve_date = href.split('/')[-2] + "__" + href.split('/')[-1]

            # 处理href为请求 交给引擎
            yield scrapy.Request(
                url=response.urljoin(href),   # 自动拼接URL
                method='get',
                callback=self.parse_riqi      # 返回数据的解析函数  回调函数
            )
            # 当回调结束后 会继续执行后面的代码
            # break

        # 链接提取器
        # le = LinkExtractor()

    # cve编号与详情页代码
    def parse_riqi(self, response):
        cve_date = response.url.split('/')[-2] + '_' + response.url.split('/')[-1]
        span_list = response.xpath('//*[@id="body-section"]/div[2]/div[2]/span')
        for span in span_list[:3]:
            cve_id = span.xpath('./a/text()').get()
            cve_url = "http://nvd.nist.gov" + span.xpath('./a/@href').get()
            print(cve_id + "==" + cve_url)
            # 准备字典
            # cve = {
            #     "name": cve_name,
            #     "url": cve_url
            # }
            # # 传递给管道
            cve = NvdItem()  # 相当于字典 key钉死
            cve['cve_name'] = cve_id
            cve['cve_url'] = cve_url
            cve['cve_date'] = cve_date
            yield cve
'''
            browser = webdriver.Safari()
            # 访问网址
            url = 'https://www.cnnvd.org.cn/home/loophole'
            browser.get(url)
            # time.sleep(20)
            input = browser.find_element(By.XPATH, '//*[@id="loudong"]/form/div[1]/div[2]/div/div/div/input')
            # buttom.click()
            input.send_keys(cve_id)
            time.sleep(2)
            buttum = browser.find_element(By.XPATH, '//*[@id="loudong"]/form/div[1]/div[2]/div/div/div/div')
            buttum.click()
            time.sleep(2)
            a = browser.find_element(By.XPATH, '//*[@id="loudong"]/form/div[2]/div/div[1]/div[1]/div/div[1]/button')
            a.click()
            time.sleep(5)
            # //*[@id="loudong"]/form/div[2]/div/div[1]/div/div[2]/div[2]/div/div/div[3]/div[2]/a/text()
            desc = browser.find_element(By.XPATH,
                                        '//*[@id="loudong"]/form/div[2]/div/div[1]/div/div[1]/div[2]/div/div[2]/div[2]/p[2]')
            print(desc.text.strip())
            time.sleep(2)
            browser.quit()


    def parse_detail(self, response):
        cve_id = response.url.split('/')[-1]
        cve_detail = response.xpath('//*[@id="vulnDetailTableView"]/tr/td/div/div[1]/p/text()').get()
        cve_nist_score = response.xpath('//*[@id="Cvss3NistCalculatorAnchor"]/text()').get()
        cve_cna_score = response.xpath('//*[@id="Cvss3CnaCalculatorAnchor"]/text()').get()
        cve_hyperlink_trs = response.xpath('//*[@id="vulnHyperlinksPanel"]/table/tbody/tr')
        cve_hyperlink = ""
        for tr in cve_hyperlink_trs:
            cve_hyperlink = tr.xpath('./td[1]/a/text()').get() + "; " + cve_hyperlink
        cve_type = response.xpath('//*[@id="vulnTechnicalDetailsDiv"]/table/tbody/tr')
        cve_type_id = ""
        cve_type_name = ""
        for tr in cve_type:
            cve_type_id = tr.xpath('./td[1]/a/text()').get() + "; " + cve_type_id
            cve_type_name = tr.xpath('./td[2]/text()').get() + "; " + cve_type_name

        # 涉及组件
        # //*[@id="vulnCpeTree"]/div  所有涉及组件
        # for 循环
        # ./table/tbody/tr 组件名 和 版本
        # ./td[1]  名 【2】 起  【3】 止

'''


