import pytest
import allure
# 引入日志功能：
from conf.read import getconf
from util.LogHandler import logger
# 引用Excel表操作功能：
from util.ExcelHandler import ExcelHandler
# 引入发请求功能：
from util.RequestHhandler import RequestHandler
# 引入报告功能：
from util.AllureHandler import AllureHandler
from conf.settings import ENV
# 引入发邮件功能：
from util.SendMailHandler import SendMailHandler
@allure.feature('错题模块')
@pytest.mark.error
@pytest.mark.appapi
@pytest.mark.online
@pytest.mark.test
class TestError(object):
    # 测试的项目名称
    Pname = "appapi"
    # 测试用例数据获取路径
    DataFlie = Pname + "/" + ENV + "/interface"
    #测试的功能模块名称
    file_name = "error"

    #获取对应接口的测试数据
    file_path = ExcelHandler().get_excel_path(DataFlie,file_name)
    deleteQusetion_data = ExcelHandler().get_excel_data_1(file_path,"deleteQusetion")
    getQusetionList_data = ExcelHandler().get_excel_data_1(file_path,"getQusetionList")
    getQusetionSubjectList_data = ExcelHandler().get_excel_data_1(file_path,"getQusetionSubjectList")
    getQusetionNum_data = ExcelHandler().get_excel_data_1(file_path,"getQusetionNum")
    getPdfUrl_data = ExcelHandler().get_excel_data_1(file_path,"getPdfUrl")
    getPdfDownloadCode_data = ExcelHandler().get_excel_data_1(file_path,"getPdfDownloadCode")

    @pytest.mark.deleteQusetion
    @pytest.mark.parametrize('item',deleteQusetion_data)
    @allure.story('错题本-删除错题')
    def test_deleteQusetion(self,item,Pname):
        Iname='deleteQusetion'
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

    @pytest.mark.getQusetionList
    @pytest.mark.parametrize('item',getQusetionList_data)
    @allure.story('错题列表')
    def test_getQusetionList(self,item,Pname):
        Iname='getQusetionList'
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


    @pytest.mark.getQusetionSubjectList
    @pytest.mark.parametrize('item',getQusetionSubjectList_data)
    @allure.feature('错题本-获取错题学科列表')
    def test_getQusetionSubjectList(self,item,Pname):
        Iname='getQusetionSubjectList'
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

    @pytest.mark.getQusetionNum
    @pytest.mark.parametrize('item',getQusetionNum_data)
    @allure.feature('错题本-错题数量')
    def test_getQusetionNum(self,item,Pname):
        Iname='getQusetionNum'
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


    @pytest.mark.getPdfUrl
    @pytest.mark.parametrize('item',getPdfUrl_data)
    @allure.feature('错题本-下载错题生成PDF轮询')
    def test_getPdfUrl(self,item,Pname):
        Iname='getPdfUrl'
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

    @pytest.mark.getPdfDownloadCode
    @pytest.mark.parametrize('item', getPdfDownloadCode_data)
    @allure.feature('错题本-下载错题生成PDF返回下载码')
    def test_getPdfDownloadCode(self, item,Pname):
        Iname='getPdfDownloadCode'
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

