# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:       verify.py
   Description :
   Author :         lemoncc
   date:            2020/7/14
-------------------------------------------------
"""
__author__ = 'lemoncc'


import requests
from concurrent.futures import ThreadPoolExecutor
from helper.common import common


class Verify(object):

	def __verify_proxy(self, proxies):
		html = requests.get('http://www.baidu.com', proxies=proxies, timeout=3)
		try:
			if html.status_code == 200:
				common.logs.store_info(proxies)
				common.dbClient.insert(proxies)
			else:
				common.dbClient.score_sub(proxies)
		except:
			common.dbClient.score_sub(proxies)
			common.logs.verify_warning(proxies)

	def verify_ip(self, proxies):
		common.logs.verify_info(proxies)
		with ThreadPoolExecutor(max_workers=50)as t:
			for proxy in proxies:
				t.submit(self.__verify_proxy, proxy)
