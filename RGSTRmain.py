import time
import calendar
import mysql.connector
from RGSTRconnect import *
from time import sleep

if __name__ == "__main__":
    configfile="config.ini"
    databaseconnect(configfile)
    while True:
        try:
            UID=int(input("input UID"))
            user=databaselookup(UID,configfile)
        except:
            print("Error")
    
        
    
