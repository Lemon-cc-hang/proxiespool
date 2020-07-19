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


dbConfig = {
	'db_host':'localhost',
	'db_port': 27017,
	'db_user': None,
	'db_pwd': None,
	'db_maxData': 10000,
	'db_table': 'proxiesPool',
	'maxPoolSize': None
}

class BaseConfig(object):
	DEBUG = False
	TESTING = False

flaskApiConfig = {
	'host': 'localhost',
	'port': 5000
}