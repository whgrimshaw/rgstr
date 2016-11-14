import time
import calendar
import mysql.connector
from RGSTRconnect import *
from RGSTRupdate import *
from RGSTRsetup import *

if __name__ == "__main__":
    configfile="config.ini"
    #Connect to database
    database=databaseconnect(configfile)
    if database==(1):
        dbsetup(configfile)
    else:
        pass

    #Poll for cards
    while True:
        UID=int(input("input UID"))
        #Search database for cards
        user=databaselookup(UID,configfile)
        try:
            #status=user
            print (user)
            #print (chr(status))
        except:
            print("User",UID,"not found.")
