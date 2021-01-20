

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
from util.TRequestHhandler import tRequestHandler


@allure.feature('教学模块')
@pytest.mark.educational
class TestEducational(object):
    # 测试的项目名称
    Pname = "teachingApi"
    # 测试用例数据获取路径
    DataFlie = Pname + "/" + ENV + "/interface"
    #测试的功能模块名称
    file_name = "educational"

    #获取对应接口的测试数据
    file_path = ExcelHandler().get_excel_path(DataFlie,file_name)
    getLessonListApp_data = ExcelHandler().get_excel_data_1(file_path,"getLessonListApp")
    getLessonInfo_data = ExcelHandler().get_excel_data_1(file_path, "getLessonInfo")
    getLessonDetail_data = ExcelHandler().get_excel_data_1(file_path, "getLessonDetail")
    getPrepareLessonListApp_data = ExcelHandler().get_excel_data_1(file_path, "getPrepareLessonListApp")
    getLessonSubjectMapping_data = ExcelHandler().get_excel_data_1(file_path, "getLessonSubjectMapping")

    @pytest.mark.educational
    @pytest.mark.getLessonListApp
    @pytest.mark.parametrize('item',getLessonListApp_data)
    @allure.feature('查询备课')
    def test_getLessonListApp(self,item,Pname=Pname):
        Iname='getLessonListApp'
        # 获取每一行数并且发请求：
        response = tRequestHandler().get_response(item,Pname,Iname)
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

    @pytest.mark.educational
    @pytest.mark.getLessonInfo
    @pytest.mark.parametrize('item', getLessonInfo_data)
    @allure.feature('课时详情')
    def test_getLessonInfo(self, item, Pname=Pname):
        Iname = 'getLessonInfo'
        # 获取每一行数并且发请求：
        response = tRequestHandler().get_response(item, Pname, Iname)
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
                getconf(Pname, ENV + '_url') + getconf(Pname, Iname),
                response[0],
                response[1]
            ))
        assert response[0] == response[1]

    @pytest.mark.educational
    @pytest.mark.getLessonDetail
    @pytest.mark.parametrize('item', getLessonDetail_data)
    @allure.feature('获取课程详情')
    def test_getLessonDetail(self, item, Pname=Pname):
        Iname = 'getLessonDetail'
        # 获取每一行数并且发请求：
        response = tRequestHandler().get_response(item, Pname, Iname)
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
                getconf(Pname, ENV + '_url') + getconf(Pname, Iname),
                response[0],
                response[1]
            ))
        assert response[0] == response[1]

    @pytest.mark.educational
    @pytest.mark.getPrepareLessonListApp
    @pytest.mark.parametrize('item', getPrepareLessonListApp_data)
    @allure.feature('获取备课清单(核录那)')
    def test_getPrepareLessonListApp(self, item, Pname=Pname):
        Iname = 'getPrepareLessonListApp'
        # 获取每一行数并且发请求：
        response = tRequestHandler().get_response(item, Pname, Iname)
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
                getconf(Pname, ENV + '_url') + getconf(Pname, Iname),
                response[0],
                response[1]
            ))
        assert response[0] == response[1]

    @pytest.mark.educational
    @pytest.mark.getLessonSubjectMapping
    @pytest.mark.parametrize('item', getLessonSubjectMapping_data)
    @allure.feature('获取课节学科映射关系')
    def test_getLessonSubjectMapping(self, item, Pname=Pname):
        Iname = 'getLessonSubjectMapping'
        # 获取每一行数并且发请求：
        response = tRequestHandler().get_response(item, Pname, Iname)
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
                getconf(Pname, ENV + '_url') + getconf(Pname, Iname),
                response[0],
                response[1]
            ))
        assert response[0] == response[1]


    #def teardown_class(self):
        # 参数化用例都执行完毕才执行的操作：
    #   logger().info('teardown_class')
        # 执行allure命令，生成allure报告
        #AllureHandler().execute_command()
        # 将测试报告打包并发送邮件：
        # SendMailHandler().send_mail_msg()


