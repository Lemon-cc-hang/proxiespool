# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:       config.py
   Description :
   Author :         lemoncc
   date:            2020/7/14
-------------------------------------------------
"""
__author__ = 'lemoncc'

# mongoDB设置
dbConfig = {
	'db_host':'localhost',
	'db_port': 27017,
	'db_user': None,
	'db_pwd': None,
	'db_maxData': 10000,
	'db_table': 'proxiesPool',
	'maxPoolSize': None
}

# Flask设置
class BaseConfig(object):
	DEBUG = False
	TESTING = False

flaskApiConfig = {
	# 改成自己的网络区段 或者 localhost
	'host': '0.0.0.0',
	'port': 5000
}

# 需要验证的网址
webConfig = 'http://www.baidu.com'