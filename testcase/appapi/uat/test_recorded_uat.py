import pytest
import allure
# 引入日志功能：
from conf.read import getconf
from conf.settings import ENV
from util.LogHandler import logger
# 引用Excel表操作功能：
from util.ExcelHandler import ExcelHandler
# 引入发请求功能：
from util.RequestHhandler import RequestHandler
# 引入报告功能：
from util.AllureHandler import AllureHandler
# 引入发邮件功能：
from util.SendMailHandler import SendMailHandler
@allure.feature('录播福利')
@pytest.mark.recorded
#@pytest.mark.uat
@pytest.mark.test
@pytest.mark.online
@pytest.mark.appapi
class TestRecordedUat(object):
    # 测试的项目名称
    Pname = "appapi"
    # 测试用例数据获取路径
    DataFlie = Pname + "/" + ENV + "/uat"
    #测试的功能模块名称
    file_name = "recorded_uat"

    #获取对应接口的测试数据
    file_path = ExcelHandler().get_excel_path(DataFlie,file_name)
    test_data = ExcelHandler().get_excel_data_1(file_path,"recorded")

    @pytest.mark.error
    @pytest.mark.parametrize('item', test_data)
    @allure.story('录播福利')
    def test_recorded(self, item,Pname):
        # 获取每一行数并且发请求：
        response = RequestHandler().get_response(item,Pname,item['case_title'])
        # 行为驱动标记：
        allure.dynamic.feature(item['case_title'])
        allure.dynamic.story(item['case_description'])
        # 动态加参：
        allure.dynamic.title(item['case_title'])
        allure.dynamic.description(
            "<b style='color:red;'>描述：</b>{}<br />"
            "<b style='color:red;'>请求的url：</b>{}<br />"
            "<b style='color:red;'>预期值：</b>{}<br />"
            "<b style='color:red;'>实际执行结果：</b>{}<br />".format(
                item['case_description'],
                getconf(Pname,ENV +'_url') + getconf(Pname,item['case_title']),
                response[0],
                response[1]
            ))
        assert response[0] == response[1]

    def teardown_class(self):
        # 参数化用例都执行完毕才执行的操作：
        logger().info('teardown_class')
        # 执行allure命令，生成allure报告
        AllureHandler().execute_command()
        # 将测试报告打包并发送邮件：
        # SendMailHandler().send_mail_msg()

