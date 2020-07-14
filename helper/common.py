# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:       common.py
   Description :
   Author :         lemoncc
   date:            2020/7/14
-------------------------------------------------
"""
__author__ = 'lemoncc'

from db.dbClient import DbClient
from helper.logs import Logs
from config import dbConfig


class Common(object):

	def __init__(self, **kwargs):
		self.logs = Logs()
		self.dbClient = DbClient(**kwargs)


common = Common(**dbConfig)