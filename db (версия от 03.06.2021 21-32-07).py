import sqlite3, pathlib, os
from sqlite3 import Error

conn = None
count = 0
def create_connection(command, p = 0):
    """ create a database connection to a SQLite database """
    
    try:
        conn = sqlite3.connect('objects-base.db')
        #print(sqlite3.version)
        c = conn.cursor()
        if p==0:
            c.execute(command)
        if p==228:
            c.executescript(command)
        conn.commit()
        
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
def select(link):
    try: 
        conn = sqlite3.connect('objects-base.db')        
        cur = conn.cursor()         
        cur.execute("select id from tenders where link=:link", {"link":link})
        ident = cur.fetchall()
        if len(ident) <= 0:       #section,dates[i],times[i],counts[i]
            return False
        else:
            return True
        conn.commit()
    except Error as e:
        print(e)
        print('from select')
    finally:
        if conn:
            conn.close()
            
def insert(list1,list2):
    try:
        print('Adding to database...')   
        conn = sqlite3.connect('objects-base.db')        
        cur = conn.cursor()
        for i in range(len(list1[0])):
            if select(list1[0][i]) == False:
                count =+1                
                tendersInsert = "insert or ignore into tenders (link,section,dates,times,counts) values(?,?,?,?,?)" #,section,dates,times,counts
                cur.execute(tendersInsert,(list1[0][i],list1[1][i],list1[2][i],list1[3][i],list1[4][i]))       #section,dates[i],times[i],counts[i]
                last_insert = cur.lastrowid
                itemsInsert = "insert or ignore into items (name,tenderkey) values(?,?)"
                if len(list2[i]) > 1:
                    for x in range(len(list2[i])):
                        cur.execute(itemsInsert,(list2[i][x], last_insert))
                if len(list2[i]) == 1:
                    cur.execute(itemsInsert,(list2[i][0], last_insert))
                conn.commit()
    except Error as e:
        print(e)
        print('from insert')
    finally:
        if conn:
            conn.close()           
# if __name__ == '__main__':
#     path = str(pathlib.Path('pythonsqlite.db'))
#     print(path)
#     create_connection(path)