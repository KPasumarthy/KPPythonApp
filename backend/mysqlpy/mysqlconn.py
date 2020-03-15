# KP : Import 'MySQL' Connector module
import mysql.connector
#import kppylogs.kplogger_module
#from kppylogs  import *
#import kppylogs.auxiliary_module
#import kppylogs.kplogger_module

#KP : Create 'MySQL' DB Connection
print("KP : mysqlconn.py :  Python 'MySQL' DB Connection" )
mysqldb = mysql.connector.connect(
    host='localhost', 
    port=3306, 
    user='svcaccount',
    passwd='(svcP@33word)'
)
print("KP : mysqlconn.py :  Python Established 'MySQL' DB Connection Successfully" )