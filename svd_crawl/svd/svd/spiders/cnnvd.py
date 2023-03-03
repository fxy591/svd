import json

import jsonpath as jsonpath
import scrapy


class CnnvdSpider(scrapy.Spider):
    name = "cnnvd"
    allowed_domains = ["www.cnnvd.org.cn"]
    start_urls = ["https://www.cnnvd.org.cn/web/cnnvdVul/getCnnnvdDetailOnDatasource"]
    header = {
        'Referer': 'https://www.cnnvd.org.cn/home/loophole',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    }
    formdata = {"cveCode": "CVE-2023-26234"}
    def start_requests(self):
        yield scrapy.Request(
            url=self.start_urls[0],
            method='post',
            headers=self.header,
            body=json.dumps(self.formdata),
            callback=self.parse
        )


    def parse(self, response):
        vul_name = response.text
        # vul_name = jsonpath.jsonpath(response.text, '$.vulName')
        with open('xxx.txt', 'w', encoding="utf-8") as f:
            f.write(response.text)
        print(vul_name)
        pass
# {
#     "version": "version 1.0.12",
#     "result": {
#         "pages": 1314,
#         "data": [
#             {
#                 "name": "大明",
#                 "IDcard": "440588190001015688",
#                 "address": "广东省广州市天河区正佳广场99楼520号",
#             },
#             {
#                 "name": "二明",
#                 "IDcard": "440588190012317456",
#                 "address": "广东省广州市天河区天环广场88楼520号",
#             }
#         ]
#     }
# }
# {
#     "code": 200,
#     "success": true,
#     "message": "操作成功",
#     "data": {
#         "cnnvdDetail": {
#             "id": null,
#             "vulName": "JD-GUI 安全漏洞",
#             "cnnvdCode": "CNNVD-202302-1638",
#             "cveCode": "CVE-2023-26234",
#             "publishTime": "2023-02-21 00:00:00",
#             "isOfficial": 1,
#             "vendor": null,
#             "hazardLevel": null,
#             "vulType": "其他",
#             "vulTypeName": "其他",
#             "vulDesc": "JD-GUI是Java Decompiler开源的一个独立的图形实用程序。显示 CLASS 文件中的 Java 源代码。\r\nJD-GUI 1.6.6版本存在安全漏洞，该漏洞源于该程序允许攻击者通过 UIMainWindowPreferencesProvider.singleInstance 进行反序列化。",
#             "affectedProduct": null,
#             "affectedVendor": null,
#             "productDesc": null,
#             "affectedSystem": null,
#             "referUrl": "来源:MISC\r\n链接:https://github.com/java-decompiler/jd-gui/issues/415\r\n\r\n来源:MISC\r\n链接:https://github.com/java-decompiler/jd-gui/pull/417",
#             "patchId": null,
#             "patch": "https://github.com/java-decompiler/jd-gui/pull/417",
#             "deleted": null,
#             "version": null,
#             "createUid": null,
#             "createUname": null,
#             "createTime": null,
#             "updateUid": null,
#             "updateUname": null,
#             "updateTime": "2023-02-21 00:00:00",
#             "cnnvdFiledShow": "vul_name,cnnvd_code,_code,publish_time,is_official,vendor,hazard_level,vul_type,vul_desc,affected_product,affected_vendor,product_desc,affected_system,refer_url,patch_id,product,update_time,patch",
#             "cveVulVO": null,
#             "cveFiledShow": null,
#             "ibmVulVO": null,
#             "ibmFiledShow": null,
#             "icsCertVulVO": null,
#             "icsCertFiledShow": null,
#             "microsoftVulVO": null,
#             "microsoftFiledShow": null,
#             "huaweiVulVO": null,
#             "huaweiFiledShow": null,
#             "nvdVulVO": null,
#             "nvdFiledShow": null,
#             "varchar1": "其他"
#         },
#         "receviceVulDetail": null
#     },
#     "time": "2023-02-22 11:19:30"
# }