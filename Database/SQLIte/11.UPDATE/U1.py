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

 
Y.execute("INSERT INTO Employee VALUES (1,'John','2020-03-01','Kerala',32,25000),(2,'Adam','2020-01-01','TN',22,30000),(3,'Mary','2022-01-01','Karnataka',24,120000)")

data = Y.execute("SELECT* from Employee");  
  
for k in data:  
   print ("ID = ", k[0])  
   print ("NAME = ", k[1])  
   print ("Date", k[2])
   print ("Place = ", k[3])  
   print ("Salary = ", k[5])
   print ("Age = ", k[4])


print("..........................................................................")


Y.execute('''UPDATE Employee SET Salary = 50000 WHERE ID=1;''')
X.commit()





data = Y.execute("select * from Employee");  

for k in data:  
   print ("ID = ", k[0])  
   print ("NAME = ", k[1])  
   print ("Date", k[2])
   print ("Place = ", k[3])  
   print ("Salary = ", k[5])
   print ("Age = ", k[4])
   print("........")

  

        
X.commit()

Y.close()
