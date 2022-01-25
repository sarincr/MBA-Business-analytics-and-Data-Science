import sqlite3

 
X = sqlite3.connect('NeDB.db')
 
Y = X.cursor()

 
Y.execute("SELECT * FROM employees ")

print("All the data")
output = Y.fetchmany(5)
for row in output:
  print(row)
  print("......................")
        
X.commit()

Y.close()
