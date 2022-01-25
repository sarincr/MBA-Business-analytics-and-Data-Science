import sqlite3

 
X = sqlite3.connect('SalesDB.db')
 
Y = X.cursor()

 
Y.execute("SELECT * FROM Supermarket_sales")

print("All the data")
output = Y.fetchall()
for k in output:
  print(k)
  print("....................")
X.commit()

Y.close()
