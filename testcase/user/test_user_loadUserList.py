# from conftest import http
# import pytest
#
#
# class Test_UserList():
#     # @pytest.mark.debug
#     def test_user_loadUserList(self):
#         path = '/user/loadUserList'
#         data = {
#             "pageCurrent":1,
#             "pageSize":10,
#             "nickName":"",
#             "userName":"",
#             "regionId":1
#         }
#         resp_loadUserList = http.post(path,data)
#         assert resp_loadUserList['code'] == 200
#         assert resp_loadUserList['msg'] == '操作成功'
