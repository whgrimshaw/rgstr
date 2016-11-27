import time
import calendar
import mysql.connector
from RGSTRconnect import *
from RGSTRupdate import *
from RGSTRsetup import *

if __name__ == "__main__":
    configfile="config.ini"
    #Connect to database
    conn=databaseconnect(configfile)
    cursor=conn.cursor()
    try:
        cursor.execute("SELECT *\nFROM users")
    except:
        dbsetup(configfile,cursor)
    #Poll for cards
    while True:
        UID=int(input("input UID"))
        #Search database for cards
        user=databaselookup(UID,configfile)
        status=(chr(user[0][2][0]))
        print ('status before:',status)
        updatestatus(UID,status,configfile)
        
