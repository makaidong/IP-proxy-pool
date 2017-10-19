# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
from ip2.settings import USER_AGENT_LIST
from ip2.settings import PROXIES
import base64


class Ip2SpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)



# 定一个中间件类
class RandomUserAgentMiddleware(object):

    def process_request(self, request, spider):
        # 随机获取一个用户头
        user_agent = random.choice(USER_AGENT_LIST)
        # print (user_agent)
        # 设置请求头
        request.headers['User-Agent'] = user_agent

# 定一个一个随机ip代理中间件类
class RandomIpProxyMiddleware(object):

    def process_request(self, request, spider):
        # 随机获取一个代理
        proxy = random.choice(PROXIES)
        # print (proxy)
        # 判断是否为私密代理
        # if proxy.has_key('user_passwd')
        if 'user_passwd' in proxy:
            # 私密代理处理
            # 对账号密码进行编码
            # python3中进行编码需要bytes类型的数据，python2中不需要
            b64_user_pwd = base64.b64encode(proxy['user_passwd'].encode())
            # print (b64_user_pwd)

            # 设置代理认证
            request.headers['Proxy-Authorization'] = "Basic " + b64_user_pwd.decode()

            # 使用IP代理
            request.meta['proxy'] = "http://" + proxy['ip_port']

        else:
            # 免费代理处理
            request.meta['proxy'] = "http://" + proxy['ip_port']



