# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:       logs.py
   Description :
   Author :         lemoncc
   date:            2020/7/14
-------------------------------------------------
"""
__author__ = 'lemoncc'

import logging


class Logs(object):

	def __init__(self):
		filename = 'logs/scraping.log'
		filemode = 'w+'
		logging.basicConfig(level=logging.INFO,
		                    format='%(asctime)s-%(levelname)s:%(message)s')

	def verify_warning(self, str1):
		logging.warning('proxy is timeout unavailable %s', str1)

	def scrap_info(self, str1):
		logging.info('scraping %s', str1)

	def retry_info(self, str1):
		logging.info("retry %s second after" % str1)

	def scrap_error(self, str1):
		logging.error('error occurred while scraping %s', str1)

	def verify_info(self, str1):
		logging.info('verify proxy %s', str1)

	def finish_info(self, str1):
		logging.info('successful , the total number of proxies is %s', str1)

	def store_info(self, str1):
		logging.info('store into database %s', str1)

	def proxies_info(self, str1):
		logging.info('using proxy is %s', str1)
