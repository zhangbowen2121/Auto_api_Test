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
@pytest.mark.app2_3
@pytest.mark.appapi
#@pytest.mark.test
class TestApp2_3(object):
    #测试的项目名称
    project_name = "appapi/"+ENV+"/interface"
    #测试的功能模块名称
    file_name = "app2_3"

    #获取对应接口的测试数据

    file_path = ExcelHandler().get_excel_path(project_name,file_name)
    logger().info(file_path)
    generOrderV2V3_data = ExcelHandler().get_excel_data_1(file_path,"generateOrderV2V3")
    lessonLeave_data = ExcelHandler().get_excel_data_1(file_path,"lessonLeave")
    getCheckPayCourse_data = ExcelHandler().get_excel_data_1(file_path,"getCheckPayCourse")
    listV2V1_data = ExcelHandler().get_excel_data_1(file_path,"listV2V1")

    @pytest.mark.generateOrderV2V3
    @pytest.mark.parametrize('item',generOrderV2V3_data)
    @allure.feature('小组课立即购买生成订单')
    def test_generateOrderV2V3(self,item):
        # 获取每一行数并且发请求：
        response = RequestHandler().get_response(item,'generOrderV2V3')
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
                getconf('api',ENV +'_url') + getconf('api','generOrderV2V3'),
                response[0],
                response[1]
            ))
        assert response[0] == response[1]

    @pytest.mark.lessonLeave
    @pytest.mark.parametrize('item',lessonLeave_data)
    @allure.feature('学员请假')
    def test_lessonLeave(self,item):
        # 获取每一行数并且发请求：
        response = RequestHandler().get_response(item,'lessonLeave')
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
                getconf('api',ENV +'_url') + getconf('api','lessonLeave'),
                response[0],
                response[1]
        ))
        assert response[0] == response[1]


    @pytest.mark.getCheckPayCourse
    @pytest.mark.parametrize('item',getCheckPayCourse_data)
    @allure.feature('获取课程是否插班，检查是否中途报名')
    def test_getCheckPayCourse(self,item):
        # 调用日志功能的info级别：
        # logger().info(item)
        # 获取每一行数并且发请求：
        response = RequestHandler().get_response(item,'getCheckPayCourse')
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
                getconf('api',ENV +'_url') + getconf('api','getCheckPayCourse'),
                response[0],
                response[1]
        ))
        assert response[0] == response[1]



    @pytest.mark.listV2V1
    @pytest.mark.parametrize('item',listV2V1_data)
    @allure.feature('根据token登录')
    def test_listV2V1(self,item):
        # 调用日志功能的info级别：
        # logger().info(item)
        # 获取每一行数并且发请求：
        response = RequestHandler().get_response(item,'listV2V1')
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
                getconf('api',ENV +'_url') + getconf('api','listV2V1'),
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

