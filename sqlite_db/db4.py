import sqlite3
conn = sqlite3.connect('my_data.sqlite')
cursor = conn.cursor()
conn.execute("UPDATE SCHOOL set MARKS = 250 where ID = 3")
conn.commit()
for row in cursor.execute("SELECT id, name, address, marks from SCHOOL"):
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("MARKS = ", row[2], "\n")
conn.commit()
conn.close()
