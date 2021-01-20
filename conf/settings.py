import os
import sys
import datetime
#测试环境
ENV = 'test'
#生产环境
#ENV = 'online'
# 根目录：
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Excel数据文件夹命名：
DATA_PATH = os.path.join(BASE_PATH,'data')
# ---------------- 日志相关 --------------------
# 日志级别：
LOG_LEVEL = 'debug'
LOG_STREAM_LEVEL = 'debug'  # 屏幕输出流
LOG_FILE_LEVEL = 'info'   # 文件输出流
# 日志文件夹命名：
LOG_FILE_NAME = os.path.join(BASE_PATH,'logs', datetime.datetime.now().strftime('%Y-%m-%d') + '.log')
# ---------------- Excel相关 --------------------
if __name__ == '__main__':
    # 添加顶级目录：
    sys.path.insert(0, BASE_PATH)
    print(sys.path)
# ---------------- Allure相关 ----------------------
# 报告路径：
REPORT_PATH = os.path.join(BASE_PATH, 'report')
# Allure的json文件夹命名：
ALLURE_JSON_DIR_NAME = 'allure-results'
# Allure的json文件路径：
ALLURE_JSON_DIR_PATH = os.path.join(REPORT_PATH, ALLURE_JSON_DIR_NAME)
# allure的html文件夹命名：
ALLURE_REPORT_DIR_NAME = os.path.join(REPORT_PATH, 'allure-report')
# allure的html报告路径
ALLURE_REPORT_DIR_PATH = os.path.join(REPORT_PATH, ALLURE_REPORT_DIR_NAME)
# 压缩包路径：
ZIP_FILE_PATH = os.path.join(REPORT_PATH, 'report.zip')
# 生成报告命令：
ALLURE_COMMAND = "allure generate {} -o {}".format(ALLURE_JSON_DIR_PATH, ALLURE_REPORT_DIR_PATH)
# ------------------- 邮件相关 -----------------
# 第三方 SMTP 服务：
MAIL_HOST = "smtp.qq.com"
MAIL_USERNAME = "510760051@qq.com"
MAIL_TOKEN = "mpaocydzpzfjidge"
# 收件人，收件人可以有多个，以列表形式存放：
RECEIVERS = ['1510760051@qq.com', '610760051@qq.com']
# 邮件主题、收件人、发件人：
MAIL_SUBJECT = '高思APPapi自动化接口测试结果'
# 可修改：设置收件人和发件人
SENDER = '15910766894@163.com'  # 发件人
# 邮件正文
#MAIN_CONTENT = 'hi man：\r这是今日的{excel_file_name}的测试报告\r详情下载附件\r查看方法，终端执行 allure open report\r测试人:{execute_tests_name},联系电话：{execute_tests_phone} \r{execute_tests_date}'.format(
 #   excel_file_name=EXCEL_FILE_NAME,
#  execute_tests_name="王薇",
 #   execute_tests_phone=18301056413,
 #   execute_tests_date=datetime.datetime.date(datetime.datetime.now())
#)
