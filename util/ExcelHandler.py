import os
# 引入配置文件：
from conf import settings
import xlrd

from conf.settings import DATA_PATH
from util.LogHandler import logger


class ExcelHandler(object):
    # Excel功能：
    def __init__(self, excel_file_path=None):
        self.excel_file_path = excel_file_path

    def get_excel_path(self,project_name,excel_name):
        EXCEL_FILE_NAME = excel_name+'.xlsx'
        logger().info(EXCEL_FILE_NAME)
        EXCEL_FILE_PATH = os.path.join(DATA_PATH,project_name,EXCEL_FILE_NAME)
        return EXCEL_FILE_PATH


    def get_excel_data(self,excel_file_path,moudle_name,case_name):
        # 读取Excel表格：
        book = xlrd.open_workbook(excel_file_path)
        # 根据sheet名称获取sheet对象：
        sheet = book.sheet_by_name(moudle_name)
        # 获取标题：
        title = sheet.row_values(0)
        #获取第二行值
        l = []
        # 循环添加返回列表：
        for row in range(1, sheet.nrows):
           l.append(dict(zip(title, sheet.row_values(row))))
        #return l
        return [l.loc[l[case_name] == 'case_name']]


    def get_excel_data_1(self,excel_file_path,sheet_name):
        # 读取Excel表格：
        book = xlrd.open_workbook(excel_file_path)
        # 根据sheet名称获取sheet对象：
        sheet = book.sheet_by_name(sheet_name)
        # 获取标题：
        title = sheet.row_values(0)
        # 方式二列表解析式返回：
        return [dict(zip(title, sheet.row_values(row))) for row in range(1, sheet.nrows)]

    def get_excel_data_2(self, excel_file_path):
        # 读取Excel表格：
        book = xlrd.open_workbook(excel_file_path)
        # 根据sheet名称获取sheet对象：
        sheet = book.sheet_by_name("pay")
        # 获取标题：
        title = sheet.row_values(0)
        # l = []
        # 方式一循环添加返回列表：
        # for row in range(1, sheet.nrows):
        #     l.append(dict(zip(title, sheet.row_values(row))))
        # return l
        # 方式二列表解析式返回：
        return [dict(zip(title, sheet.row_values(row))) for row in range(1, sheet.nrows)]
    def write_excel(self):
        # 写入Excel表格：
        pass
if __name__ == '__main__':
    print(ExcelHandler().get_excel_data(settings.EXCEL_FILE_PATH))
