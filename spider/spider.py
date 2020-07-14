# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:       spider.py
   Description :
   Author :         lemoncc
   date:            2020/7/14
-------------------------------------------------
"""
__author__ = 'lemoncc'


from multiprocessing import Process
from spider.getPages import GetPages
from helper.scheduler import scheduler
from threading import Thread

class Spider(object):

	def __init__(self):
		getPages = GetPages()
		kuaidaili_pages = getPages.kuaidaili_pages()
		xiladaili_pages = getPages.xiladaili_pages()
		ip89_pages = getPages.ip89_pages()
		ip3366_pages = getPages.ip3366_pages()
		jiangxianli_pages = getPages.jiangxianli_pages()
		self.kuaidaili_urls = [f'https://www.kuaidaili.com/free/inha/{i}'for i in range(1, kuaidaili_pages + 1)]
		self.xiladaili_urls = [f'http://www.xiladaili.com/gaoni/{i}/'for i in range(1, xiladaili_pages + 1)]
		self.ip89_urls = [f'http://www.89ip.cn/index_{i}.html'for i in range(1, ip89_pages + 1)]
		self.ip3366_urls = [f'http://www.ip3366.net/free/?stype=1&page={i}'for i in range(1, ip3366_pages + 1)]
		self.jiangxianli_urls = [f'https://ip.jiangxianli.com/?page={i}'for i in range(1, jiangxianli_pages + 1)]

	def xiLaDaiLi(self):
		for url in self.xiladaili_urls:
			scheduler.runParseHtml().parse_html_xiladaili(scheduler.runGetHtml().get(url))

	def kuaiDaiLi(self):
		for url in self.kuaidaili_urls:
			scheduler.runParseHtml().parse_html_kuaidaili(scheduler.runGetHtml().get(url))

	def ip89(self):
		for url in self.ip89_urls:
			scheduler.runParseHtml().parse_html_ip89(scheduler.runGetHtml().get(url))

	def ip3366(self):
		for url in self.ip3366_urls:
			scheduler.runParseHtml().parse_html_kuaidaili(scheduler.runGetHtml().get(url))

	def jiangxianli(self):
		for url in self.jiangxianli_urls:
			scheduler.runParseHtml().parse_html_kuaidaili(scheduler.runGetHtml().get(url))

	def collection(self):
		t1 = Thread(target=self.ip89, name='ip89')
		t2 = Thread(target=self.ip3366, name='ip3366')
		t3 = Thread(target=self.jiangxianli, name='jiangxianli')
		t1.start()
		t2.start()
		t3.start()
		t1.join()
		t2.join()
		t3.join()

	def run(self):
		p = Process(target=self.xiLaDaiLi, name='xiLaDaiLi')
		p1 = Process(target=self.kuaiDaiLi, name='kuaiDaiLi')
		p2 = Process(target=self.collection, name='others')
		p.start()
		p1.start()
		p2.start()
		p.join()
		p1.join()
		p2.join()
		p.close()
		p1.close()
		p2.close()
