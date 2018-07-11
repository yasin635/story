import pymysql,os
#打开数据库连接
db = pymysql.connect(host="127.0.0.1", user="root", password="Aa123456", db="story", port=3306)

#获取句柄
cur = db.cursor()

#查询数据库

sql = "select * from users limit 10"

try:
    cur.execute(sql)
    #获得所有记录
    results = cur.fetchall()
    print("uid", "username", "password")
    # 遍历
    for row in results:
        uid = row[0]
        username = row[1]
        password = row[2]
        print(uid,username,password)
except Exception as e:
    raise e
finally:
    db.close()
        