#all the imports
import os
import sqlite3


from flask import Flask, request, session, g, redirect, url_for, abort,render_template, flash

app = Flask(__name__)
app.config['DATABASE'] = '/www/db/storydb'
# 连接数据库
def connect_db():
    """Connects to the speciffic database."""
    # app.logger.warning(app.config['DATABASE'])
    rv = sqlite3.connect("/www/db/storydb.db")
    # rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

#获取数据库连接句柄
def get_db():
    """Opens a new database connection if there is none yet for the current application ocntext"""
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

#断开数据库
def close_db(error):
    """Closes the databse again at the end of the request"""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

# 执行数据库model
def ini_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
            db.commit()

if __name__ == '__main__':
    app.run()