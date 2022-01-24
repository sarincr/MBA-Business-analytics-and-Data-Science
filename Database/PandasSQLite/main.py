import sqlite3
import pandas as pd

conn = sqlite3.connect('my_data.db')

c = conn.cursor()

df = pd.read_excel('SalesData.xlsx')

df.to_sql('df', conn, if_exists='append', index = False, chunksize = 10000)


data = conn.execute("SELECT * from df ");  

 

 

  
for k in data:
   print (k)  
 
conn.commit()

conn.close()
