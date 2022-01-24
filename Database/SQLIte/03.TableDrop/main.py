import sqlite3

conn = sqlite3.connect('test.db')
conn.execute("DROP TABLE IF EXISTS EMPLOYEE")
conn.execute('''CREATE TABLE EMPLOYEE
         (ID INT NOT NULL,
         NAME TEXT NOT NULL);''')
print("A new Table is created");

conn.close()