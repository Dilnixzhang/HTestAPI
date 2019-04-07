import allure
from common.commonData import CommonData
from conftest import http
import pytest

@allure.feature('获取用户信息模块')
# @pytest.mark.debug
class Test_getUserinfo:
    def test_getUserInfo(self):
        path = '/sys/getUserInfo'
        data = {'token': CommonData.token}
        resp_getUserInfo = http.post(path, data)
        assert resp_getUserInfo['code'] == 200
        assert resp_getUserInfo['msg'] == '操作成功'
