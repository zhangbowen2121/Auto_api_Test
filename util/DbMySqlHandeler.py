# -*- coding: utf-8 -*-

"""

Created on Fri Mar 20 10:50:56 2015



@author: sl

"""

import os

import MySQLdb

import pandas as pd

MySQL_NAME = os.getenv('MySQL_NAME', '*')

MySQL_USER = os.getenv('MySQL_USER', '*')

MySQLPASSWORD = os.getenv('MySQL_PASSWORD', '*')

MySQL_HOST = os.getenv('MySQL_HOST', '*')

MySQL_PORT = os.getenv('MySQL_PORT', '*')


# MySQL_NAME = os.getenv('MySQL_NAME', 'mysql')

# MySQL_USER = os.getenv('MySQL_USER', 'root')

# MySQLPASSWORD = os.getenv('MySQL_PASSWORD', '123456')

# MySQL_HOST = os.getenv('MySQL_HOST', 'localhost')

# MySQL_PORT = os.getenv('MySQL_PORT','3306')


def connect():
    db = MySQLdb.connect(host=MySQL_HOST, user=MySQL_USER, passwd=MySQLPASSWORD, db=MySQL_NAME, charset="utf8")

    return db


def sqlSelect(sql, db):
    # include:select

    cr = db.cursor()

    cr.execute(sql)

    rs = cr.fetchall()

    cr.close()

    return rs