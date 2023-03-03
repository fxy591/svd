# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
from svd.settings import MYSQL
from svd.items import CweItem, SvdItem, NvdItem, DetailItem
import cx_Oracle



class SvdPipeline:
    def open_spider(self, spider):
        self.conn = cx_Oracle.connect('svd','123456','localhost:1521/ORCL')


    def close_spider(self, spider):
        if self.conn:
            self.conn.close()

    # 方法名 必须为process_item(self, item, spider)process_item(self, item, spider)
    def process_item(self, item, spider):  # 处理数据的专用方法 不能改 收数据 =》 item   爬虫=》spider

        if isinstance(item, CweItem):
            # print(item['cwe_id']+item['cwe_name'])
            # 写文件/数据库/脑补
            try:
                print(item)
                cursor = self.conn.cursor()
                # print('连接数据库成功！')
                # sql = "select * from SVD_CWE"
                # cursor.execute(sql)
                # data = cursor.fetchone()
                # print(data)
                sql = "insert into SVD_CWE values (:cwe_id, :cwe_name)"
                cursor.execute(sql, (item['cwe_id'], item['cwe_name']))
                self.conn.commit()
            except Exception as e:
                print("错误：{}".format(e))
                print("5454")
                self.conn.rollback()
            finally:
                if cursor:
                    cursor.close()
            return item  # 进入下一个管道


        if isinstance(item, SvdItem):
            # print(item['cwe_id']+item['cwe_name'])
            # 写文件/数据库/脑补
            try:
                cursor = self.conn.cursor()
                # print('连接数据库成功！')
                # sql = "select * from SVD_CWE"
                # cursor.execute(sql)
                # data = cursor.fetchone()
                print(item)
                print(type(str(item['cve_id'])))
                sql = "insert into SVD_COMPONENT_INFO (group_id, artifact_id, version, cve_id) values (:group_id, :artifact_id, :version, :cve_id)"
                cursor.execute(sql, (item['group_id'], item['artifact_id'], item['version'], str(item['cve_id'])))
                self.conn.commit()
            except Exception as e:
                print("错误：{}".format(e))
                self.conn.rollback()
            finally:
                if cursor:
                    cursor.close()
            return item  # 进入下一个管道

        # if isinstance(item, NvdItem):
        #     print(item)
        #     try:
        #         cursor = self.conn.cursor()
        #         sql = "insert into SVD_CVE_LIST (CVE_NAME, CVE_URL) values (:CVE_NAME, :CVE_URL)"
        #         cursor.execute(sql, (item['CVE_NAME'], item['CVE_URL'], item['version'], str(item['cve_id'])))
        #         self.conn.commit()
        #     except Exception as e:
        #         print("错误：{}".format(e))
        #         self.conn.rollback()
        #     finally:
        #         if cursor:
        #             cursor.close()
        #     return item

        if isinstance(item, DetailItem):
            print(item)
            try:
                cursor = self.conn.cursor()
                sql = "insert into SVD_CVE_LIST (CVE_NAME, CVE_URL, CVE_CNA_SCORE, CVE_NIST_SCORE, CVE_DESC, CVE_PUBLIC, CVE_LAST_MODIFIED, CVE_TYPE_ID, CVE_REFERER) values (:CVE_NAME, :CVE_URL, :CVE_CNA_SCORE, :CVE_NIST_SCORE, :CVE_DESC, :CVE_PUBLIC, :CVE_LAST_MODIFIED, :CVE_TYPE_ID, :CVE_REFERER)"
                cursor.execute(sql, (item['cve_name'], item['cve_url'], item['cve_cna_score'], item['cve_nist_score'], item['cve_desc'], item['cve_public'], item['cve_last_modified'], item['cve_type_id'], item['cve_referer']))
                self.conn.commit()
            except Exception as e:
                print("错误：{}".format(e))
                self.conn.rollback()
            finally:
                if cursor:
                    cursor.close()
            return item