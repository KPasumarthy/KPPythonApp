### KP : Import 'MSSQL' Connector module
import pyodbc

#KP : 'Microsoft SQL' DB Connection 
print("KP : mssqlconn.py : Python 'MSSQL' DB Connection" )
cnxn = pyodbc.connect("Driver={SQL Server};"
                      "Server=localhost;"
                      "Database=AdventureWorks2022;"
                      "UID=sa;PWD=MSSQLServer2022sysadminPassword!;"
                      "Trusted_Connection=yes;")


cursor = cnxn.cursor()
cursor.execute('SELECT Top 5 * From Person.Person')

for row in cursor:
    print('row = %r' % (row,))

