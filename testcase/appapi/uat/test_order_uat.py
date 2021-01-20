import pytest
import allure
# 引入日志功能：
from conf.settings import ENV
from util.DbSqlServer import MSSQL
from util.LogHandler import logger
# 引用Excel表操作功能：
from util.ExcelHandler import ExcelHandler
# 引入发请求功能：
from util.RequestHhandler import RequestHandler
# 引入报告功能：
from util.AllureHandler import AllureHandler
# 引入发邮件功能：
from util.SendMailHandler import SendMailHandler
@allure.feature('订单模块业务场景回归')
@pytest.mark.orderT
#@pytest.mark.uat
class TestOrder(object):
    # 测试的项目名称
    Pname = "appapi"
    # 测试用例数据获取路径
    DataFlie = Pname + "/" + ENV + "/uat"
    #测试的功能模块名称
    file_name = "order_uat"

    #获取对应接口的测试数据
    file_path = ExcelHandler().get_excel_path(DataFlie,file_name)
    test_data = ExcelHandler().get_excel_data_1(file_path,"Order")


    @pytest.mark.Order
    @pytest.mark.parametrize('item', test_data)
    @allure.story('立即购买')
    def test_Order(self, item,Pname=Pname):
        Iname = "Order"
        # 获取每一行数并且发请求：
        response = RequestHandler().get_response_prec(Pname,Iname)
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
                item['case_url'],
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

