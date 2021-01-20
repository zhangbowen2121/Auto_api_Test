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
@allure.feature('登录模块')
@pytest.mark.login
@pytest.mark.markpwd
@pytest.mark.appapi
@pytest.mark.test
@pytest.mark.online
class TestLogin(object):
    # 测试的项目名称
    Pname = "appapi"
    # 测试用例数据获取路径
    DataFlie = Pname + "/" + ENV + "/interface"
    #测试的功能模块名称
    file_name = "login"

    #获取对应接口的测试数据
    file_path = ExcelHandler().get_excel_path(DataFlie,file_name)
    login_data = ExcelHandler().get_excel_data_1(file_path,"password")
    yzm_data = ExcelHandler().get_excel_data_1(file_path,"yzm")
    GetUList_data = ExcelHandler().get_excel_data_1(file_path,"getUserList")
    GetStuType_data = ExcelHandler().get_excel_data_1(file_path,"getStuType")
    LoginByToken_data = ExcelHandler().get_excel_data_1(file_path,"Token")
    ChangePwd_data = ExcelHandler().get_excel_data_1(file_path,"changePwd")

    @pytest.mark.loginpwd
    @pytest.mark.pwd1
    @pytest.mark.parametrize('item',login_data)
    @allure.story('通过用户名和密码登录')
    def test_loginByPwd(self,item,Pname):
        Iname='pwd'
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

    @pytest.mark.loginbyyzm
    @pytest.mark.parametrize('item',yzm_data)
    @allure.story('通过手机号和短信验证码登录')
    def test_loginByYzm(self,item,Pname):
        Iname='yzm'
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


    @pytest.mark.getUserList
    @pytest.mark.parametrize('item',GetUList_data)
    @allure.story('根据手机号获取学员的身份')
    def test_getUserlist(self,item,Pname):
        Iname='getUList'
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

    @pytest.mark.getStuType
    @pytest.mark.parametrize('item',GetStuType_data)
    @allure.story('根据手机号获取学员的身份')
    def test_getStuType(self,item,Pname):
        Iname='getStuType'
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


    @pytest.mark.token
    @pytest.mark.parametrize('item',LoginByToken_data)
    @allure.story('根据token登录')
    def test_loginByToken(self,item,Pname):
        Iname='token'
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

    @pytest.mark.changePwd
    @pytest.mark.parametrize('item',ChangePwd_data)
    @allure.story('修改密码')
    def test_changePwd(self,item,Pname):
        Iname='changePwd'
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

