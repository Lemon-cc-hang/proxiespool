# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:       redisClient.py
   Description :
   Author :         lemoncc
   date:            2020/7/13
-------------------------------------------------
"""
__author__ = 'lemoncc'

# import redis


# class RedisClient(object):
#
# 	def __init__(self):
# 		pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)   # host是redis主机，需要redis服务端和客户端都起着 redis默认端口是6379
# 		self.conn = redis.Redis(connection_pool=pool)
#
# 	def insert(self, **kwargs):
# 		self.conn.hset('proxies', kwargs['name'],{'proxy': kwargs['proxy'], 'value': 10})
#
# 	def verify_true(self, **kwargs):
# 		self.conn.hincrby('proxies', kwargs['name'], {'proxy': 1})
#
#
