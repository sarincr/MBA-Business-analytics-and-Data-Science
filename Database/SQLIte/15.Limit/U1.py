import sqlite3

 
X = sqlite3.connect('NeDB.db')
 
Y = X.cursor()

 
Y.execute('''CREATE TABLE IF NOT EXISTS EMPLOYEE (
         	ID integer,
         	Name text NOT NULL,
         	Date_Join text,
            Place text,
            Age integer,
            Salary real);''')

 
Y.execute('''INSERT INTO Employee VALUES (1,'John','2020-03-01','Kerala',32,25000),(2,'Adam','2020-01-01','TN',22,30000),(3,'Mary','2022-01-01','Karnataka',24,120000)
          ,(4,'Jacob','2022-01-01','Mharashtra',24,430000),(5,'Johny','2022-01-01','Karnataka',24,34000),(6,'Lynda','2022-01-01','Delhi',24,56700),
          (7,'Smith','2022-01-01','Kerala',24,234000),(8,'Gem','2022-01-01','Karnataka',24,120000)''')

data = Y.execute("SELECT * from Employee LIMIT 2 OFFSET 4");  

  
for k in data:
   print (k)  
 
X.commit()

Y.close()
