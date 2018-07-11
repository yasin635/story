import os
from flask import Flask, render_template, request,redirect,url_for,send_from_directory,request
from werkzeug.utils import secure_filename
ALLOWED_EXTENSIONS = set(["txt",'pdf', 'png','jpg', 'jpeg', 'gif'])
app = Flask(__name__)
app.config['UPLOAD_PATH'] = os.getcwd()
app.config['UPLOAD_SIZE'] = 16 * 1024 * 1024
html = '''
    <!DOCTYPE html>
    <title>Upload File</title>
    <h1>图片上传</h1>
    <form method=post enctype=multipart/form-data>
         <input type=file name=file>
         <input type=submit value=上传>
    </form>
    '''


@app.route('/')
def hello_world():
    #存储cookie
    return 'Index!'

@app.route('/hello')
def hello():
    return 'hello'

@app.route('/user')
@app.route('/user/<username>')
def show_user_profile(username=''):
    # 用户个人信息展示
    return render_template("user.html", username=username)
    # return 'User %s' % username


@app.route('/post/<int:post_id>')
# 规定参数格式
def postRequest(post_id=0):
    return 'Id is %s' % post_id


# post get 请求
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return loging(username, password)

    else:
        return login_form()
#文件上传
def allowed_file(filename):
    pass


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
            file_url = url_for('uploaded_file', filename=filename)
            return html + '<br><img src=' + file_url + '>'
    return html

# 登录
def loging(username = '', password = ''):

    error = ""
    if username == "" :
        error = "用户名为空"
        return error
    if password == "" :
        error = "密码为空"
        return error

    return "用户名、密码正确"


# 登录界面
def login_form():
    return render_template('login.bak.html')


#允许上传的文件
def allowed_file(filename):
    return '.' in filename and \
    filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
#获取上传文件路径
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)

#重定向404
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html", error=error)
if __name__ == '__main__':
    app.run()
