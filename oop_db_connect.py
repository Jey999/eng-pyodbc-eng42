import pyodbc
#Concept of 'strong params'
    #never ever trust user inputs
    #avoid sql injections
    #filter for sql injections

class ConnectMsS():

    def __init__(self,server,database,username,password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.conn_nwdb = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+self.password)
        self.cursor = self.conn_nwdb.cursor()

    def __filter_query(self,query):
        return  self.cursor.execute(query)
        #doing some filtering for bad queries

    def sql_query(self,query):
        return self.__filter_query(query)

    def sql_query_fetchone(self,query):
        return self.__filter_query(query).fetchone()

    def print_all_product_records_from_table (self):
        query_rows = self.__filter_query('SELECT *FROM Products')
        while True:
            record = query_rows.fetchone
            if record is None:
                break
            print(record)

    def average_unit_price_products(self):
        #Query
        query = self.__filter_query('SELECT * FROM Products')
        # summ of all the unit prices
        prices = []
        while True:
            #get indiviual prices and append to my lis
            record = query.fetchone()
            if record is None:
                break
            prices.append(record.UnitPrice)
        #sum all the unit prices
        #divide by length of wos

        return (sum(prices)/len(prices))

#CRUD
# create 1 entry
    # use insert
    # the cursor can not make transaction (go to documentation)
#read all entries
    # fetch all record and return as a list of dictionaries
#read one entry
    #fetch a specific record
    #get one value using id

# update 1 entry
    #the id of the record to update
    # update the specific record
            #the cursor cannot make transaction (go to documentation)

#destroy / one entry

    # the id of th specific record
    #destory the record