import pyodbc
server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

conn_nwdb = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
print(conn_nwdb)

cursor=conn_nwdb.cursor()
total_orders_in_nwd = cursor.execute("SELECT COUNT(*) FROM Orders").fetchone()
print(total_orders_in_nwd)

