import scrapy
from svd.request import SeleniumRequest
from scrapy.linkextractors import LinkExtractor
import time
from svd.items import SvdItem
class MavenSpider(scrapy.Spider):
    # 爬虫名 运行
    name = "maven"
    # 允许访问的域名
    allowed_domains = ['mvnrepository.com']
    # 起始的url
    start_urls = ['https://mvnrepository.com/open-source']  # 后缀为HTMl结尾 不需要加/

    def start_requests(self):  # 控制爬虫发出的第一个请求
        # 登陆流程
        header={
            # 'Referer': 'https://mvnrepository.com/?__cf_chl_tk=oE1UfOeRlIuT_.tLOs2prnbBZiC_7SKGeX524yscfNg-1677030554-0-gaNycGzNCfs',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
        }
        # data='md=7dwN0ikvz4_uQAll.VrQ6anzrK1CbFsmNSRvgawhkrE-1677030554-0-ASXXMlA9bxFyFR-vQBQmbQHDG7S4Gnd0O-aVJ9IBbxyXXjDgTOvzT3Wtusq5J5QwuSKYJu05qFC0rduUKVr3LYbqr_7_vC2_omjy6QvW9niu1zqp7T7XuLu2TKnvq5EdCEKDzCnV0zsqDS0wABKzPy9UtPZv5qJKxQTc4hhBwA4Xbj_V_E7ySpJ5qFz9kxi0Wob1x9EpJNFdOSEpaCMCoyqj5Okur5e3xU2-vpYxFiIIyHrHeK_ARUEnAGlMOzHINhqMfaCjrEnbYV-u9VOblkzSFs12nJnQ_0bExIksnr--bW0KbbytZ3yweZngIibT08FtKna79jqUZSkS_wWVyJ4Vlvku1dWJjHhUEj0ApwA7s4LZq2VGajtpqXokJlV46GOYDKBJYN-rDWgal_1KHQs1XLif-vYOgRRIbGs3oZqEouFiDdX3YWHK_yjlhg4iREC8gdrd9cmOjEAbAWiWXykGYgtiNaptPOrYg4PDVB8w1NZpYxAfMElOKwjzTuOtu3uXiSRNvLpaF9I7zQlGhkdBOpJg3a_QLnTJzd6qSKTa1KaIJw008ZJFEfM4hb6ig28rUeZPiWg8dJQm21N1Z9_SBGcpwUp0eFGpFCaql_4RptYHlxUI69YYNiEXilK4-5r-SLwD5XbsoM0ufGvgNvIkh2MpZbqGS6WaIC_EP22JLnSPDQDmo2b-0UpmJSdV_l_30q5D-bGI3gJ6aoqeogvulMSbRbq_T9G84dN5ZpxtQvXWKs3-9PCH2RJfKGbDPLSeATkfaWTILV-2fbDnexvYOy7dKDagwXBx-cgzOpUwrToSaq6Xm1ZNRaAj_-sJksK5MibSIxVjTlX1losMjrutJ7BjhNJbf1Bb_KyjKHb0gStCJPDEr9B7hajX9BlBf3M7zRKxYJFBdsvNJUoh5DtHxPs5gZkXt_itNNcYmag9dqs4uXQ2qGcKnAq7k8UXs3-jiwTLEJEyPdUU9Wi74fJhNVi1LdBED0Zt3rvvXXh8sofDGmzMgU9zv8_ot-NWIjBkUC19P4kYeM4RRCypyBfl5DqLJf5gLcdlug4H_3bqo3uiEKY4T-eQKmh_zSAr1dESqodrMEOdSbGAF0qRFueboO8muOVJYmIRu2SLyFYwYLqL0egbKA2OqDCD9t6Q84ZIMvUbFLmsIVhZSUKsxOY073kZ94Nw_jldeqZtoMvro_5QOuj55uzRxCaIKpuJTtzrafafir7kq1gWH0aywHTKcSV6on7lFiDkqW2v2IiW-Fz0QAbxdMsWytTb8qzZHbjo1uXb75VugVZd55fxwIMuWEGKMLTvwMaYeq5o8dsE6SoIXFcUZzAK3dKEkzz7kNbn_uie27V0n2s6BiuBcPnqbL3RhEJIVhIGLZp_Fg6kwlTPTcRPdmUfBZItte6ePs1nCpeuhkiiY6v47qoevquIZIeLyNzm10actPvevNH-sFkxE2bE3uPbtlwBN9P0J2Z7klPSE1SYH8iqMGfrs3SBwh55LIFuEIur-WOqO_cvavZj6bV-GJ1Hq9a05REuJVANoJEADHzn8J_8y7ljoTgNOid8pKb7UD6F7QhqjAfuuCZ0rMocefFQdeAT2WQUDnc49rlHaBOA3CymJodpbJorvl5T4SMMLDZUQwTgV-RzxzHsF4ZN5TEEgmEUsIgSVy0rJU1VJMduPgogtgMvNkbM38LPNhXoChs-Bpj8BFysYfmpdJ0JdaSoxvdmCN1mAwR-AfwmVo7nhJxRFa0POLyp28J1PB5ckLRSIjayOULbbCWNN7Z8L5H8G0e5jwr5bXPteos-JPky6ErarmP5ra9HjOXH9YoaQI-OcXBEC5tHPaj39GNbJs2NecgS77bEdVvZG4A1lFpDewQjAw5Dccs5wBAxMYCh0L2WbiBgBgsq5XLy52U3yGlnlRw8n-D328TGQytMbVb71u_Rp-jIJ6LUO_NzOiU1rdu9iINirO_x1WSzpK2U54TK5uLBzFRm-yds04y47gpMTOff7KqCYUiQNdV9Cja9VIUy2L3iKQqfQz9XwneBXt1liXvk__FhGa5sSDVR7w6uYfBZW3cMB9xNNNT7GqyZVtTBeivyz_sgVIFX3reqYqc1wrvhPsK2aotG6FB4fB6iK3YFQf2mdZHwnBBNgxvpvb1kN5lAHIlc1T74xc1dn5OWqyhhz_UU7vtn7QSH7oP5XoFPrbZKM8OAdcS7rN7AAij_Rkp47nTuW6Uw2K5rsKoVUccbV0Pllold9DoiDukivQodz15QP2SXi2zOLyuHGrfSM7OVWTyFGyp6RlZ2x0i5tOzGisCTb2aOzipM9hCceCdnt5ECP6nYKhDdG-3vIVrgLaPc88-4yOVrKVhG9hTRA5zE2Lew5YwSt4mkj0pCB3XPjYjRtpIkZY5v9MREW6FgblmfoL8V6wPjAfVVEJwDSFkkBBBxfBtTB9j-Pr3Xncp_BbBMfcLo0gpkf5pndtSnAxmCJ8cb5UzJeeRf5T59MbCzHcrK4w&sh=9ae87706b4444d6d680c3b4fedd45a59&aw=fzceiyiNRpbc-15-79d410636b999860&cf_ch_cp_return=6451717e085a50219aca297585d407ab%7C%7B%22managed_clearance%22%3A%22ni%22%7D'

        # yield scrapy.Request(
        #     url=self.start_urls[0],
        #     # method='post',
        #     headers=header,
        #     # body=data,
        #     callback=self.parse
        # )
        # 通过selenium对open-source进行请求
        yield SeleniumRequest(
            url=self.start_urls[0],
            # callback=self.parse_home
            # callback=self.parse_version
            # method = 'post',
            headers = header,
            # body = data,
            callback=self.parse_open_source
        )
        # 之后进行parse解析即可

    # 对主页处理 获取每个分类的url并发送请求
    def parse_home(self, response):
        le = LinkExtractor(restrict_xpaths='/html/body/div/div/div[2]/div/ul/li/div/div[2]/a')
        links = le.extract_links(response)
        # i = 0
        for link in links:

            print("home:" + link.url)
            # time.sleep(10)
            yield SeleniumRequest(
                url=link.url,
                callback=self.parse_categories
            )
            break

    def parse_open_source(self, response):
        # 获取每个分类的链接
        le = LinkExtractor(restrict_xpaths='/html/body/div/main/div[1]/div/h4/a')
        links = le.extract_links(response)
        for link in links:
            print("home:" + link.url)
            # time.sleep(10)
            # 对每个链接进行请求
            yield SeleniumRequest(
                url=link.url,
                # callback=self.parse_component1
                callback=self.parse_categories
            )

        # 获取分页链接
        le2 = LinkExtractor(restrict_xpaths='/html/body/div/main/div[1]/ul/li/a')
        links2 = le2.extract_links(response)
        for link in links2:
            print("source page:" + link.url)
            time.sleep(3)
            # 对每个分页进行相同的操作
            yield SeleniumRequest(
                url=link.url,
                callback=self.parse_open_source
            )

    # 对分类进行处理
    def parse_categories(self, response):
        # 获取组件链接
        le = LinkExtractor(restrict_xpaths='/html/body/div/main/div[1]/div/div[1]/h2/a[1]')
        links = le.extract_links(response)
        for link in links:
            print("cate:" + link.url)
            # time.sleep(10)
            # 对每个组件进行请求
            yield SeleniumRequest(
                url=link.url,
                callback=self.parse_tag
                # callback=self.parse_component
            )
            # break

        # 分页处理
        le2 = LinkExtractor(restrict_xpaths='/html/body/div/main/div[1]/ul/li/a')
        links2 = le2.extract_links(response)
        for link in links2:
            print("page:" + link.url)
            time.sleep(3)
            yield SeleniumRequest(
                url=link.url,
                callback=self.parse_categories
            )
            # i = i + 1
            # if i == 2:
            #     break
            # break

    # test
    def parse_component(self, response):
        print("进来了" + response.url)

    # 标签
    def parse_tag(self, response):
        # 获取个标签的链接
        le = LinkExtractor(restrict_xpaths='//*[@id="snippets"]/ul/li/a')
        links = le.extract_links(response)

        for link in links:
            # 如果是第一个标签
            if response.url == link.url:
                print("tags:" + link.url)
                # self.parse_component2(response)
                # 提取 有问题的版本
                le1 = LinkExtractor(restrict_xpaths='//*[@id="snippets"]/div/div/div/table/tbody/tr/td[2]/a')
                links1 = le1.extract_links(response)
                for link1 in links1:
                    print("version:" + link1.url)
                    time.sleep(2)
                    # 对版本处理
                    yield SeleniumRequest(
                        url=link1.url,
                        callback=self.parse_version
                    )
                    # break
            # 如果是其他标签
            else:
                print("tags:" + link.url)
                yield SeleniumRequest(
                    url=link.url,
                    callback=self.parse_component
                )
                # break

        # break

    # 有问题的版本
    def parse_component(self, response):
        le = LinkExtractor(restrict_xpaths='//*[@id="snippets"]/div/div/div/table/tbody/tr/td[2]/a')
        links = le.extract_links(response)
        # i = 0
        for link in links:
            print("version:" + link.url)
            yield SeleniumRequest(
                url=link.url,
                callback=self.parse_version
            )
            # i = i + 1
            # if i == 2:
            #     break
            # break

    # 版本详情页
    def parse_version(self, response):
        svd = SvdItem()
        str = response.url.split("/")

        svd['group_id'] = str[-3]
        svd['artfact_id'] = str[-2]
        svd['version'] = str[-1]
        print("parse_version")

        cves = response.xpath('/html/body/div/main/div[1]/table/tbody/tr[11]/td/span/a/text()').getall()
        svd['cve_id'] = cves
        yield svd
            # print(cves)

    # cve详情页
    # todo：爬取详情页   问题 多个库怎么合一块？ 或者不在中间件中调用，而是在这直接调用

    def parse(self, response):
        # content = response.text # 获取内容
        with open('xxx.txt', 'w', encoding='utf-8') as f:
            f.write(response.text)
        print("漏洞库爬取开始")
        print(response.text)
        print(response.xpath('/html/body/div/div/div[2]/div/ul/li[1]/div/div[2]/a/text()').get())