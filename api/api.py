# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:       api.py
   Description :
   Author :         lemoncc
   date:            2020/7/19
-------------------------------------------------
"""
__author__ = 'lemoncc'

from flask import Flask, jsonify
from helper.common import common
from random import choice
from config import flaskApiConfig


def getProxies():
    if common.dbClient.getNumber() > 100:
        proxies = common.dbClient.get_proxies(10)
        if proxies is None:
            return None
        else:
            return choice(proxies)
    else:
        return None


app = Flask(__name__)
app.config.from_object('config.BaseConfig')


api_list = {
	'get_proxy': 'get an useful proxy',
	'get_all': 'get all proxies',
	'get_number': 'get count of the proxies'
}


@app.route('/')
def index():
    return api_list


@app.route('/get_proxy', methods=['GET'])
def get():
    proxy = getProxies()
    return proxy


@app.route('/get_all')
def getAll():
    proxies = common.dbClient.getAll()
    return jsonify([_ for _ in proxies])


@app.route('/get_number', methods=['GET'])
def getNumber():
    status = common.dbClient.getNumber()
    return {'count': status}


if __name__ == '__main__':
    app.run(**flaskApiConfig)
