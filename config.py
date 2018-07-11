import configparser as ConfigParser

#获取配置
def getconfig(filename, section=''):
    cf = ConfigParser.ConfigParser()
    cf.read(filename)  # 读取配置文件
    cf_items = dict(cf.items(section)) if cf.has_section(section) else {}  # 判断SECTION是否存在,存在把数据存入字典,没有返回空字典
    return cf_items