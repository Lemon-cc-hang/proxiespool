# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:       getHtml.py
   Description :
   Author :         lemoncc
   date:            2020/7/14
-------------------------------------------------
"""
__author__ = 'lemoncc'

import requests
from random import choice
from requests.models import Response
import time
from helper.common import common


class GetHtml(object):

	def __user_agent(self):
		ua_list = [
			'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101',
			'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122',
			'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71',
			'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95',
			'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71',
			'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
			'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
			'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
		]
		return choice(ua_list)

	def __header(self):
		return {'User-Agent': self.__user_agent(),
		        'Accept': '*/*',
		        'Connection': 'keep-alive',
		        'Accept-Language': 'zh-CN,zh;q=0.8'}

	def getProxies(self):
		if common.dbClient.getNumber() > 100:
			proxies = common.dbClient.get_proxies(10)
			if proxies is None:
				return None
			else:
				return choice(proxies)
		else:
			return None

	def get(self, url, retry_time=3, retry_interval=5, timeout=5, *args, **kwargs):
		headers = self.__header()
		while True:
			proxies = self.getProxies()
			common.logs.proxies_info(proxies)
			try:
				common.logs.scrap_info(url)
				html = requests.get(url, headers=headers, timeout=timeout, proxies=proxies, *args, **kwargs)
				if html.status_code == 200:
					common.dbClient.insert(proxies)
					return html
				else:
					common.dbClient.score_sub(proxies)
					common.logs.retry_info(retry_interval)
					time.sleep(retry_interval)
					self.get(url)

			except Exception:
				common.dbClient.score_sub(proxies)
				common.logs.scrap_error(url)
				retry_time -= 1
				if retry_time <= 0:
					resp = Response()
					if resp.status_code == 200:
						return resp
					else:
						common.logs.retry_info(retry_interval)
						time.sleep(retry_interval)
						self.get(url)
