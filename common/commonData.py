import requests
import pytest

class CommonData():
    userId = 165
    userName = '13812345678'
    password = '123456'
    host = 'http://192.168.1.203:8083'
    token = None
    proxies = {'http': 'http://localhost:8888'}

    # headers = {'Content-Type': 'application/json;charset=UTF-8'}
