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
@allure.feature('教师登录模块')
@pytest.mark.vip
@pytest.mark.teacher
@pytest.mark.viptest
@pytest.mark.viponline
class TestWin(object):
    #测试的项目名称
    Pname = "viponline"
    pFile =  Pname +"/"+ENV+"/interface"
    #测试的功能模块名称
    file_name = "teacher"


    #获取对应接口的测试数据
    file_path = ExcelHandler().get_excel_path(pFile,file_name)
    login_data = ExcelHandler().get_excel_data_1(file_path,"winlogin")
    getinfo_data = ExcelHandler().get_excel_data_1(file_path,"getinfo")
    getlessondate_data = ExcelHandler().get_excel_data_1(file_path,"getlessondate")
    getlessonlist_data = ExcelHandler().get_excel_data_1(file_path,"getlessonlist")
    tokenlogin_data = ExcelHandler().get_excel_data_1(file_path,"tokenlogin")
    getattach_data = ExcelHandler().get_excel_data_1(file_path,"getattach")

    @pytest.mark.teacherlogin
    @pytest.mark.parametrize('item',login_data)
    @allure.story('教师登录接口')
    def test_teacherlogin(self, item, Pname=Pname):
        Iname='winlogin'
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
                getconf(Pname,ENV+'_url')+getconf(Pname,Iname),
                response[0],
                response[1]
            ))
        assert response[0] == response[1]

    @pytest.mark.getinfo
    @pytest.mark.parametrize('item',getinfo_data)
    @allure.story('win获取教师基本信息')
    def test_loginGetinfo(self,item,Pname=Pname):
        Iname ='wingetinfo'
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
                getconf(Pname,ENV+'_url')+getconf(Pname,Iname),
                response[0],
                response[1]
        ))
        assert response[0] == response[1]


    @pytest.mark.getlessondate
    @pytest.mark.parametrize('item',getlessondate_data)
    @allure.story('win获取有课的日期')
    def test_getUserlist(self,item,Pname=Pname):
        Iname = 'wingetlessondate'
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
                getconf(Pname,ENV+'_url')+getconf(Pname,Iname),
                response[0],
                response[1]
        ))
        assert response[0] == response[1]

    @pytest.mark.getlessonlist
    @pytest.mark.parametrize('item',getlessonlist_data)
    @allure.story('win获取老师课表')
    def test_getLessonlist(self,item,Pname=Pname):
        Iname = 'wingetlessonlist'
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


    @pytest.mark.tokenlogin
    @pytest.mark.parametrize('item',tokenlogin_data)
    @allure.story('根据token登录')
    def test_loginByToken(self,item,Pname=Pname):
        Iname ='wintokenlogin'
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
                getconf(Pname,ENV+'_url') + getconf(Pname,Iname),
                response[0],
                response[1]
            ))
        assert response[0] == response[1]

    @pytest.mark.getattach
    @pytest.mark.parametrize('item',getattach_data)
    @allure.story('win获取直播配置')
    def test_getattach(self,item,Pname=Pname):
        Iname = 'wingetattach'
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

