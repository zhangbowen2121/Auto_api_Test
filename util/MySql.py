#导入psycopg2
import psycopg2
# 连接到一个给定的数据库
conn = psycopg2.connect(database="database", user="eolinker",password="eolinker", host="172.16.200.161", port="3306")
#建立游标，用来执行数据库操作
cur = conn.cursor()

#执行SQL命令
cur.execute("SQL命令")

# 获取SELECT返回的元组
rows = cur.fetchall()

# 遍历元组获取值
for row in rows:
    print(row)

# 提交SQL命令
conn.commit()

#关闭游标
cur.close()

#关闭数据库连接
conn.close()