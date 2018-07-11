from config import getconfig
from flask import Flask
app = Flask(__name__)

#配置
@app.route('/test')
def testConfig():
    conf = getconfig('config.ini', 'api')
    return 'Test Config.ini %s ' %(conf['port'])

if __name__ == '__main__':
    app.run()