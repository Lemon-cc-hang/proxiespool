# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:       finish_.py
   Description :
   Author :         lemoncc
   date:            2020/7/14
-------------------------------------------------
"""
__author__ = 'lemoncc'

from helper.common import common
from helper.verify import Verify


class Finish_(object):

	def __init__(self):
		self.verify_ip = Verify().verify_ip

	def run(self):
		proxies = common.dbClient.getAll()
		self.verify_ip(proxies)
		common.logs.finish_info(common.dbClient.getNumber())