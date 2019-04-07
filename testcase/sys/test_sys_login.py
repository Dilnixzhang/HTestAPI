import pytest
import allure
from common.commonData import CommonData
from conftest import http

@allure.feature('登录模块')
# @pytest.mark.debug
class Test_login:
    @allure.story('登录成功')
    def test_login(self):
        path = '/sys/login'
        data = {"userName": CommonData.userName,
                "password": CommonData.password}
        resp_login = http.post(path, data)
        assert resp_login['code'] == 200
        assert resp_login['msg'] == '操作成功'
        assert resp_login['object']['userId'] == 165
        # CommonData.token = resp_login['object']['token']
    @allure.story('登录用户名或密码错误')
    def test_login_pwd_fail(self):
        path = '/sys/login'
        data = {"userName": CommonData.userName, "password": "1234756"}
        resp_login_pwd_fail=http.post(path,data)
        assert resp_login_pwd_fail['code'] == 410
        assert resp_login_pwd_fail['msg'] == '用户名或密码错误'
    @allure.story('用户名不存在')
    def test_login_user_fail(self):
        path = '/sys/login'
        data = {"userName": "18723456709", "password": "1234756"}
        resp_login_user_fail = http.post(path, data)
        assert resp_login_user_fail['code'] == 301
        assert resp_login_user_fail['msg'] == '用户不存在'

    # def test_login_no_user(self):
    #     path = '/sys/login'
    #     data = {'userName':' ','password':'123456'}
    #     resp_login_no_user = http.post(path,data)
    #     return resp_login_no_user

    def test_login_no_name(self):
        path = '/sys/login'
        data = {'password':CommonData.password}
        resp_login_no_name = http.post(path, data)
        assert resp_login_no_name['code'] == 301
        assert resp_login_no_name['msg'] == '用户不存在'
        return resp_login_no_name
    @allure.story('无密码')
    def test_login_no_pwd(self):
        path = '/sys/login'
        data = {'userName': CommonData.userName}
        resp_login_no_name = http.post(path, data)
        assert resp_login_no_name['code'] == 500
        assert resp_login_no_name['msg'] == '内部服务器异常，请联系研发人员'

    @allure.story('用户禁止登录')
    def test_login_forbidde(self):
        path = '/sys/login'
        data = {'userName': ' ', 'password': '123456'}
        resp_login_forbidde = http.post(path, data)
        assert resp_login_forbidde['code'] == 3010
        assert resp_login_forbidde['msg'] == '此账户禁止登录'


 






