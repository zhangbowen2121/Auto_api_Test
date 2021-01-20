# coding=utf-8
import pytest
import sys


def main(argv):
        for name in sys.argv[1:]:
            if name == 'getExamList':
                pytest.main(["-m", "gettoken"])
                pytest.main(["-m", "getExamList"])
                print("getExamList功能测试完成")

            if name == 'getCookie':
                pytest.main(["-m", "TestUser"])
                print("getCookie功能测试完成")

            elif name == 'educational':
                pytest.main(["-m", "TestUser"])
                pytest.main(["-m", "educational"])
        #  pytest.main(["-m", "getTeachingCount"])
        #  pytest.main(["-m", "beixiao"])

                print("getLessonListApp功能测试完成")


if __name__ == "__main__":
    main(sys.argv)

