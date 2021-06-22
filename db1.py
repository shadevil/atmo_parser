import sqlite3, pathlib, os
from sqlite3 import Error

conn = None
items = None
def operators(operator, p1=None, p2=None):
    try:
        conn = sqlite3.connect('main.db')
        #print(sqlite3.version)
        cur = conn.cursor()
        print("Подключен к SQLite")
        
        if operator=='createTenders':
                cur.execute("create table if not exists tenders ('id' INTEGER PRIMARY KEY AUTOINCREMENT, 'section', 'link' NOT NULL UNIQUE, 'dynamics', 'dates', 'times', 'counts', 'addresses',items,dateInsert)")
                print('Tables created or exists')
        # if operator=='createItems':
        #         cur.executescript("PRAGMA foreign_keys=on; create table if not exists items ('id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 'name' NOT NULL, 'tenderkey' INTEGER NOT NULL, FOREIGN KEY ('tenderkey') REFERENCES tenders(id))")
        #         print('Items created or exists')
        
        if operator=='read_tables':
            #sqlite_select_query = '''SELECT t.id, t.section, t.link, t.dates, t.times, t.counts, GROUP_CONCAT(i.name,',') as names from tenders t inner join items i on t.id=i.tenderkey'''
            sqlite_select_query = '''SELECT id, section, link, dates, times, counts, items, dateInsert from tenders'''
            cur.execute(sqlite_select_query)
            return cur.fetchall()
        if operator=='insert':
            for i in range(len(p1[0])):
                #if select(list1[0][i]) == False:
                #for x in range(len(p2[i])):
                items = ','.join(p2[i])
                tendersInsert = "insert or ignore into tenders (link,section,dates,times,counts,items,dateInsert) values(?,?,?,?,?,?,DATE('now'))" #,section,dates,times,counts
                cur.execute(tendersInsert,(p1[0][i],p1[1][i],p1[2][i],p1[3][i][7:],p1[4][i],items))
                #section,dates[i],times[i],counts[i]
                print(items)

        if operator=='drop tables':
            cur.execute('DROP TABLE IF EXISTS tenders;')
            #cur.execute('DROP TABLE IF EXISTS items;')
        cur.close()
        conn.commit()
    except Error as e:
        print("Ошибка при работе с SQLite", e)
    finally:
        if conn:
            conn.close()
            print("Соединение с SQLite закрыто")
            
# if operator=='select':
        #     cur.execute("select link from tenders where link=:link", {"link":link})
        #     ident = cur.fetchall()
        #     for i in ident:
        #         print('ident' + i)
        #     if len(ident) == 0:       #section,dates[i],times[i],counts[i]
        #         return False
        #     else:
        #         print(ident)
        #         return True
        
        
        #last_insert = cur.lastrowid
                # itemsInsert = "insert or ignore into items (name,tenderkey) values(?,?)"
                # if len(p2[i]) > 1:
                #     for x in range(len(p2[i])):
                #         cur.execute(itemsInsert,(p2[i][x], last_insert))
                # if len(p2[i]) == 1:
                #     cur.execute(itemsInsert,(p2[i][0], last_insert))