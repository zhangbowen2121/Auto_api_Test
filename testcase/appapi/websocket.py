#coding=utf-8
from data import dict1
import httplib.client


def Featchinfo():
 url="test.beat.com"
 port=9700
 path="/oqq_ws_51/Name.asmx"
 header={'Content-Type' : 'text/xml; charset=utf-8'}
 conn = httplib.client.HTTPConnection(url,port,timeout=10)
 for key,value in dict1.items():
     conn.request('POST',path,value.encode('utf-8'),header)
     response=conn.getresponse()
     resp=response.read()
     if(key=="success" and "resultStatusFlag=\"SUCCESS" in str(resp)):
         print("case1 验证通过")
     elif(key=="fail" and "resultStatusFlag=\"FAIL" in str(resp)):
         # print(resp)
         print("case2 验证通过")

if __name__ == '__main__':

 conn = httplib.client.HTTPConnection("www.google.cn")
 conn.request('get', '/')
 print
 conn.getresponse().read()
 conn.close()