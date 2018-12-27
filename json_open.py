#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 19:05:47 2018

@author: mac-pro
"""

import json,pickle
import re


def sort_str(string):
    str_list=sorted(string.split(','))
    new_str = ','.join(str_list)
    return new_str


pattern = re.compile('[ \t\n\r\f\v]')
pattern2 = re.compile('<!--.*-->|<td.*?>|</td>')
pattern3 = re.compile('<br>')
pattern4 = re.compile('.*(?=\(.*\))')
#pattern3 = re.compile('([\u4e00-\u9fa5].*[\u4e00-\u9fa5])|')

with open('items.json','r') as f:
    item_list=json.load(f)

#sub_set = set()

for dic in item_list:
#    unic = i['region'].encode('unicode_escape').decode('gbk')
    dic['region'] = dic['region'].encode('latin-1').decode('gbk')
    dic['name'] = dic['name'].encode('latin-1').decode('gbk')
    for k,v in dic.items():
        string = ''
        if v==None:
            v = ''
        for s in v:
            if pattern.match(s):
                s = ''
            string += s
        dic[k] = string
    dic['skill'] = pattern2.sub('',dic['skill'])
    dic['skill'] = pattern3.sub(' ',dic['skill'])

#    print(dic['skill'])
    if dic['sub'] == '不提科目要求':
        dic['sub_type'] = 0
        dic['sub_con'] = sort_str('物理,化学,生物,政治,历史,地理')
    elif '其中一门' in dic['sub']:
        dic['sub_type'] = 0
        dic['sub_con'] = sort_str(pattern4.match(dic['sub']).group(0))
    elif '均需选考' in dic['sub'] or '必须选考' in dic['sub'] :
        dic['sub_type'] = 1
        dic['sub_con'] = sort_str(pattern4.match(dic['sub']).group(0))
#    sub_set.add((dic['sub_type'],dic['sub_con']))
        

#print(len(sub_set))

#print(item_list[100:200])

#print(dic)
#print(len(dic))
#school_set = []
#for x in dic:
#    if x['name'] not in school_set:
#        school_set.append(x['name'])
#
#print(len(school_set))

with open('item_list.pickle','wb') as f1:
    pickle.dump(item_list,f1)

