# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:       getPages.py
   Description :
   Author :         lemoncc
   date:            2020/7/14
-------------------------------------------------
"""
__author__ = 'lemoncc'

from helper.scheduler import scheduler
from bs4 import BeautifulSoup


class GetPages(object):

	def kuaidaili_pages(self):
		url = 'https://www.kuaidaili.com/free/inha/1/'
		html = scheduler.runGetHtml().get(url)
		soup = BeautifulSoup(html.text, 'html.parser')
		pages = soup.select('#listnav > ul > li > a')[-1].text
		return int(pages)

	def xiladaili_pages(self):
		return 2000

	def ip89_pages(self):
		return 50

	def ip3366_pages(self):
		return 7

	def jiangxianli_pages(self):
		return 25
