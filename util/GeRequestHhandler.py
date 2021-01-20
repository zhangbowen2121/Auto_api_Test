import json
import datetime
import time

import grequests
import requests
from urllib import parse
from urllib.parse import urlencode

import requests
from urllib3.util import timeout

from plugs.get_globals_data import GlobalData
from plugs.get_order_code import get_order_code
from util.MD5 import md5


# 导入解析功能：
# 引入日志功能：
from util.LogHandler import logger

headers = {'Content-Type': 'application/json;charset=UTF-8',
           'Accept':     'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, sdch, br',
           'Accept-Language': 'zh-CN,zh;q=0.8',
           'Connection': 'keep-alive',
           'Host': 'vipapp.tun.aitifen.cn',
           'Upgrade-Insecure-Requests': '1',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
# headers = {'Host' : 'vipapp.tun.aitifen.cn','Content-Type': 'application/json;charset=UTF-8'}
class GeRequestHandler(object):
# 发请求功能：
    def get_response(self, item):
        # 获得请求结果：
        # logger().info(item)
        return self._send_msg(item)

    def _send_msg(self, item):
        start = time.time()
        if item['case_method'] == 'get':
            headers = json.loads(item['case_headers'].replace("\n", "").strip().replace(" ", ""), strict=False)
            if 'token' in headers:
                #    logger().info(headers)
                #    logger().info(GlobalData.token['token'])
                headers.update({"token": GlobalData.token['token']})
                logger().info(item['case_data'])
                r = grequests.get(item['case_url'],params=urlencode(json.loads(item['case_data'])),headers=headers)
        if item['case_method'] == 'post':
            #logger().info(item['case_data'])
            data = json.loads(item['case_data'].replace("\n", "").strip().replace(" ",""),strict=False)
            headers = json.loads(item['case_headers'].replace("\n", "").strip().replace(" ",""),strict=False)
            #logger().info(data)
            if 'token' in headers:
            #    logger().info(headers)
                 logger().info(GlobalData.token['token'])
                 headers.update({"token":GlobalData.token['token']})
            if 'order_id' in data:
                if data.get("order_id") == 'auto':
                    order_no = get_order_code()
                    logger().info(order_no)
                    data.update({"order_id":order_no})
                    logger().info(data)
            if 'sign' in data:
                if data.get("sign") is None or data.get("sign")=='':
                    sign_data = data.get('phone')+"-"+str(datetime.datetime.now())[:-3]
                    # logger().info(type(sign_data))
                    data.update({"sign":md5(sign_data)})
                    logger().info(json.dumps(data))
                    logger().info(headers)
                    r = grequests.post(item['case_url'],data=json.dumps(data),headers=headers,allow_redirects=False)
            else:
                logger().info(json.dumps(data))
                r = grequests.post(item['case_url'],data=json.dumps(data),headers=headers,allow_redirects=False)
        print(time.time() - start)
        response = r.text
        logger().info("响应信息为"+response)
        #print(response)
        res = self._check_application_response(response,item)
        return res


    def _send_msg_data(self, item):
        if item['case_method'] == 'get':
           r = requests.get(item['case_url'],params=item['case_data'])
        if item['case_method'] == 'post':
            data = json.loads(item['case_data'].replace("\n", "").strip().replace(" ",""),strict=False)
            if 'sign' in data:
                    if data.get("sign") is None or data.get("sign")=='':
                        sign_data = data.get('phone')+"-"+str(datetime.datetime.now())[:-3]
                        data.update({"sign":md5(sign_data)})
                        logger().info(json.dumps(data))
                        r = requests.post(item['case_url'],data=json.dumps(data),headers=headers,allow_redirects=False)
            else:
                logger().info(item['case_data'])
                start = time.time()
                r = grequests.post(item['case_url'],data=item['case_data'],headers=headers,allow_redirects=False)
            response = r.text
            print(time.time() - start)
            #logger().info(response)
            return response

    def _check_application_response(self, response, item):
        # 处理json类型的响应：
        response = json.loads(response)
        expect = json.loads(item['case_expect'])
        for key, value in expect.items():
            # 意味着预期值的字段跟实际请求结果的字段不一致：断言失败
            if value != response.get(key, None):
                logger().info('请求：{} 断言失败，预期值是：[{}] 实际执行结果：[{}], 相关参数:{}'.format(
                    item['case_url'],
                    value,
                    response.get(key, None),
                    item
                ))
                return (value, response.get(key, None))
        else:
            # 断言成功
            return (value, response.get(key, None))


if __name__ == '__main__':
    pass
