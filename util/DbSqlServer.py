from datetime import datetime
import pymssql #引入pymssql模块
class MSSQL:
    # 数据库连接重试功能和连接超时功能的DB连接
    _conn_status = True
    _max_retries_count = 10  # 设置最大重试次数
    _conn_retries_count = 0  # 初始重试次数
    _conn_timeout = 3  # 连接超时时间为3秒
    def __init__(self,host,user,pwd,db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def __GetConnect(self):
        if not self.db:
            raise(NameError,"没有设置数据库信息")
        self.conn = pymssql.connect(host=self.host,user=self.user,password=self.pwd,database=self.db,charset="utf8",timeout=3)
        cur = self.conn.cursor()
        if not cur:
            raise(NameError,"连接数据库失败")
        else:
            return cur

    def ExecQuery(self,sql):

        cur = self.__GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()

        #查询完毕后必须关闭连接
        self.conn.close()
        return resList

    def ExecNonQuery(self,sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()

    def ExecNonQueryInsert(self, sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        returnId=int(cur.lastrowid)
        # print(returnId)
        self.conn.commit()
        self.conn.close()
        return returnId


conn = MSSQL(host="172.16.4.40",user="wangwei",pwd="W?@,w87,90$$rTs",db="GsTest")

# reslist = ms.ExecQuery("select  TOP 3 *  from S_City")
# for i in reslist:
#     print (i)
#updatesql1="select * from v_biz_flow  where sStudentCode='VP87718' and id='2019665'"
now_time = datetime.now()
try:
   updatesql1="update v_biz_flow set Create_Time=datetime.now() where sStudentCode='VP87718' and id='2019665'"
#newsql2="update V_Biz_FlowItem set CreateTime=CONVERT(varchar,GETDATE(),120) where sStudentCode='VP87718' and nBizId='2019665'"
   s1=conn.ExecQuery(updatesql1.encode('utf-8'))
   print(s1)
   conn.commit()
   print('数据提交')
except:
    #conn.rollback()
    print('数据回滚')
    #conn.execute("select cardcode, AccountsCode from [9002].tbCard where cardcode='0000000001'")
    #print(conn.fetchall())
    #conn.close()
#print (newsql2)


#Id2=ms.ExecQuery(newsql2.encode('utf-8'))
#print(Id2)

# newsql="update contract_Statelog set contract_StateName='%s' where id=1"%u'测试'
# print (newsql)
# ms.ExecNonQuery(newsql.encode('utf-8'))

# newsql="delete from contract_Statelog  where id=1"
# print (newsql)
# ms.ExecNonQuery(newsql.encode('utf-8'))