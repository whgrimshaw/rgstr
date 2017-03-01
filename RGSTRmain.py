from time import sleep
import mysql.connector
from RGSTRconnect import *
from RGSTRupdate import *
from RGSTRsetup import *
try:
    import winsound
except ImportError:
    import os
    def playsound(frequency,duration):
        #apt-get install beep
        os.system('beep -f %s -l %s' % (frequency,duration))
else:
    def playsound(frequency,duration):
        winsound.Beep(frequency,duration)

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
            UID=input("input UID")
            #Search database for cards
            user=databaselookup(UID,configfile)
            status=(chr(user[0][2][0]))
            print ('status before:',status)
            updatestatus(UID,status,configfile)
            if status=="1":
                playsound(600,750)
            else:
                playsound(400,750)
        except:
            print("Card ID not found")
            playsound(200,750)
        
