#Parameters/variables for connection
import pyodbc
server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'
# Establish a connection
conn_nwdb = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
print(conn_nwdb)