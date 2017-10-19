# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Ip2Spider(CrawlSpider):
    name = 'ip2'
    allowed_domains = ['xicidaili.com']
    start_urls = ['http://www.xicidaili.com/nn']

    rules = (
        Rule(LinkExtractor(allow=r'/nn/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # print(response, '----------**************----------')
        node_list = response.xpath('//*[@id="ip_list"]/tr')
        for node in node_list[1:]:
            time1 = node.xpath('td[7]/div/@title').extract_first().rstrip('秒')
            print(time1)
            # self.print_data(time1)






    def print_data(self, print_data):
        print(type(print_data))
        print(print_data)