import sqlite3

con = sqlite3.connect('sample.db')
cursor = con.cursor()
cursor.execute('CREATE TABLE data_set(id, name, date)');
cursor.executescript("""
DROP TABLE IF EXISTS data_set;
CREATE TABLE data_set(id , name , date )
""")
cursor.execute("INSERT INTO data_set VALUES(1, 'saito', 19980810)")
cursor.execute("INSERT INTO data_set(id, name, date) VALUES(?,?,?)", (1,'saito',19980810))

p = "INSERT INTO data_set(id, name, date) VALUES(?, ?, ?)"
cursor.execute(p, (1, 'saito', 19980810))
data = [
     (1, "saito", 19980810),
     (2, "hori", 19961015),
     (3, "yoda", 20000505),
     (4, "nishino", 19940525),
     (5, "kitano", 19960717)
 ]
cursor.executemany("INSERT INTO data_set VALUES(?,?,?)", data)
con.commit()
cursor.execute('SELECT * FROM data_set')
cursor.fetchall()
cursor.execute("select * from data_set")
for row in cursor:
     print(row[0], row[1], row[2])

cursor.execute('delete from data_set where id=?', (2,))
cursor.execute('select * from data_set')
cursor.fetchall()

cursor.execute('delete from data_set')
cursor.execute('select * from data_set')
cursor.fetchall()

cursor.execute('drop table data_set')
con.commit()

