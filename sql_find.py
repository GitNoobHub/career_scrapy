#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 18:20:21 2018

@author: mac-pro
"""

import pymysql

conn = pymysql.connect(host='localhost',user='root',
                       passwd='mac65512802dqx',
                       local_infile=True,charset='utf8')

my_sub = ['物理','化学','政治']



#select distinct sub from main_table where (sub_type = 1 and find_in_set(sub,'地理,生物,政治')) 
#or 
#(sub_type=0  and (find_in_set(substring_index('地理,生物,政治',',',1) , sub) 
#or 
#find_in_set(substring_index(substring_index('地理,生物,政治',',',-2),',',1) , sub) or 
#find_in_set(substring_index('地理,生物,政治',',',-1) , sub)));

#select * from main_table where (sub_type = 1 and find_in_set(sub,'地理,生物,政治')) 
#or 
#(sub_type=0  and (sub REGEXP '地理|生物|政治') and (sub != '化学,历史,地理,政治,物理,生物'));
#
#select distinct sub, sub_type from main_table where (sub_type = 1 and find_in_set(sub,'地理,生物,政治')) 
#or 
#(sub_type=0  and (sub REGEXP '地理|生物|政治') and (sub != '化学,历史,地理,政治,物理,生物'));

select distinct sub, sub_type from main_table where (sub_type = 1 and find_in_set(sub,'地理,生物,政治'))  or  (sub_type=0  and (sub REGEXP '地理|生物|政治') and (sub != '化学,历史,地理,政治,物理,生物'));


select distinct sub, sub_type from main_table where (sub_type = 1 and '地理,生物,政治' REGEXP '^.*(%s).*$')  or  (sub_type=0  and (sub REGEXP '地理|生物|政治') and (sub != '化学,历史,地理,政治,物理,生物'));

