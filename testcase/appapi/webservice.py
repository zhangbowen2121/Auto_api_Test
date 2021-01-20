import json

from zeep import Client  # 建议使用该模块


def websevice():
    endpoint_url = 'http://172.16.4.40:8002/CRUDQueryPortalController.svc?wsdl'
    client = Client(endpoint_url)
    print(client)
    result = client.service
    print(result)
    return result

if __name__ == '__main__':
    # 创建websev

    websev = websevice()
     # 调用方式websev.方法名（参数）

    ws = websev.getLessonRosterInfoById("11")
    assert ws.status_code == 200





