#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 10:02:28 2018

@author: mac-pro
"""

import json,pickle
import pymysql

def to_generator(lst):
    for i in lst:
        yield i

f = open('item_list.pickle','rb')
item_list = pickle.load(f)
f.close()
#print(item_list[:50])

item_ge = to_generator(item_list)

#print(len(item_list))
#print(type(item_ge))
#
#for i in item_ge:
#    print(i)

conn = pymysql.connect(host='localhost',user='root',
                       passwd='mac65512802dqx',
                       local_infile=True,charset='utf8')

cur = conn.cursor()
cur.execute('CREATE DATABASE IF NOT EXISTS career')
cur.execute('USE career')
cur.execute('DROP TABLE IF EXISTS main_table')
cur.execute('CREATE TABLE  main_table \
            (id int PRIMARY KEY AUTO_INCREMENT,地区 varchar(100),学校代码 varchar(100),学校名称 varchar(100),层次 varchar(100),专业类别 varchar(200),\
            专业 varchar(500), 科目要求 varchar(200),学校网站 varchar(500), sub_type int,sub varchar(100))')
conn.commit()

cur.execute('truncate main_table')
conn.commit()

i = 1
for dic in item_ge:
    region = dic['region']
    identify = dic['identify']
    name = dic['name']
    level = dic['level']
    cate = dic['cate']
    skill = dic['skill']
    sub= dic['sub']
    school_url = dic['school_url']
    sub_type = dic['sub_type']
    sub_con = dic['sub_con']
    row = [i,region,identify,name,level,cate,skill,sub,school_url,sub_type,sub_con]
#    print(row)
    cur.execute('INSERT INTO main_table \
                    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',row)
    i += 1
#    if i == 10:
#        break
    print(i)
    conn.commit()








