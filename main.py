import sqlite3
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, session, g, url_for, render_template, flash, abort, request, redirect

app = Flask(__name__)
app.config['USERNAME'] = 'amos'
app.config['PASSWORD'] = '123456'
@app.route('/')
def show_entries():
    cur = g.db.execute('select title,text from entrires order by id desc ')
    entries = [dict(title=row[0],text=row[1]) for row in cur.fetchall()]
    return render_template('shoe_entries.html', entries)

@app.route('/add')
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into enterires (title, text) values(?, ?)', [request.form['title'], request.form['text']])
    g.db.commit()
    flash('新增成功')
    return redirect(url_for('show_entries'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] :
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You are logined in')
            return redirect(url_for('show_entries'))
    return render_template('login.bak.html', error=error)
@app.route('/logout')
def logout():
    session.pop('logged_in',None)
    flash('You are loged out ')
    return redirect(url_for('show_entries'))
    

#session key值
app.secret_key = '?pj\xf4\xe2\xfe\x07i\xc2D\xc0]\xa8\xc8\xf9\xfd\xab\xc9\xe7\xea\xc2\xa9\x0fq'
if __name__ == '__main__':
    app.run()