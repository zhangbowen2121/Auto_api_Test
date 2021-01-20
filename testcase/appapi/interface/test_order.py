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
@allure.feature('订单模块')
@pytest.mark.order
@pytest.mark.appapi
class TestOrdercd(object):
    # 测试的项目名称
    Pname = "appapi"
    # 测试用例数据获取路径
    DataFlie = Pname + "/" + ENV + "/interface"
    #测试的功能模块名称
    file_name = "order"

    #获取对应接口的测试数据
    file_path = ExcelHandler().get_excel_path(DataFlie,file_name)
    pay_data = ExcelHandler().get_excel_data_1(file_path,"pay")
    list_data = ExcelHandler().get_excel_data_1(file_path,"list")
    syncOrderAddress_data = ExcelHandler().get_excel_data_1(file_path,"syncOrderAddress")
    deleteOrder_data = ExcelHandler().get_excel_data_1(file_path,"deleteOrder")
    generateOrder_data = ExcelHandler().get_excel_data_1(file_path,"generateOrder")

    @pytest.mark.pay
    @pytest.mark.parametrize('item',pay_data)
    @allure.story('订单支付')
    def test_pay(self,item,Pname):
        Iname='pay'
        # 获取每一行数并且发请求：
        response = RequestHandler().get_response(item,Pname,Iname)
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
                getconf(Pname,ENV +'_url') + getconf(Pname,Iname),
                response[0],
                response[1]
            ))
        assert response[0] == response[1]

    @pytest.mark.list
    @pytest.mark.parametrize('item',list_data)
    @allure.story('订单列表')
    def test_list(self,item,Pname):
        Iname='list'
        # 获取每一行数并且发请求：
        response = RequestHandler().get_response(item,Pname,Iname)
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
                getconf(Pname,ENV +'_url') + getconf(Pname,Iname),
                response[0],
                response[1]
        ))
        assert response[0] == response[1]


    @pytest.mark.syncOrderAddress
    #@pytest.mark.appapi
    @pytest.mark.parametrize('item',syncOrderAddress_data)
    @allure.feature('同步订单地址')
    def test_syncOrderAddress(self,item,Pname):
        Iname='syncOrderAddress'
        # 调用日志功能的info级别：
        # logger().info(item)
        # 获取每一行数并且发请求：
        response = RequestHandler().get_response(item,Pname,Iname)
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
                getconf(Pname,ENV +'_url') + getconf(Pname,Iname),
                response[0],
                response[1]
        ))
        assert response[0] == response[1]

    @pytest.mark.generateOrder
    @pytest.mark.parametrize('item',generateOrder_data)
    @allure.feature('立即购买')
    def test_generateOrder(self,item,Pname):
        Iname='generateOrder'
        # 调用日志功能的info级别：
        # logger().info(item)
        # 获取每一行数并且发请求：
        response = RequestHandler().get_response(item,Pname,Iname)
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
                getconf(Pname,ENV +'_url') + getconf(Pname,Iname),
                response[0],
                response[1]
            ))
        assert response[0] == response[1]


    @pytest.mark.deleteOrde
    @pytest.mark.parametrize('item',deleteOrder_data)
    @allure.story('删除订单')
    def test_deleteOrder(self,item,Pname):
        Iname='deleteOrde'
        # 调用日志功能的info级别：
        # logger().info(item)
        # 获取每一行数并且发请求：
        response = RequestHandler().get_response(item,Pname,Iname)
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
                getconf(Pname,ENV +'_url') + getconf(Pname,Iname),
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

