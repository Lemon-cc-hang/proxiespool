# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:       mongoClient.py
   Description :
   Author :         lemoncc
   date:            2020/7/13
-------------------------------------------------
"""
__author__ = 'lemoncc'

from pymongo import MongoClient


class MongodbClient(object):

	def __init__(self, table, host, port, max_data, **kwargs):
		self.__collection = table
		self._max_data = max_data
		self._client = MongoClient(host, port, connect=False, **kwargs)
		self._db = self._client.proxy

	def changeTable(self, table):
		self.__collection = table

	def insert(self, _dict):
		if self.getNumber() <= self._max_data:
			if _dict is not None:
				if not self.__isExist(_dict):
					_dict['score'] = 10
					self._db[self.__collection].insert_one(_dict)
				else:
					self.__score_add(_dict)

	def clean_database(self):
		self._client.drop_database('proxy')

	def delete_all(self):
		self._db[self.__collection].remove()

	def getNumber(self):
		return self._db[self.__collection].count()

	def delete(self, _dict):
		return self._db[self.__collection].delete_one(_dict)

	def __score_add(self, __dict):
		result = self.__find(__dict)
		if result['score'] >= 100:
			return
		elif result['score'] >= 10:
			result['score'] += 1
		else:
			result['score'] = 10
		self.__update(__dict, result)

	def __update(self, __dict, result):
		return self._db[self.__collection].update(__dict, result)

	def score_sub(self, __dict):
		if self.__isExist(__dict):
			result = self.__find(__dict)
			result['score'] -= 1
			if result['score'] > 0:
				self.__update(__dict, result)
			else:
				self.delete(__dict)

	def get_proxies(self, num=1):
		result = self.__sort().limit(num)
		return [{'http': r['http'], 'https': r['https']} for r in result]

	def __find(self, _dict):
		return self._db[self.__collection].find_one(_dict)

	def __isExist(self, _dict):
		if self.__find(_dict):
			return True
		else:
			return False

	def __sort(self):
		if not self.__isEmpty():
			return self._db[self.__collection].find().sort('score', -1)

	def __isEmpty(self):
		if self.getNumber():
			return False
		else:
			return True

	def getAll(self):
		results = self._db[self.__collection].find({'score': {'$gt': 0}})
		return [{'http': r['http'], 'https': r['https']} for r in results]

	def find(self, _dict):
		return self._db[self.__collection].find(_dict)