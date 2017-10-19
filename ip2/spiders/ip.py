# -*- coding: utf-8 -*-
import scrapy


class IpSpider(scrapy.Spider):
    name = 'ip'
    allowed_domains = ['xicidaili.com']
    start_urls = ['http://www.xicidaili.com/nn']

    def parse(self, response):
        ip = response.xpath('//*[@id="ip_list"]/tr[2]/td[2]/text()').extract()
        print(ip, '--------------****************------------')
        pass
