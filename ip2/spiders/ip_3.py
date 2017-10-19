# -*- coding: utf-8 -*-
import scrapy
import requests
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import json


class Ip3Spider(CrawlSpider):
    name = 'ip_3'
    allowed_domains = ['kuaidaili.com']
    start_urls = ['http://www.kuaidaili.com/free/']

    rules = (
        # 下一页
        Rule(LinkExtractor(allow=r'/free/inha/\d+?/'), callback='parse_item', follow=True),
        #
    )

    def parse_item(self, response):
        # print(response, '--------*************----------')
        node_list = response.xpath('//*[@id="list"]/table/tbody/tr')
        for node in node_list:
            ip = node.xpath('./td[1]/text()').extract_first()
            post = node.xpath('./td[2]/text()').extract_first()
            self.get_page(ip, post)
            # print(ip, ':', post, '-------************--------')

    def get_page(self, ip, post):
        '''发送请求测试ip'''
        url = 'https://www.oschina.net/'
        proxies = {
            'http': 'http://' + ip + ':' + post
            # 'http': 'http://220.166.242.8:8118'
        }
        # 这只要状态码，反扒并不重要
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER',
        }
        data_list = [',\n']
        try:
            ip_text = requests.get(url, headers=headers, timeout=0.5, proxies=proxies)
            # print('------************---------')
            if ip_text.status_code == 200:
                # data = {'http': 'http://' + ip + ':' + post} + ',\n'
                # str_data = json.dumps(dict(data), ensure_ascii=False) + ',\n'
                data = "'http': 'http://" + ip + ':' + post + "'" + ',\n'
                data_list.append(data)
                print(ip)
            self.save_data(data_list)
        except:
            pass

    def save_data(self, data):
        # 打开存储数据的文件
        print(data)
        file = open('ip.txt', 'w')
        file.write(data)
        file.close()
