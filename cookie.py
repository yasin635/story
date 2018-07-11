from flask import Flask, sessions, session, escape, redirect, url_for, request

app = Flask(__name__)
app.debug = True
@app.route('/')
def index():
    app.logger.debug('A value for debugging')
    app.logger.warning('A warning occurred (%d apples)', 42)
    app.logger.error('An error occurred')
    if 'username' in session:
        return 'logged in as %s ' % escape(session['username'])
    return 'You are not loged in'


# 登录
@app.route('/login', methods=['POST', 'GET'])
def login():

    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
    <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''


app.secret_key = '?pj\xf4\xe2\xfe\x07i\xc2D\xc0]\xa8\xc8\xf9\xfd\xab\xc9\xe7\xea\xc2\xa9\x0fq'
if __name__ == 'main':
    app.run(debug=True)
