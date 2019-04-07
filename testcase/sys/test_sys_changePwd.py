import pytest
import allure
from common.commonData import CommonData
from conftest import http


@allure.feature('修改密码模块')
class Test_ChangePwd(object):
    @allure.story('修改密码成功')
    # @pytest.mark.debug
    @pytest.mark.usefixtures("recoverPwd")
    def test_sys_changePwd(self):
        path = '/sys/changePwd'
        newpwd = '654321'
        data = {'userId':CommonData.userId,
                'userName':CommonData.userName,
                'oldPwd':newpwd,
                'password':'123456'}
        resp_changPwd = http.post(path,data)
        assert resp_changPwd['code'] == 200
        assert resp_changPwd['msg'] == '操作成功'
    @allure.story('旧密码错误，修改失败')
    # @pytest.mark.debug
    def test_sys_changFail(self):
        path = '/sys/changePwd'
        data = {
            'userId':CommonData.userId,
            'userName':CommonData.userName,
            'oldPwd':'0987654',
            'password': '123456'
        }
        resp_changeFail = http.post(path,data)
        assert resp_changeFail['code'] == 411
        assert resp_changeFail['msg'] == '旧密码错误'
    #
    # def test_sys_oldpwd_null(self):
    #     path = '/sys/changePwd'
    #     data = {
    #         'userId': CommonData.userId,
    #         'userName': CommonData.userName,
    #         'oldPwd': ' ',
    #         'password': '123456'
    #     }
    #     resp_oldpwd_null = http.post(path,data)
    #     return resp_oldpwd_null
    #
    # def test_sys_newpwd_null(self):
    #     path = '/sys/changePwd'
    #     data = {
    #         'userId': CommonData.userId,
    #         'userName': CommonData.userName,
    #         'oldPwd':'654321',
    #         'password':''
    #     }
    #     resp_newpwd_null = http.post(path,data)
    #     return resp_newpwd_null
    #
@allure.story('恢复密码')
@pytest.fixture()
def recoverPwd():
    path = '/sys/changePwd'
    newpwd = '654321'
    data = {'userId':CommonData.userId,
            'userName':CommonData.userName,
            'oldPwd':'123456',
            'password':newpwd
            }
    resp_recoverPwd = http.post(path,data)
    # assert resp_recoverPwd['code'] == 200
    # assert resp_recoverPwd['msg'] == '操作成功'