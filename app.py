from flask import Flask, render_template
import sqlite3, db1, os, run, time
app = Flask(__name__)
#app.root_path = os.path.dirname(os.path.abspath(__file__))
@app.route('/')
def read_sqlite_table():
    while True:
        run.runner();
        items=db1.operators('read_tables')
        return render_template('mainpage.html',items=items)
        db1.operators('drop tables')
        time.sleep(900)
#$env:FLASK_APP = "run.py"