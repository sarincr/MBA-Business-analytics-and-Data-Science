import sqlite3

 
X = sqlite3.connect('NeDB.db')
 
Y = X.cursor()

 
Y.execute('''CREATE TABLE IF NOT EXISTS EMPLOYEE (
         	ID integer,
         	Name text NOT NULL,
         	Date_Join text,
            Place text,
            Salary integer,
            Age real);''')

 
Y.execute("INSERT INTO Employee VALUES (1,'John','2020-01-01','Kerala',32,25000)")
 
X.commit()

Y.close()