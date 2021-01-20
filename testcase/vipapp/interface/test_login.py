import json
import re
import pytest
import allure

# 引入日志功能：
from conf.read import getconf
from conf.settings import ENV
from plugs.get_globals_data import GlobalData
from util.LogHandler import logger
# 引用Excel表操作功能：
from util.ExcelHandler import ExcelHandler
from util.TRequestHhandler import tRequestHandler

@allure.feature('登陆学员app')
@pytest.mark.TestvipappLogin
class TestvipappLogin(object):
    # 测试的项目名
    Pname = 'vipapp'
    # 测试用例数据获取路径
    DataFlie = Pname + "/" + ENV + "/interface"
    file_name = "login"
    # 获取对应接口的测试数据
    file_path = ExcelHandler().get_excel_path(DataFlie, file_name)
    login_data = ExcelHandler().get_excel_data_1(file_path, "yzm")

    @pytest.TestvipappLogin
    @pytest.mark.loginyzm
    @pytest.mark.parametrize('item', login_data)
    @allure.feature('获取token')
    def test_loginyzm(self): #item, Pname=Pname
        # Iname = 'yzm'
        # # 获取每一行数并且发请求：
        # response = tRequestHandler()._send_msg_data(item, Pname, Iname)
        # print(response)
        # if json.loads(response)["code"] == 0:
        #     if str(json.loads(response)["data"]["token"]) is None:
        #         logger().info("获取token失败")
        #     else:
        #         GlobalData.token['token'] = str(json.loads(response)["data"]["token"])
        # else:
        #     logger().info("登录失败获取token失败")
        # assert json.loads(response)["code"] == 0





