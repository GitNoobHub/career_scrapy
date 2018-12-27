#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 16:33:05 2018

@author: mac-pro
"""
with open ('/Users/mac-pro/Desktop/proxy/result/alive_ip.txt','r') as f:
    ls = f.readlines()
    proxies = [x.strip('\n') for x in ls]

print(proxies)