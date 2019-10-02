import pyodbc
server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

conn_nwdb = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
# print(conn_nwdb)
#
cursor=conn_nwdb.cursor()

# how many orders have ship city from rio de janeiro

query2= cursor.execute("SELECT *  FROM Orders where ship 'city' = 'rio de janeiro' ").fetchone()
print(query2)