import sqlite3
conn = sqlite3.connect('my_data.sqlite')
cursor = conn.cursor()
for row in cursor.execute("SELECT id, name, marks from SCHOOL"):
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("MARKS = ", row[2], "\n")
conn.commit()
conn.close()
