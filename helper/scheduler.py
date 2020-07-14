# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:       scheduler.py
   Description :
   Author :         lemoncc
   date:            2020/7/14
-------------------------------------------------
"""
__author__ = 'lemoncc'

from spider.getHtml import GetHtml
from spider.parseHtml import ParseHtml


class Scheduler(object):
	def __init__(self):
		self.__getHtml = GetHtml()
		self.__parseHtml = ParseHtml()

	def runGetHtml(self):
		return self.__getHtml

	def runParseHtml(self):
		return self.__parseHtml


scheduler = Scheduler()