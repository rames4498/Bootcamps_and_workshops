import sqlite3
conn = sqlite3.connect('my_data.sqlite')
cursor = conn.cursor()
print("Opened database successfully")
cursor.execute('''CREATE TABLE SCHOOL
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         MARKS          INT);''')
cursor.close()
