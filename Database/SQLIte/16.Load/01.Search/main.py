import sqlite3

 
X = sqlite3.connect('NeDB.db')
 
Y = X.cursor()

 
Y.execute("SELECT * FROM employees ")

print(Y.fetchall())

        
X.commit()

Y.close()
