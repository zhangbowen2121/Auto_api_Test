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
@allure.feature('校区模块')
@pytest.mark.school
@pytest.mark.appapi
@pytest.mark.test
@pytest.mark.online
class TestSchool(object):
    # 测试的项目名称
    Pname = "appapi"
    # 测试用例数据获取路径
    DataFlie = Pname + "/" + ENV + "/interface"
    #测试的功能模块名称
    file_name = "school"

    #获取对应接口的测试数据
    file_path = ExcelHandler().get_excel_path(DataFlie,file_name)
    getList_data = ExcelHandler().get_excel_data_1(file_path,"getList")
    getDistrictList_data = ExcelHandler().get_excel_data_1(file_path,"getDistrictList")
    getCampusList_data = ExcelHandler().get_excel_data_1(file_path,"getCampusList")
    getSchoolList_data = ExcelHandler().get_excel_data_1(file_path,"getSchoolList")

    @pytest.mark.getList
    @pytest.mark.parametrize('item',getList_data)
    @allure.story('校区导航')
    def test_getList(self,item,Pname):
        Iname='getList'
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

    @pytest.mark.getDistrictList
    @pytest.mark.parametrize('item',getDistrictList_data)
    @allure.story('获取校区导航的地区列表')
    def test_getDistrictList(self,item,Pname):
        Iname='getDistrictList'
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


    @pytest.mark.getSchoolList
    @pytest.mark.parametrize('item',getSchoolList_data)
    @allure.story('学员推荐-获取校区')
    def test_getSchoolList(self,item,Pname):
        Iname='getSchoolList'
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

    @pytest.mark.getCampusList
    @pytest.mark.parametrize('item',getCampusList_data)
    @allure.story('获取校区导航的地区列表')
    def test_getCampusList(self,item,Pname):
        Iname='getCampusList'
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

