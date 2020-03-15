# KP : Import 'MySQL' Connector module
import mysql.connector
#import kppylogs
#import kppylogs.auxiliary_module
#import kppylogs.kplogger_module

#KP : 'MySQL' DB Connection 
print("KP : mysqlconn.py :  Python 'MySQL' DB Connection" )
mysqldb = mysql.connector.connect(
    host='localhost', 
    port=3306, 
    user='svcaccount',
    passwd='(svcP@33word)'
)
print("KP : mysqlconn.py :  Python Established 'MySQL' DB Connection Successfully" )

#KP : 'MySQL' Define Function to get Connection
def getMySQLConn():    
    return mysqldb

#KP : 'MYSQL' DB Select Statement
def mySqlSelect(mySqlStmnt):
    print("KP : mysqlconn.py :  Execute 'MySQL' Statment!" )
    mycursor = mysqldb.cursor()
    mycursor.execute(mySqlStmnt)
    mySqlResult = mycursor.fetchall()
    print("KP : mysqlconn.py :  Python Executed 'MySQL' Statment Successfully!" )
    return mySqlResult


#KP : MySQL Statement to Select All Cities
sqlStmnt4Cities = "Select * From world.city"
cities = mySqlSelect(sqlStmnt4Cities)
for city in cities:
    print(city)