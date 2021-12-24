from flask import Flask, render_template
import sqlite3, db1, os, time
app = Flask(__name__)
#app.config['SERVER_NAME'] = '10.0.0.95:5000'
#app.root_path = os.path.dirname(os.path.abspath(__file__))
message = '<html><head></head><body><h1 class="h1">Данные загружаются. Пожалуйста, обновите страницу через пару минут.</h1></body></html>'
@app.route('/')
def read_sqlite_table():
    # items=db1.operators('read_tables')
    # return render_template('mainpage.html',items=items) 
    items=db1.operators('read_tables')
    dateStr = db1.dateStr
    if(items != None):
        if(len(items)>20):        
            return render_template('mainpage.html',items=items, dateStr=dateStr)
        else:
            return message
    else:
        return message
#$env:FLASK_APP = "run.py"