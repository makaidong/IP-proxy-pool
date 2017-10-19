# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class Ip2Pipeline(object):
    def __init__(self):
        # 打开存储数据的文件
        self.file = open('ip.json','a')


    def process_item(self, item, spider):
        # 转换数据
        str_data = json.dumps(dict(item),ensure_ascii=False) + ',\n'
        self.file.write(str_data)

        return item


    def close_spider(self, spider):
        self.file.close()

