#coding=utf-8
import random

import pymysql as MySQLdb  #这里是python3
import xlwt
import json
import numpy as np

host = '172.16.200.161'
user = 'eolinker'
passwd = 'eolinker'
port = 3306
db = 'eolinker'
class SelectMySQL(object):
    def select_data(self,sql):
        result = []
        try:
            conn = MySQLdb.connect(host=host,
                               port=port,
                               user=user,
                               passwd=passwd,
                               db=db,
                               charset='utf8', )
            cur = conn.cursor()
            cur.execute(sql)
            alldata = cur.fetchall()
            # print(alldata)
            for rec in alldata:
                result.append(rec[0])
        except Exception as e:
            print('Error msg: ' + e)
        finally:
            cur.close()
            conn.close()

        return result

    def get_result(self, sql, filename):
        print(sql)
        results = self.select_data(sql)
        print('The amount of datas: %d' % (len(results)))
        with open(filename, 'w') as f:
            for result in results:
                f.write(str(result) + '\n')
        print('Data write is over!')
        return results

    def listToJson(lst):

        keys = [str(x) for x in np.arange(len(lst))]
        list_json = dict(zip(lst,""))
        str_json = json.dumps(list_json, indent=2, ensure_ascii=False)  # json转为string
        return str_json



if __name__ == '__main__':
    sql = "select projectID from eo_project where to_days(projectUpdateTime)=to_days(now())"
    select = SelectMySQL()
    projectId = select.get_result(sql, 'namemsg.txt')
    if len(projectId) == 0:
        { print("今天没有更新的接口")}
    else:
        print(projectId)
        for i in range(len(projectId)):
            sql1 = "select apiID from eo_api where to_days(apiUpdateTime)=to_days(now()) and projectID = '%d'" % (projectId[i])
            select = SelectMySQL()
            apiId = select.get_result(sql1,'namemsg.txt')
            print(apiId)
            sql2 = "select envName from eo_api_env where  projectID ='%d'" % (projectId[i])
            select = SelectMySQL()
            envName = select.get_result(sql2, 'namemsg.txt')
            print(envName)
            for j in range(len(apiId)):
                  sql3 = "select apiName from eo_api where  apiID='%d'" % (apiId[j])
                  select = SelectMySQL()
                  apiName = select.get_result(sql3, 'namemsg.txt')
                  print(apiName)
                  sql4 = "select apiURI from eo_api where  apiID='%d'" % (apiId[j])
                  select = SelectMySQL()
                  apiurl = select.get_result(sql4, 'namemsg.txt')
                  print(apiurl)
                  sql5 = "select paramKey from eo_api_request_param where  apiID='%d'" % (apiId[j])
                  select = SelectMySQL()
                  paramKey = select.get_result(sql5, 'namemsg.txt')
                  print(type(paramKey))
                  print(select.listToJson(paramKey))

                  sql6 = "select apiRequestType from eo_api where  apiID='%d'" % (apiId[j])
                  select = SelectMySQL()
                  apiRequestType = select.get_result(sql6, 'namemsg.txt')
                  print(apiRequestType)
                  if apiRequestType == '1':
                      apiRequestValue="post"
                  else:
                      apiRequestValue = "get"

                  # 创建一个workbook 设置编码
                  workbook = xlwt.Workbook(encoding='utf-8')
                  # 创建一个worksheet
                  worksheet = workbook.add_sheet('test'+str(apiId[j]))
                  row0 = [u'case_id', u'case_title', u'case_description', u'case_url', u'case_method', u'case_data',
                        u'case_expect']
                  for i in range(0, len(row0)):
                    worksheet.write(0, i, row0[i])
                  print(apiId[j], apiName, apiurl, paramKey)
                     # 参数对应 行, 列, 值
                  worksheet.write(1, 1, label=apiName)
                  worksheet.write(1, 3, label=apiurl)
                  worksheet.write(1, 4, label=apiRequestValue)
                  worksheet.write(1, 5, label=paramKey)

                  # 保存
                  workbook.save('test.xls')

