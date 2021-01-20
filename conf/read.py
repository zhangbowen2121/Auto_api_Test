import configparser
# 实例化ConfigParser对象
import os
def getconf(pName,item):
    conf = configparser.ConfigParser()
    file1 = os.path.dirname(os.path.abspath(__file__)) + "\\"+pName+".conf"
    #print(file1)
    # 打开配置文件
    f = conf.read(file1,encoding = 'utf8')
    # 根据section和option得到option的值
    a = conf.get(pName,item)
    #print(a)
    return a

    def getconf_all(file,pName):
        conf = configparser.ConfigParser()
        parent_dir = os.path.dirname(os.path.abspath(__file__))
        # print(parent_dir)
        # 打开配置文件
        f = conf.read(file, encoding='utf8')
        # 得到该section的所有option
        c = conf.options(pName)
        print(a)
        return c


    def getconf_all_item(file,pName):
        conf = configparser.ConfigParser()
        parent_dir = os.path.dirname(os.path.abspath(__file__))
        # print(parent_dir)
        # 得到该section所有的键值对
        d = dict(conf.items(pName))
        return d


