import sqlite3, pathlib, os, datetime
from sqlite3 import Error

conn = None
dateStr = ''
def operators(operator, tender = None):
    try:
        conn = sqlite3.connect('main.db')
        print(sqlite3.version)
        cur = conn.cursor()
        print("Подключен к SQLite")
        
        if operator=='createTenders':
                cur.execute("create table if not exists tenders ('id' INTEGER PRIMARY KEY AUTOINCREMENT, 'name', 'inn', 'kpp', 'mailAddress', 'category', 'price', 'deliveryAddress', 'link' NOT NULL UNIQUE, 'dynamics', 'dateStart', 'dateEnd', 'items NOT NULL')")
                print('Tables created or exists')
        
        if operator=='read_tables':
            try:
                sqlite_select_query = '''SELECT 'id' , 'name', 'inn', 'kpp', 'mailAddress', 'category', 'price', 'deliveryAddress', 'link', 'dynamics', 'dateStart', 'dateEnd' from tenders'''
                cur.execute(sqlite_select_query)
                if(cur.fetchall!=None):
                    return cur.fetchall()
                else:
                    return None
            except:
                return None
        if operator=='insert':
            tendersInsert = "insert or ignore into tenders (name, inn, kpp, mailAddress, category, price, deliveryAddress, link, dynamics, dateStart, dateEnd,items) values(?,?,?,?,?,?,?,?,?,?,?,?)"
            cur.execute(tendersInsert,(tender.name,tender.inn,tender.kpp,tender.mailAddress,tender.category,tender.price,tender.deliveryAddress,tender.link,tender.dynamics,tender.dateStart,tender.dateEnd,tender.items))
            #dateStr = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        if operator=='drop tables':
            cur.execute('DROP TABLE IF EXISTS tenders;')
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