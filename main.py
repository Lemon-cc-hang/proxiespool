# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:       main.py
   Description :
   Author :         lemoncc
   date:            2020/7/9
-------------------------------------------------
"""
__author__ = 'lemoncc'

from spider.spider import Spider
from finish_.finish_ import Finish_
from helper.common import common, dbConfig

if common.dbClient.getNumber() <= dbConfig['db_maxData']:
	spider = Spider().run()
finish_ = Finish_().run()