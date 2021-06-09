from flask import Flask, render_template
import sqlite3, db1, os
app = Flask(__name__)
app.root_path = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def read_sqlite_table():
    items=db1.operators('read_sqlite_table')
    return render_template('mainpage.html',items=items)
#$env:FLASK_APP = "run.py"