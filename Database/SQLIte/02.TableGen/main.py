import sqlite3

conn = sqlite3.connect('test.db')

print("A new Database is created");
conn.execute('''CREATE TABLE COMPANY
         (ID INT NOT NULL,
         NAME TEXT NOT NULL);''')
print("A new Table is created");

conn.close()