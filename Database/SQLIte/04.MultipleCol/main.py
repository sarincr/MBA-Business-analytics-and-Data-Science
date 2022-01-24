import sqlite3

conn = sqlite3.connect('test.db')
conn.execute('''CREATE TABLE IF NOT EXISTS EMPLOYEE (
         	ID integer PRIMARY KEY,
         	Name text NOT NULL,
         	Date_Join text,
         	Date_Rel text.
            Salary integer);''')
print("A new Table is created");

conn.close()

