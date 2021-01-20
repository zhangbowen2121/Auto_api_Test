from pycparser.c_ast import Default
from ZSI import ServiceProxy
from suds.client import Client
from suds.wsdl import Import
from suds.xsd.doctor import ImportDoctor

proxy = ServiceProxy.ServiceProxy(url)

if __name__ == '__main__':
      client = Client('http://ws.webxml.com.cn/WebServices/MobileCodeWS.asmx?wsdl')
      print(client.service.getMobileCodeInfo('15116020790', ''))
      imp = Import('http://www.w3.org/2001/XMLSchema',
                    location = 'http://www.w3.org/2001/XMLSchema.xsd')
      imp.filter.add('http://WebXml.com.cn/')
      doctor = ImportDoctor(imp)
      #client = Client('http://www.webxml.com.cn/WebServices/WeatherWebService.asmx?wsdl', doctor=doctor)
      #print(client)
      client = Client('http://172.16.4.40:8002/CRUDQueryPortalController.svc?singleWsdl', doctor=doctor,faults=False)
      service = client.service.getLessonRosterInfoById("1222")
      print(service)

      url = 'http://172.16.4.40:8002/CRUDQueryPortalController.svc?Wsdl'

      proxy = ServiceProxy.ServiceProxy(url)  # 是两个ServiceProxy
      person = "{\
          'IDNumber': '4123412412423',\
          'Name': '张三'\
      }"

      account = "{\
          'UserName': 'admin',\
          'Password': '123456'\
      }"
      response = proxy.ExactCheckByJson(request=person, cred=account)