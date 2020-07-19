# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:       startApi.py
   Description :
   Author :         lemoncc
   date:            2020/7/19
-------------------------------------------------
"""
__author__ = 'lemoncc'

from api.api import app
from config import flaskApiConfig

if __name__ == '__main__':
	app.run(**flaskApiConfig)