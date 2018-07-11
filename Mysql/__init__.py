import pymysql,os,time
from config import getconfig

class Db:
    # 数据库IP
    host: str = '127.0.0.1'
    # 用户名
    user: str = 'root'
    # 密码
    password: str = ''
    # 数据库
    dbname: str = ''
    # 端口
    port: int = 3306
    # 执行sql语句
    sql:str = ''
    # 获取项目路径
    apppath = os.path.abspath('..')
    #数据库句柄
    link = object
    db = object
    #debug
    debug = True
    
    #初始化
    def __init__(self):
        # 加载配置文件
        print(self.apppath)
        # self.connect_db(self)
    #连接数据库
    def connect_db(self, host = '', user='', password='', db='', port=''):
        # if host == '':
        config_url = self.apppath + '/config/config.ini'
        conf = getconfig(config_url, 'mysql')
        
        self.host = conf['host']
        self.user = conf['user']
        self.password = conf['password']
        self.port = int(conf['port'])
        self.database = conf['database']
        
        self.db = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.database, port=self.port)
        # self.db = pymysql.connect(host="127.0.0.1", user="root", password="Aa123456", db="story", port=3306)
        # 获取句柄
        self.link = self.db.cursor()
        return self.link
    #获取数据库
    def get_db(self, host='',  user='', password='', db='', port=''):
        self.link = self.connect_db(self,host, user, password, db, port)
        return self.link
    #关闭数据库
    def close_db(self):
        self.link.close()
    
    #查询操作
    def select(self,fields, table, condition = '', order='', limit=''):
        self.get_db(self)
        fields = '*' if fields == '' else fields
        sql = 'SELECT '
        sql += fields
        sql += ' FROM '
        sql += table
        self.sql = sql
        self.link.execute(sql)
        # 获得所有记录
        results = self.link.fetchall()
        self.debugTrace(self)
        return results
    def insert(self,table, data):
        #字段值
        fields = ''
        values = ''
        i = 0
        for key, val in data.items():
            split = ',' if i > 0 else ''
            fields +=  split+ ' `'+key+'` '
            values +=  split+ " '"+val+"' "
            i = i + 1
        # fields = dict.keys()
        # values = dict.values()
        sql = 'INSERT INTO '
        sql += table
        sql += ' ('+fields+') '
        sql += ' VALUE ('+values+') '
        self.sql = sql
        self.execute(self,self.sql)
    
    #更新
    def update(self,table='', data = {}, condition=''):
        # 字段值
        setField = ''
        i = 0
        for key, val in data.items():
            split = ',' if i > 0 else ''
            setField += split + " `" + key + "` =  '"+ val +"'"
            i = i + 1
        sql = 'UPDATE '
        sql += table
        sql += " SET " + setField
        if condition != '':
            sql += ' WHERE ' + condition
        
        self.sql = sql
        self.execute(self,self.sql)
        
    #删除
    def delete(self, table='', condition=''):
        # 字段值
        sql = 'DELETE FROM '
        sql += table
        if condition != '':
            sql += ' WHERE ' + condition
    
        self.sql = sql
        self.execute(self, self.sql)
    
    #执行Sql
    def execute(self,sql = ''):
        self.debugTrace(self)
        if sql == '':
            return False
        self.get_db(self)
        try:
            rs = self.link.execute(sql)
            # 提交
            self.db.commit()
        except Exception as e:
            # 错误回滚
            self.db.rollback()
            return e
            # raise e
        finally:
            self.db.close()
        return rs
    #debug
    def debugTrace(self):
        if self.debug == True:
            print(self.sql)
        return
    
#打开数据库连接

db = Db
data = dict(username="amos3",password="123234",register_time=str(int(time.time())))
print(data)
# rs = db.insert(db, 'users',data)
# rs = db.update(db, 'users',data,' uid = 1')
# rs = db.select(db,'*','users')
rs = db.delete(db,'users',"uid=2")
print(rs)