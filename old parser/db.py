import sqlite3, pathlib, os
from sqlite3 import Error

conn = None
def create_connection(command, p = 0):
    """ create a database connection to a SQLite database """    
    try:
        conn = sqlite3.connect('main.db')
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
count = 0
def select(link):
    try: 
        conn = sqlite3.connect('main.db')        
        cur = conn.cursor()
        print(link)
        cur.execute("select link from tenders where link=:link", {"link":link})
        ident = cur.fetchall()
        for i in ident:
            print('ident' + i)
        if len(ident) == 0:       #section,dates[i],times[i],counts[i]
            return False
        else:
            print(ident)
            return True
        conn.commit()
    except Error as e:
        print(e)
        print('from select')
    finally:
        if conn:
            conn.close()
            
def read_sqlite_table():
    try:
        sqlite_connection = sqlite3.connect('main.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_select_query = '''SELECT id, section, link, dates, times, counts from tenders'''
        cursor.execute(sqlite_select_query)
        return cursor.fetchall()
        # print("Всего строк:  ", len(records))
        # print("Вывод каждой строки")
        # for row in records:
        #     print("ID:", row[0])
        #     print("Имя:", row[1])
        #     print("Почта:", row[2])
        #     print("Добавлен:", row[3])
        #     print("Зарплата:", row[4], end="\n\n")

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
       
def insert(list1,list2):
    try:
        print('Adding to database...')   
        conn = sqlite3.connect('main.db')        
        cur = conn.cursor()
        for i in range(len(list1[0])):
            #if select(list1[0][i]) == False:
            count =+1              
            tendersInsert = "insert or ignore into tenders (link,section,dates,times,counts) values(?,?,?,?,?)" #,section,dates,times,counts
            cur.execute(tendersInsert,(list1[0][i],list1[1][i],list1[2][i],list1[3][i],list1[4][i]))       #section,dates[i],times[i],counts[i]
            last_insert = cur.lastrowid
            itemsInsert = "insert or ignore into items (name,tenderkey) values(?,?)"
            if len(list2[i]) > 1:
                for x in range(len(list2[i])):
                    #print(list2[i])
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