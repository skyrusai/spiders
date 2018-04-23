# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

import random
from scrapy import signals
from quotesbot.settings import IPPOOL

class MyproxiesSpiderMiddleware(object):

      def __init__(self,ip=''):
          self.ip=ip
       
      def process_request(self, request, spider):
          thisip=random.choice(IPPOOL)
          print("this is ip:"+thisip["ipaddr"])
          request.meta["proxy"]="http://"+thisip["ipaddr"]