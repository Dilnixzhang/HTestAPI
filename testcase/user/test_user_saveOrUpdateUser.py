from conftest import http
import random
import json
import pytest

@pytest.mark.debug
class Test_User:
    #注册
    nickName = str(random.randint(00000000,99999999))
    userName = '188' + nickName
    def test_user_saveOrUpdate(self):
        update_path = '/user/saveOrUpdateUser'
        update_data = {
                "nickName":self.nickName,
                "userName":self.userName,
                "telNo":"",
                "email":"",
                "address":"",
                "roleIds":"",
                "regionId":1,
                "regionLevel":1
            }
        resp_saveOrUpdate_success = http.post(update_path,update_data)
        assert resp_saveOrUpdate_success['code'] == 200

    #登录
    def test_login(self):
        login_path = '/sys/login'
        # userName = '188' + self.nickName
        login_data = {"userName":self.userName, "password":'123456'}
        # data['userName'] = '18210034706'
        # data['password'] = '123456'
        resp_login = http.post(login_path, login_data)
        assert resp_login['code'] == 200
        assert resp_login['msg'] == '操作成功'
        Id = resp_login['object']['userId']
        return Id

    def test_loadUserList(self):
        list_path = '/user/loadUserList'
        list_data = {
            "pageCurrent":1,
            "pageSize":10,
            "nickName":"",
            "userName":"",
            "regionId":1
        }
        resp_loadUserList = http.post(list_path,list_data)
        assert resp_loadUserList['code'] == 200
        assert resp_loadUserList['msg'] == '操作成功'
        assert resp_loadUserList['object']['list'][0]['id'] == self.test_login()

    def test_user_loadUserInfo(self):
        info_path = '/user/loadUserInfo'
        info_data = {"id":self.test_login()}
        resp_loadUserInfo = http.post(info_path,info_data)
        resp_json = json.dumps(resp_loadUserInfo)  # 获取response响应的body值
        # resp_dict = json.loads(resp_loadUserInfo)
        print(resp_json)
