import sqlite3

 
X = sqlite3.connect('NeDB.db')
 
Y = X.cursor()

 
Y.execute("SELECT * FROM invoice_items")
new_list=[]
print("All the data")
output = Y.fetchall()
for k in output:
  new_list.append(k[3])
print(new_list)      
X.commit()

Y.close()
