#Parameters/variables for connection
import pyodbc
server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'
# Establish a connection
conn_nwdb = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
print(conn_nwdb)

#Create a cursor
#allows us to execute read only queries on the db
cursor=conn_nwdb.cursor()
cursor.execute("SELECT * FROM Customers")

#Fetch rows from cursor - .fetchone()   #it maintains state
# row = cursor.fetchone()
# print(row)
#
# row = cursor.fetchone() #it maintains state
# print(row.ContactName)
#
# row = cursor.fetchone() #it maintains state
# print(row.ContactName)

# .fetchall()
#This is bad


rows = cursor.execute("SELECT *FROM Customers").fetchall()
print(rows)
#print(len(rows)) #if this is a list then we can iterate

rows = cursor.execute("SELECT * FROM Products").fetchall()
#we can iterate
for record in rows:
    print(type(record))
    print(record.UnitPrice) #we can access the column of a specific record

    # however, this is dangerous as we said.
    # because we can clog our machine with too much data
    #we can use while loop to be more efficient

rows = cursor.execute("SELECT* FROM Products")

while True:
    record= rows.fetchone()
    if record is None:
        break
    print(record.UnitPrice)