import sqlite3 as sq

con = sq.connect('data.db')
cursor = con.cursor()




cursor.close()
con.close()