#coding=utf-8

import pymysql as MySQLdb  #这里是python3
import xlwt

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
        #print(sql)
        results = self.select_data(sql)
        #print('The amount of datas: %d' % (len(results)))
        with open(filename, 'w') as f:
            for result in results:
                f.write(str(result) + '\n')
        #print('Data write is over!')
        return results

if __name__ == '__main__':
    sql = "select projectID from eo_project where to_days(projectUpdateTime)<to_days(now())"
    select = SelectMySQL()
    projectId = select.get_result(sql, 'namemsg.txt')
    sql0 = "select projectName from eo_project where to_days(projectUpdateTime)=to_days(now())"
    select = SelectMySQL()
    projectName = select.get_result(sql0, 'namemsg.txt')
    if len(projectId) == 0:
        { print("今天没有更新的接口")}
    else:
        print("今天共有"+str(len(projectId))+"项目更新接口")
        print("更新的信息有（projectId,projectName,appId,envName,apiurl,apiRequestType,paramKey）:")
        for i in range(len(projectId)):
            sql1 = "select apiID from eo_api where to_days(apiUpdateTime)=to_days(now()) and projectID = '%d'" % (projectId[i])
            select = SelectMySQL()
            apiId = select.get_result(sql1,'namemsg.txt')
            sql11 = "select groupName from eo_api a left join eo_api_group b on a.groupID=b.groupID  where to_days(a.apiUpdateTime)=to_days(now()) and a.projectID = '%d'" % (projectId[i])
            select = SelectMySQL()
            groupName = select.get_result(sql11,'namemsg.txt')
            #print(apiId)
            sql2 = "select envName from eo_api_env where  projectID ='%d'" % (projectId[i])
            select = SelectMySQL()
            envName = select.get_result(sql2, 'namemsg.txt')

            #print(envName)
            for j in range(len(apiId)):
                  sql3 = "select apiName from eo_api where  apiID='%d'" % (apiId[j])
                  select = SelectMySQL()
                  apiName = select.get_result(sql3, 'namemsg.txt')
                  #print(apiName)
                  sql4 = "select apiURI from eo_api where  apiID='%d'" % (apiId[j])
                  select = SelectMySQL()
                  apiurl = select.get_result(sql4, 'namemsg.txt')
                  #print(apiurl)
                  sql5 = "select paramKey from eo_api_request_param where  apiID='%d'" % (apiId[j])
                  select = SelectMySQL()
                  paramKey = select.get_result(sql5, 'namemsg.txt')
                  #print(paramKey)
                  sql6 = "select apiRequestType from eo_api where  apiID='%d'" % (apiId[j])
                  select = SelectMySQL()
                  apiRequestType = select.get_result(sql6, 'namemsg.txt')


                  #print(apiRequestType)
                  if apiRequestType == '1':
                      apiRequestValue="post"
                  else:
                      apiRequestValue = "get"

                  print(projectId[i],projectName[i],groupName[i],apiId[j],apiName,apiurl,apiRequestValue,paramKey)




