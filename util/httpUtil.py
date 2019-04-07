import requests
import json
from common.commonData import CommonData

class HttpUtil:
    def __init__(self):
        self.http = requests.session()
        self.headers = {'Content-Type':'application/json;charset=UTF-8'}

    def post(self,path,data):
        proxies = {'http': 'http://localhost:8888'}     #获取全局变量proxies
        # headers = {'Content-Type':'application/json;charset=UTF-8'}
        # print(headers)
        # http = requests.session()
        host = CommonData.host       #获取全局变量host
        data_json = json.dumps(data)        #将data参数转为json格式
        if CommonData.token is not None:        #判断token是否为空，不为空则赋值，为空则不加
            self.headers['token'] = CommonData.token
        # self.headers['token'] = CommonData.token
        resp_login = self.http.post(url=host+path,       #发起post请求
                             proxies=proxies,
                             data=data_json,
                             headers=self.headers)
        # assert resp_login.status_code == 200    #校验码返回是否为200
        resp_json = resp_login.text          #获取response响应的body值
        resp_dict = json.loads(resp_json)       #将body值转换为dict
        # resp_json = json.loads(resp_login)
        # return resp_json
        return resp_dict                    #返回body













# #添加代理
# proxies = {'http':'http://localhost:8888'}
# headers = {'Content-Type':'application/json;charset=UTF-8'}
# print(headers)
# http = requests.session()
# resp = http.post(url="http://192.168.1.203:8083/sys/login",
#                      proxies=proxies,
#                      data='{"userName":"18210034706","password":"123456"}',
#                      headers=headers)
# print(resp.text)
# # print(json.loads(resp.text))
# resp_dict = json.loads(resp.text)   #json转python dict
# # print(resp_dict['object']['token'])
# token = resp_dict['object']['token']  #获取token
# headers['token'] = token    #将token加到headers dict里
# # print(headers)
# data = {'token': token}      #创建了一个data的dict，添加了token数据
# data_json =json.dumps(data)   #将python对象转换成json
# print(token)
# resp = http.post(url="http://192.168.1.203:8083/sys/getUserInfo",
#                      proxies=proxies,
#                      # data='{"token":"'+token+'"}',
#                      data=data_json,
#                      headers=headers)
# print(resp)
# print(resp.text)
# # print(resp.cookies)
# # print(resp.encoding)
# # print(resp.headers)
# # print(resp.history)