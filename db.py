import sqlite3, pathlib
from sqlite3 import Error

conn = None
def create_connection():
    """ create a database connection to a SQLite database """
    
    try:
        conn = sqlite3.connect('objects-base.db')
        #print(sqlite3.version)
        c = conn.cursor()
        create = "create table if not exists tenders ('id' INTEGER PRIMARY KEY AUTOINCREMENT, 'section' NOT NULL, 'link' NOT NULL)"
        c.execute(create)        
        
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
            
def insert(db_file,links,sections):
    try:        
        conn = sqlite3.connect(db_file)        
        c = conn.cursor()
        for i in range(len(links)):
            command = "insert into tenders (link,section) values (?,?)"
            c.execute(command,(links[i],sections[i]))        
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