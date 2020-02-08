import sqlite3
conn = sqlite3.connect('my_data.sqlite')
cursor = conn.cursor()
conn.execute("DELETE from  SCHOOL where ID = 2")
conn.commit()
for row in cursor.execute("SELECT id, name, address, marks from SCHOOL"):
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("ADDRESS = ", row[2])   
   print("MARKS = ", row[3], "\n")
conn.commit()
conn.close()
