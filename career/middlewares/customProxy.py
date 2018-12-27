#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 16:42:24 2018

@author: mac-pro
"""

from career.middlewares.proxy import proxies
import random

class RandomProxy(object):
    def process_request(self,request,spider):
         proxy = random.choice(proxies)
         request.meta['proxy'] = 'http://{}'.format(proxy)