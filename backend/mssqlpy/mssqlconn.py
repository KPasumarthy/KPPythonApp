### KP : Import 'MSSQL' pyodbc module
import pyodbc

###KP : 'Microsoft SQL' DB Connection  : MSSQL Connection WORKING!!
print("KP : mssqlconn.py : Python 'MSSQL' DB Connection" )
cnxn = pyodbc.connect("Driver={SQL Server};"
                      "Server=localhost;"
                      "Database=AdventureWorks2022;"
                      "UID=sa;PWD=KPSQLServer2022sysadminPassword!;"
                      "Trusted_Connection=yes;")


#KP : 'MSSQL' Define Function to get Connection
def getMSSQLConn():    
    return cnxn.cursor()
cursor = getMSSQLConn()


def msSqlSelect(msSqlStmnt):
    print("KP : mssqlconn.py :  Execute 'MSSQL' Statment!" )
    cursor = cnxn.cursor()
    cursor.execute(msSqlStmnt)
    msSqlResult = cursor.fetchall()
    print("KP : mssqlconn.py :  Python Executed 'MSSQL' Statment Successfully!" )
    return msSqlResult


#KP : MSSQL Statement to Select Top 5 Persons
msSqlStmntTop5Persons = "SELECT TOP 5 * FROM Person.Person"    
personTop5 = msSqlSelect(msSqlStmntTop5Persons)
for person in personTop5:
    print('person = %r' % (person,))



### KP : Import 'MSSQL' pyodbc module
#import pyodbc

###KP : 'Microsoft SQL' DB Connection  : MSSQL Connection WORKING!!
# print("KP : mssqlconn.py : Python 'MSSQL' DB Connection" )
# cnxn = pyodbc.connect("Driver={SQL Server};"
#                       "Server=localhost;"
#                       "Database=AdventureWorks2022;"
#                       "UID=sa;PWD=MSSQLServer2022sysadminPassword!;"
#                       "Trusted_Connection=yes;")


# cursor = cnxn.cursor()
# cursor.execute('SELECT Top 5 * From Person.Person')

# for row in cursor:
#     print('row = %r' % (row,))

