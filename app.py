from flask import Flask, render_template
import sqlite3, db1, os, time
app = Flask(__name__)
#app.root_path = os.path.dirname(os.path.abspath(__file__))
@app.route('/')
def read_sqlite_table():
    # items=db1.operators('read_tables')
    # return render_template('mainpage.html',items=items) 
    items=db1.operators('read_tables')
    if(items != None):
        if(len(items)>20):        
            return render_template('mainpage.html',items=items)
    else:
        return '<html><head></head><body><h1 class="h1">No data avaliable</h1></body></html>'
#$env:FLASK_APP = "run.py"