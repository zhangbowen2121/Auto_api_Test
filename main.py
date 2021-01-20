#coding=utf-8
import pytest
import sys

def main(argv):

    for name in sys.argv[1:]:
        if name == 'appapi':
            pytest.main(["-m", "gettoken"])
            pytest.main(["-m","appapi"])
            print("appapi项目测试完成")
        if name == 'teacherlogin':
            pytest.main(["-m","teacherlogin"])
            print("teacher项目测试完成")
        if name == 'uat':
            #pytest.main(["-m", "uat1"])
            pytest.main(["-m","gettoken"])
            pytest.main(["-m","uat"])
            print("uat测试完成")
        if name == 'token':
            pytest.main(["-m", "gettoken"])
            print("homepage项目测试完成")
        if name == 'list1':
            pytest.main(["-m", "gettoken"])
            pytest.main(["-m","list1"])
            print("uat测试完成")
        elif name == 'login':
            pytest.main(["-m","login"])
            pytest.main(["-m","login_business"])
            print("登录功能测试完成")
        elif name == 'lession':
            pytest.main(["-m", "gettoken"])
            pytest.main(["-m", "lession"])
            print("课堂测试完成")
        elif name == 'push':
            pytest.main(["-m", "push"])
            print("push测试完成")
        elif name == 'homepage':
            pytest.main(["-m", "homepage"])
            print("homepage测试完成")
        elif name == 'listV2V1':
            pytest.main(["-m", "gettoken"])
            pytest.main(["-m", "listV2V1"])
            print("order测试完成")
        elif name == 'paper':
            pytest.main(["-m","paper"])
            print("paper测试完成")
        elif name == 'banner':
            pytest.main(["-m", "gettoken"])
            pytest.main(["-m","banner"])
            print("banner测试完成")
        elif name == 'complain':
            pytest.main(["-m", "gettoken"])
            pytest.main(["-m","complain"])
            print("complain测试完成")
        elif name == 'recorded':
            pytest.main(["-m","recorded"])
            print("recorded测试完成")
        elif name == 'school':
            pytest.main(["-m", "gettoken"])
            pytest.main(["-m", "school"])
            print("school测试完成")
        elif name == 'source':
            pytest.main(["-m", "source"])
            print("source测试完成")
        elif name == 'subscribe':
            pytest.main(["-m", "subscribe"])
            print("subscribe测试完成")
        elif name == 'address':
            pytest.main(["-m", "address"])
            print("address测试完成")
        elif name == 'advert':
            pytest.main(["-m", "advert"])
            print("advert测试完成")
        elif name == 'coach':
            pytest.main(["-m", "coach"])
            print("coach测试完成")
        elif name == 'error':
            pytest.main(["-m", "error"])
            print("error测试完成")
        elif name == 'evaluation':
            pytest.main(["-m", "evaluation"])
            print("evaluation测试完成")
        elif name == 'examing':
            pytest.main(["-m", "examing"])
            print("examing测试完成")
        elif name == 'account':
            pytest.main(["-m", "account"])
            print("account测试完成")
        elif name == 'ykt3_5':
            pytest.main(["-m","ykt3_5"])
            print("ykt3_5测试完成")
        elif name == 'app2_3':
            pytest.main(["-m", "gettoken"])
            pytest.main(["-m","app2_3"])
            print("app2_3功能测试完成")
        elif name == 'recorded':
            pytest.main(["-m","gettoken"])
            pytest.main(["-m","recorded"])
            print("app2_3功能测试完成")
        elif name == 'generateOrderV2V3':
            pytest.main(["-m","gettoken"])
            pytest.main(["-m","generateOrderV2V3"])
            print("generateOrderV2V3功能测试完成")
        elif name == 'listV2V1':
            pytest.main(["-m", "gettoken"])
            pytest.main(["-m","listV2V1"])
            print("listV2V1功能测试完成")
        elif name == 'gettoken':
            pytest.main(["-m","gettoken"])
            print("gettoken功能测试完成")
        elif name == 'getCheckPayCourse':
            pytest.main(["-m", "gettoken"])
            pytest.main(["-m","getCheckPayCourse"])
            print("getCheckPayCourse功能测试完成")
        elif name == 'lessonLeave':
            pytest.main(["-m", "gettoken"])
            pytest.main(["-m", "lessonLeave"])
            print("lessonLeave功能测试完成")
        elif name == 'getCheckPayCourse':
            pytest.main(["-m", "getCheckPayCourse"])
            print("getCheckPayCourse功能测试完成")
        elif name == 'getCheckPayCourse':
            pytest.main(["-m", "getCheckPayCourse"])
            print("getCheckPayCourse功能测试完成")

        elif name == 'getExamList':
            pytest.main(["-m", "gettoken"])
            pytest.main(["-m", "getExamList"])
            print("getExamList功能测试完成")
        elif name == 'gettoken':
            pytest.main(["-m", "gettoken"])
            print("gettoken功能测试完成")



if __name__ == "__main__":
     main(sys.argv)