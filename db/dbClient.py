# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:       dbClient.py
   Description :
   Author :         lemoncc
   date:            2020/7/14
-------------------------------------------------
"""
__author__ = 'lemoncc'

from db.mongoClient import MongodbClient


class DbClient(object):
	"""
	changeTable(): 改变表
	insert(): 插入数据
	clean_database(): 清空数据库
	delete_all(): 删除所有
	getNumber(): 返回长度
	delete(): 删除一个数据
	score_sub(): 减分
	get_proxies(): 获取代理
	sort_(): 排序
	"""

	def __init__(self, db_host='localhost', db_port=27017, db_user=None, db_pwd=None, db_maxData=10000, db_table='proxiesPool', maxPoolSize=None):
		self.client = MongodbClient(host=db_host,
		                            port=db_port,
		                            max_data=db_maxData,
		                            username=db_user,
		                            password=db_pwd,
		                            table=db_table,
		                            maxPoolSize=maxPoolSize)

	def get_proxies(self, num=1):
		return self.client.get_proxies(num)

	def insert(self, _dict):
		return self.client.insert(_dict)

	def changeTable(self, _dict):
		return self.client.changeTable(_dict)

	def clean_database(self):
		return self.client.clean_database()

	def delete_all(self):
		return self.client.delete_all()

	def getNumber(self):
		return self.client.getNumber()

	def delete(self, _dict):
		return self.client.delete(_dict)

	def score_sub(self, _dict):
		return self.client.score_sub(_dict)

	def getAll(self):
		return self.client.getAll()

	def find(self, _dict):
		return self.client.find(_dict)