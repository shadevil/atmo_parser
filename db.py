import sqlite3, pathlib
from sqlite3 import Error

conn = None
def create_connection():
    """ create a database connection to a SQLite database """
    
    try:
        conn = sqlite3.connect('objects-base.db')
        #print(sqlite3.version)
        c = conn.cursor()
        create = "create table if not exists tenders ('id' INTEGER PRIMARY KEY AUTOINCREMENT, 'section' NOT NULL, 'link' NOT NULL, 'dynamics' NOT NULL, 'dates' NOT NULL, 'times' NOT NULL, 'counts' NOT NULL, 'addresses')"
        c.execute(create)        
        
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
            
def insert(db_file,links,dynamics,sections,dates,times,counts):
    try:        
        conn = sqlite3.connect(db_file)        
        c = conn.cursor()
        for i in range(len(links)):
            command = "insert into tenders (link,dynamics,section,dates,times,counts) values(?,?,?,?,?,?)" #,section,dates,times,counts
            c.execute(command,(links[1][i],sections[2,i],dates[1,i],times[1,i],counts[1,i]))        #section,dates[i],times[i],counts[i]
            conn.commit()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
    
# if __name__ == '__main__':
#     path = str(pathlib.Path('pythonsqlite.db'))
#     print(path)
#     create_connection(path)