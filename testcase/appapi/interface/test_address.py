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
# 引入发邮件功能：
from util.SendMailHandler import SendMailHandler
from conf.settings import ENV
@allure.feature('收获地址模块')
@pytest.mark.address
@pytest.mark.appapi
@pytest.mark.test
@pytest.mark.online
class TestAddress(object):
    #测试的项目名称
    Pname = "appapi"
    #测试用例数据获取路径
    DataFlie =  Pname+"/"+ENV+"/interface"
    #测试的功能模块名称
    file_name = "address"


    #获取对应接口的测试数据
    file_path = ExcelHandler().get_excel_path(DataFlie,file_name)
    add_data = ExcelHandler().get_excel_data_1(file_path,"add")
    edit_data = ExcelHandler().get_excel_data_1(file_path,"edit")
    delete_data = ExcelHandler().get_excel_data_1(file_path,"delete")
    list_data = ExcelHandler().get_excel_data_1(file_path,"list")
    province_data = ExcelHandler().get_excel_data_1(file_path,"province")
    city_data = ExcelHandler().get_excel_data_1(file_path,"city")
    county_data = ExcelHandler().get_excel_data_1(file_path, "county")

    @pytest.mark.add
    @pytest.mark.parametrize('item',add_data)
    @allure.story('收货地址新增')
    def test_add(self,item,Pname):
        Iname ='add'
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

    @pytest.mark.edit
    @pytest.mark.parametrize('item',edit_data)
    @allure.story('收货地址修改')
    def test_edit(self,item,Pname):
        Iname='edit'
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
    @allure.story('获取收获地址列表')
    def test_list(self,item):
        # 调用日志功能的info级别：
        # logger().info(item)
        # 获取每一行数并且发请求：
        response = RequestHandler().get_response(item,'list')
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
                getconf('api',ENV +'_url') + getconf('api','list'),
                response[0],
                response[1]
        ))
        assert response[0] == response[1]

    @pytest.mark.delete
    @pytest.mark.parametrize('item',delete_data)
    @allure.story('删除收获地址')
    def test_delete(self,item):
        # 调用日志功能的info级别：
        # logger().info(item)
        # 获取每一行数并且发请求：
        response = RequestHandler().get_response(item,'delete')
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
                getconf('api',ENV +'_url') + getconf('api','delete'),
                response[0],
                response[1]
            ))
        assert response[0] == response[1]


    @pytest.mark.province
    @pytest.mark.parametrize('item',province_data)
    @allure.story('获取省份列表')
    def test_province(self,item):
        # 调用日志功能的info级别：
        # logger().info(item)
        # 获取每一行数并且发请求：
        response = RequestHandler().get_response(item,'province')
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
                getconf('api',ENV +'_url') + getconf('api','province'),
                response[0],
                response[1]
            ))
        assert response[0] == response[1]

    @pytest.mark.city
    @pytest.mark.parametrize('item',city_data)
    @allure.feature('获取城市列表')
    def test_city(self,item):
        # 调用日志功能的info级别：
        # logger().info(item)
        # 获取每一行数并且发请求：
        response = RequestHandler().get_response(item,'city')
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
                getconf('api',ENV +'_url') + getconf('api','city'),
                response[0],
                response[1]
        ))
        assert response[0] == response[1]

    @pytest.mark.county
    @pytest.mark.parametrize('item',county_data)
    @allure.story('根据城市ID获取县城列表')
    def test_county(self,item):
        # 调用日志功能的info级别：
        # logger().info(item)
        # 获取每一行数并且发请求：
        response = RequestHandler().get_response(item,'county')
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
               getconf('api',ENV +'_url') + getconf('api','county'),
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

