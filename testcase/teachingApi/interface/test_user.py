import json
import re
import pytest
import allure
# 引入日志功能：
from conf.settings import ENV
from plugs.get_globals_data import GlobalData
from util.LogHandler import logger
# 引用Excel表操作功能：
from util.ExcelHandler import ExcelHandler
from util.TRequestHhandler import tRequestHandler
# 引入发请求功能：
from util.RequestHhandler import RequestHandler
# 引入报告功能：
from util.AllureHandler import AllureHandler
# 引入发邮件功能：

@allure.feature('获取教师TOKEN模块')
@pytest.mark.Tgetname

class TestSetToken(object):
    # 测试的项目名称
    Pname = "teachingApi"
    # 测试用例数据获取路径
    DataFlie = Pname + "/" + ENV + "/interface"
    file_name = "user"

    #获取对应接口的测试数据
    file_path = ExcelHandler().get_excel_path(DataFlie,file_name)
    logger().info(file_path)
    login_data = ExcelHandler().get_excel_data_1(file_path,"yzm")

    @pytest.mark.Tgetname
    @pytest.mark.parametrize('item',login_data)
    @allure.feature('获取token')
    def test_gettoken(self,item,Pname=Pname):
        Iname='yzm'
        # 获取每一行数并且发请求：
        response = tRequestHandler()._send_msg_data(item,Pname,Iname)
        if json.loads(response)["code"]==0:
            response1=tRequestHandler()._getCookie(item,Pname,Iname)
            app=re.findall(r"app=(.+?);",response1)
            accessToken=re.findall(r"ACCESS-TOKEN=(.+?);",response1)
            if app == None or accessToken ==None:
                logger().info("登录失败获取token失败")
            else:
                logger().info(app)

        assert json.loads(response)["code"] == 0


    #def teardown_class(self):
        # 参数化用例都执行完毕才执行的操作：
    #   logger().info('teardown_class')
        # 执行allure命令，生成allure报告
        #AllureHandler().execute_command()
        # 将测试报告打包并发送邮件：
        # SendMailHandler().send_mail_msg()

