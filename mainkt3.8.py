#coding=utf-8
import pytest
import sys

def main(argv):

    for name in sys.argv[1:]:
         if name == 'getExamList':
            pytest.main(["-m", "gettoken"])
            pytest.main(["-m", "getExamList"])
            print("getExamList功能测试完成")

         if name == 'Tgetname':
            pytest.main(["-m", "Tgetname"])

            print("Tgetname功能测试完成")

if __name__ == "__main__":
     main(sys.argv)