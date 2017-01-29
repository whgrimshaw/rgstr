import time
import calendar
import mysql.connector
from RGSTRconnect import *
from RGSTRupdate import *
from RGSTRsetup import *
import nxppy
mifare=nxppy.Mifare()

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
        try:
            UID=mifare.select()
            #Search database for cards
            user=databaselookup(UID,configfile)
            status=(chr(user[0][2][0]))
            print ('status before:',status)
            updatestatus(UID,status,configfile)
            sleep(0.5)
        except nxppy.SelectError:
            sleep(1)
        
        
