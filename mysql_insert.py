import pymysql

# 2.插入操作
db = pymysql.connect(host="127.0.01", user="root",
                     password="Aa123456", db="story", port=3306)

# 使用cursor()方法获取操作游标
cur = db.cursor()

sql_insert = """insert into users(username,password) values('liu','1234')"""

try:
    cur.execute(sql_insert)
    # 提交
    db.commit()
except Exception as e:
    # 错误回滚
    db.rollback()
finally:
    db.close()
