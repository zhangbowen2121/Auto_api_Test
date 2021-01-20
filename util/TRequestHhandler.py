import json
import datetime
import os
import urllib
import time
from urllib.parse import urlencode, urlparse
import urllib3
import requests
from urllib3.util import timeout
from plugs.get_globals_data import GlobalData
from plugs.get_order_code import get_order_code
from util.DbSqlServer import MSSQL
from util.MD5 import md5
from requests.packages import urllib3
from conf.read import getconf
from conf.settings import ENV

# 导入解析功能：
# 引入日志功能：
from util.LogHandler import logger
# 获取headers：
headers = eval(getconf('teachingApi','headers'))
# 请求地址：
url=getconf('teachingApi',ENV+'_url')
# headers中host信息更新：
headers.update({"Host":url.split('//')[1]})
timeout=2
class tRequestHandler(object):
# 发请求功能：
    def get_response(self,item,Pname,Iname):
        # 获得请求结果：
        # logger().info(item)
        return self._send_msg(item,Pname,Iname)

    def get_response_prec(self,item,Pname,Iname):
        # 获得请求结果：
        # logger().info(item)
        return self._send_msg_prec(item,Pname,Iname)

    def _send_msg(self, item,Pname,Iname, headers=headers):
        start = time.time()
        logger().info("请求url：" + url + getconf(Pname, Iname))
        if item['case_method'] == 'get':
            if len(item['case_headers'])>0:
                headers1 = json.loads(item['case_headers'].replace("\n", "").strip().replace(" ", ""), strict=False)
                if 'token' in headers1:
                   headers.update({"token": GlobalData.token['token']})
                   urllib3.disable_warnings()
                   r = requests.get(url+getconf(Pname,Iname),params=urlencode(json.loads(item['case_data'])),headers=headers,verify=False,timeout=timeout)
                   #logger().info(r.status_code)
            else:
                r = requests.get(url + getconf(Pname,Iname), params=urlencode(json.loads(item['case_data'])), headers=headers,verify=False,timeout=timeout)

        if item['case_method'] == 'post':
            if len(item['case_headers']) > 0:
                if 'token' in headers:
                    if len(GlobalData.token['token'])>1:
                       headers.update({"token":GlobalData.token['token']})
                    else:
                        print("未获取到token")
            if len(item['case_data']) > 0:
                data = json.loads(item['case_data'].replace("\n", "").strip().replace(" ", ""), strict=False)
            if 'order_id' in data:
                if data.get("order_id") == 'auto':
                    order_no = get_order_code()
                    data.update({"order_id":order_no})
            if 'auth_verify_key' in data:
                if data.get("auth_verify_key") is None or data.get("auth_verify_key") == '':
                    sign_data = data.get('mobile') + "-" + str(datetime.datetime.now())[:-3]
                    data.update({"auth_verify_key": md5(sign_data)})
                    logger().info("请求信息：" + json.dumps(data))
                    print(url + getconf(Pname, Iname))
                    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
                    r = requests.post(url + getconf(Pname, Iname), data=json.dumps(data), headers=headers,allow_redirects=False, verify=False, timeout=timeout)
            if 'sign' in data:
                if data.get("sign") is None or data.get("sign")=='':
                    sign_data = data.get('phone')+"-"+str(datetime.datetime.now())[:-3]
                    data.update({"sign":md5(sign_data)})
                    logger().info("请求信息："+json.dumps(data))
                    logger().info(headers)
                    print(url+getconf(Pname,Iname))
                    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
                    r = requests.post(url+getconf(Pname,Iname),data=json.dumps(data),headers=headers,allow_redirects=False,verify=False,timeout=timeout)
            else:
                logger().info("请求信息："+json.dumps(data))
                headers.update({"token": GlobalData.token['token']})
                logger().info(headers)
                urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
                r = requests.post(url+getconf(Pname,Iname),data=json.dumps(data),headers=headers,allow_redirects=False,verify=False,timeout=timeout)
        logger().info("本次调用耗时："+"%.8f"%(time.time() - start))
        time.sleep(1)
        response = r.text
        logger().info("响应信息为"+response)
        #print(response)
        res = self._check_application_response(response,item,Iname)
        return res

    def _send_msg_data(self,item,Pname,Iname,headers=headers):
        if item['case_method'] == 'get':
           r = requests.get(url+getconf(Pname,Iname),params=item['case_data'])
        if item['case_method'] == 'post':
            data = json.loads(item['case_data'].replace("\n", "").strip().replace(" ",""),strict=False)
            if 'sign' in data:
                    if data.get("sign") is None or data.get("sign")=='':
                        sign_data = data.get('phone')+"-"+str(datetime.datetime.now())[:-3]
                        data.update({"sign":md5(sign_data)})
                        logger().info("请求信息："+json.dumps(data))
                        r = requests.post(url+getconf(Pname,Iname),data=json.dumps(data),headers=headers,allow_redirects=False,timeout=timeout)
            else:
                #logger().info(item['case_data'])
                r = requests.post(url+getconf(Pname,Iname),data=item['case_data'],headers=headers,allow_redirects=False,timeout=timeout)
            response = r.text
            logger().info(response)
            return response
    def _getCookie(self,item,Pname,Iname):
        if item['case_method'] == 'post':
            r = requests.post(url + getconf(Pname, Iname), data=item['case_data'], headers=headers,allow_redirects=False, timeout=timeout)

            setCooick=r.headers['Set-Cookie']
           # logger().info(setCooick)

            return setCooick



    def _send_msg_prec(self, item,headers=headers):
        if item['precondition'] is None or item['precondition'] :
           if item['case_method'] == 'get':
             r = requests.get(item['case_url'],params=item['case_data'])
           if item['case_method'] == 'post':
              data = json.loads(item['case_data'].replace("\n", "").strip().replace(" ",""),strict=False)
              if 'sign' in data:
                    if data.get("sign") is None or data.get("sign")=='':
                        sign_data = data.get('phone')+"-"+str(datetime.datetime.now())[:-3]
                        data.update({"sign":md5(sign_data)})
                        logger().info(json.dumps(data))
                        r = requests.post(item['case_url'],data=json.dumps(data),headers=headers,allow_redirects=False,timeout=timeout)
              else:
                logger().info(item['case_data'])
                r = requests.post(item['case_url'],data=item['case_data'],headers=headers,allow_redirects=False,timeout=timeout)
        else:
            pr = json.loads(item['precondition'])
            if 'db' in pr:
                # 初始化数据：
                ms = MSSQL(host="172.16.4.40", user="wangwei", pwd="W?@,w87,90$$rTs", db="GsTest")
                newsql1 = pr.get('db1')
                newsql2 = pr.get('db2')
                Id1 = ms.ExecQuery(newsql1.encode('utf-8'))
                print(Id1)
                Id2 = ms.ExecQuery(newsql2.encode('utf-8'))
                print(Id2)
                if item['case_method'] == 'get':
                    r = requests.get(item['case_url'], params=item['case_data'])
                if item['case_method'] == 'post':
                    data = json.loads(item['case_data'].replace("\n", "").strip().replace(" ", ""), strict=False)
                    if 'sign' in data:
                        if data.get("sign") is None or data.get("sign") == '':
                            sign_data = data.get('phone') + "-" + str(datetime.datetime.now())[:-3]
                            data.update({"sign": md5(sign_data)})
                            logger().info(json.dumps(data))
                            r = requests.post(item['case_url'], data=json.dumps(data), headers=headers,allow_redirects=False, timeout=timeout)
                    else:
                        logger().info(item['case_data'])
                        r = requests.post(item['case_url'], data=item['case_data'], headers=headers,allow_redirects=False, timeout=timeout)
        response = r.text
            #logger().info(response)
        return response

    def _check_application_response(self, response,item,Iname):
        # 处理json类型的响应：
        response = json.loads(response)
        expect = json.loads(item['case_expect'])
        for key, value in expect.items():
            # 意味着预期值的字段跟实际请求结果的字段不一致：断言失败
            if value != response.get(key, None):
                logger().info('请求：{} 断言失败，预期值是：[{}] 实际执行结果：[{}], 相关参数:{}'.format(
                    url+getconf('api',Iname),
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
