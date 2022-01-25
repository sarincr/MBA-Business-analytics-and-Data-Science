import sqlite3

 
X = sqlite3.connect('NeDB.db')
 
Y = X.cursor()

 
Y.execute("SELECT * FROM employees ")

print("All the data")
output = Y.fetchall()
for row in output:
  print(row)
        
X.commit()

Y.close()
