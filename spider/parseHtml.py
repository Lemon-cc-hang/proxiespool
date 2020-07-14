# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:       parseHtml.py
   Description :
   Author :         lemoncc
   date:            2020/7/14
-------------------------------------------------
"""
__author__ = 'lemoncc'

from bs4 import BeautifulSoup
from helper.verify import Verify


class ParseHtml(object):

	def __init__(self):
		self.verify_ip = Verify().verify_ip

	def parse_html_kuaidaili(self, html):
		if html is not None:
			soup = BeautifulSoup(html.text, 'html.parser')
			ips = soup.select('table tbody tr')
			proxies = []
			for line in ips:
				ip = line.select_one('td').text
				port = line.select('td')[1].text
				addr = f'http://{ip}:{port}'
				proxies.append({'http': addr, 'https': addr})
			self.verify_ip(proxies)

	def parse_html_xiladaili(self, html):
		if html is not None:
			soup = BeautifulSoup(html.text, 'html.parser')
			ips = soup.select('table tbody tr')
			proxies = []
			for line in ips:
				ip = line.select_one('td').text
				addr = f'http://{ip}'
				proxies.append({'http': addr,'https': addr})
			self.verify_ip(proxies)

	def parse_html_ip89(self, html):
		if html is not None:
			soup = BeautifulSoup(html.text, 'html.parser')
			ips = soup.select('.layui-table tbody tr')
			proxies = []
			for line in ips:
				ip = line.select_one('td').text.strip()
				port = line.select('td')[1].text
				addr = f'http://{ip}:{port}'
				proxies.append({'http': addr, 'https': addr})
			self.verify_ip(proxies)
